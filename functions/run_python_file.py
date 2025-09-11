def run_python_file(working_directory, file_path, args=[]):
    import os
    import subprocess

    path = os.path.join(working_directory, file_path)
   
    oscwd = os.getcwd() 
    new_file = os.path.abspath(path) 
    if file_path.startswith('..'):
        return f'Error: Cannot execute "{file_path}" as it is outside'
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
                return f'Error: File "{file_path}" not found.'
        else:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
    

