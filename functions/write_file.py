import os
from google.genai import types

def write_file(working_directory, file_path, content):
      
      path=os.path.join(working_directory, file_path)
      oscwd=os.getcwd()         
      new_file=os.path.abspath(path)
      if new_file.startswith(oscwd):                    
            print(f'Writing to file: {file_path}')
            if os.path.exists(new_file):   
                try:
                    with open(new_file, "w") as f:
                        f.write(content)
                        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
                except Exception as e:
                    return f'Error: Could not write to file "{file_path}". {str(e)}'               
            else:
                print(f'Error: File not found creating new file : "{file_path}"')
                with open(new_file, "w") as f:
                    f.write(content)
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
      else :
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'      
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Write to a file  in the working directory with given content .",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory to   file ,to be writen to ,  file path to the file and content to be written into the file",
            ),
        },
    ),
)
