import os
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
        
write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")