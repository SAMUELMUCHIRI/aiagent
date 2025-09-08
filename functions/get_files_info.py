import os
def get_files_info(working_directory, directory="."):
    try:
        if os.path.isdir(directory):
            if directory.startswith(working_directory):        
                path=os.path.join(working_directory, directory)
                return os.listdir(path)
            else :
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f'Error: {str(e)}'
    