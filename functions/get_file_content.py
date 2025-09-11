import os
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    try:
        path=os.path.join(working_directory, file_path)
        oscwd=os.getcwd()   

        
        new_file=os.path.abspath(path)
    
        if new_file.startswith(oscwd):                    
            if os.path.isfile(new_file):        
            
                    try:                        
                        with open(new_file, "r") as f:
                            file_content_string = f.read() 
                            n_chars = len(file_content_string)
                            print(f'File "{file_path}" read successfully.')
                            if n_chars > MAX_CHARS:
                                return file_content_string[0:MAX_CHARS] + f"[...File {file_path} truncated at {MAX_CHARS} characters]."                               
                            else:
                                return file_content_string
                    except Exception as e:
                        return f'Error: Could not read file "{file_path}". {str(e)}'                 
                                    
            else:
                return  f'Error: File not found or is not a regular file: "{file_path}"'              
        else :
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

           
            
       
    except Exception as e:
        return f'Error: {str(e)}'

print(get_file_content("calculator", "lorem.txt"))