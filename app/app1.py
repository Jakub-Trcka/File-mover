from pathlib import Path
from funcions import *


name_of_the_folder = 'File_orginazer'
path_of_the_folder = f"C:/Users/HP/{name_of_the_folder}"
name_of_folder_with_moved_files = 'File_orginazer'
path_of_folder_with_moved_files = f"C:/Users/HP/{name_of_folder_with_moved_files}"

files_to_move = Path(path_of_the_folder)
create_folder(files_to_move)

for file in files_to_move.iterdir():
    if file.is_file():
        extension = str(file.suffix)
        name_ = str(file.stem)

        try:
            CreateName(f"{path_of_folder_with_moved_files}/DCIM", ".jpg", file, extension, name_)
            CreateName(f"{path_of_folder_with_moved_files}/DCIM", ".mp4", file, extension, name_)
            CreateName(f"{path_of_folder_with_moved_files}/DCIM", ".png", file, extension, name_)
        except IndexError:
            pass

        CreateNow(f"{path_of_folder_with_moved_files}/DCIM", ".jpg", file, extension, name_)
        CreateNow(f"{path_of_folder_with_moved_files}/DCIM", ".mp4", file, extension, name_)
        CreateNow(f"{path_of_folder_with_moved_files}/DCIM", ".png", file, extension, name_)

        CreateNow(f"{path_of_folder_with_moved_files}/Python", ".py", file, extension, name_)
        CreateNow(f"{path_of_folder_with_moved_files}/Text", ".txt", file, extension, name_)
        CreateNow(f"{path_of_folder_with_moved_files}/Program_Installers", ".exe", file, extension, name_)
        CreateNow(f"{path_of_folder_with_moved_files}/Compress_files", ".zip", file, extension, name_)
        CreateNow(f"{path_of_folder_with_moved_files}/Compress_files", ".rar", file, extension, name_)
        