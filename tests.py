from functions.get_files_info import *

get_files_info("calculator", ".") 
get_files_info("calculator", "pkg") 
print(get_files_info("calculator", "/bin"))


print(get_files_info("calculator", "../"))