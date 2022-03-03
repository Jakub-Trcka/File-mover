from pathlib import Path
from funcions import *

name_of_your_folder = 'File_orginazer'
path = f"C:/Users/HP/{name_of_your_folder}"
path2 = f"C:/kuba"

files_to_move = Path(path)
create_folder(path)

for file in files_to_move.iterdir():
    # if file.is_file():
    e = str(file.suffix)
    n = str(file.stem)
    full_name = f'{n}{e}'

    CreateNoMatterSuffix(f'{path2}/Portfófio' , file, full_name)