import os
from pathlib import Path
import shutil

def optimize_storage():

    user_temp_folder = "C:/Users/SAMKEZ~1/AppData/Local/Temp"
    files_in_temp = os.listdir(user_temp_folder)
    size_of_temp = os.path.getsize(user_temp_folder)


    #temp folder_2 (temp folder for windows caching)
    win_temp_folder = "C:/Windows/Temp"
    files_in_temp_2 = os.listdir(win_temp_folder)
    size_of_temp_2 = os.path.getsize(win_temp_folder)

    
    Total_size_temp = size_of_temp+size_of_temp_2
    Total_size_MB = Total_size_temp/1024 
    
    print(Total_size_MB)

    for file in files_in_temp:
        file_path = os.path.join(user_temp_folder,file)
        
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
                print("file removed")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print("file removed")
        
        except Exception as e:
            print(f'\n Failed to delete {file_path}. \n Reason: {e}')   
    
    for file in files_in_temp_2:
        file_path = os.path.join(win_temp_folder,file)
        
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
                print("file removed")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                
                print("file removed")

        except Exception as e:
            print(f'\n Failed to delete {file_path}. \n Reason: {e}')

    Total_size_MB = Total_size_MB

if __name__ == "__main__":
    print("you executed storage_optimizer.py")
else:
    print("you imported this file from somewhere else")
