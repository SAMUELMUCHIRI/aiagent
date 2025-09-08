import os
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

get_files_info("calculator", ".") 
get_files_info("calculator", "pkg") 
print(get_files_info("calculator", "/bin"))


print(get_files_info("calculator", "../"))