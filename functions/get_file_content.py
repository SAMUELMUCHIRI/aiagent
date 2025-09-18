import os
from config import MAX_CHARS

from google.genai import types
def get_file_content(working_directory, directory):
    try:
        path=os.path.join(working_directory, directory)
        oscwd=os.getcwd()   

        
        new_file=os.path.abspath(path)
    
        if new_file.startswith(oscwd):                    
            if os.path.isfile(new_file):        
            
                    try:                        
                        with open(new_file, "r") as f:
                            file_content_string = f.read() 
                            n_chars = len(file_content_string)
                            print(f'File "{directory}" read successfully.')
                            if n_chars > MAX_CHARS:
                                return file_content_string[0:MAX_CHARS] + f"[...File {directory} truncated at {MAX_CHARS} characters]."                               
                            else:
                                return file_content_string
                    except Exception as e:
                        return f'Error: Could not read file "{directory}". {str(e)}'                 
                                    
            else:
                return  f'Error: File not found or is not a regular file: "{directory}"'              
        else :
            return f'Error: Cannot read "{directory}" as it is outside the permitted working directory'

           
            
       
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Get the contents of a file , truncated to {MAX_CHARS} characters in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory to get content from file , and file path to the file .",
            ),
        },
    ),
)