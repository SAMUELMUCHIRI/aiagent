import os
import subprocess
from google.genai import types
def run_python_file(working_directory, directory, args=[]):
    

    path = os.path.join(working_directory, directory)
   
    oscwd = os.getcwd() 
    new_file = os.path.abspath(path) 
    if directory.startswith('..'):
        return f'Error: Cannot execute "{directory}" as it is outside'
    else:
        if new_file.startswith(oscwd):
            if os.path.isfile(path):
                if new_file.endswith('.py'):
                        try:
                            result=subprocess.run(['python3', new_file] + args ,
                            timeout=30 ,
                            stderr=subprocess.STDOUT,
                            stdout= subprocess.PIPE, 
                            text=True)
                            return_string= f'''STDOUT: \n 
                            {result.stdout if result.stdout != None else "No output produced."}  \n
                            STDERR: \n
                            {result.stderr} \n
                            Return code: {0 if result.returncode == 0 else f"Process exited with code {result.returncode}"}'''
                            return return_string
                        except Exception as e:
                            return f"Error: executing Python file: {e}"
                else:
                    return "not a python file"
            else:
                return f'Error: File "{directory}" not found.'
        else:
            return f'Error: Cannot execute "{directory}" as it is outside the permitted working directory'
        
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"run a python file in the working directory with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory to run  the  file ,  file path to the file and optional arguments to be accepted into the function",
            ),
        },
    ),
)
