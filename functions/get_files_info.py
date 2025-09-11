import os

from google.genai import types



def get_files_info(working_directory, directory="."):
    try:
        path=os.path.join(working_directory, directory)
        oscwd=os.getcwd()
        if directory=='.':
                    print(f'Result for current directory:')
        else:   
            print(f'Result for \'{directory}\' directory:')
        if directory.startswith('..'):
            return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:        
            if os.path.isdir(oscwd+"/"+path):
                if os.path.isdir(path):
                    files= os.listdir(path)
                    
                    for file in files:
                        if file.startswith('_'):
                            continue
                        else:
                            if os.path.isfile(path+"/"+file): 
                                print(f'- {file}:  file_size={os.path.getsize(path+"/"+file)} bytes, is_dir=False')
                            elif os.path.isdir(path+"/"+file):
                                print(f'- {file}:  file_size={os.path.getsize(path+"/"+file)} bytes, is_dir=True')
                    
                else:
                    return f'   Error: "{directory}" is not a directory'
            else:
                return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'       
                
       
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)