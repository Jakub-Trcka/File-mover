from datetime import datetime
from pathlib import Path
import os

our_files = Path("C:/Kuba/code/file_mover/files")
text = "C:/Kuba/code/file_mover/text"
python = "C:/Kuba/code/file_mover/python"
dcim = "C:/Users/HP/Pictures/DCIM"

now = datetime.now()
current_time = now.strftime("%D")
month = current_time.split('/')[0]
year = '20' + current_time.split('/')[2]

directory_name_year_text = text + "/" + year
directory_name_year_python = python + "/" + year
directory_name_year_dcim = dcim + "/" + year

directory_name_month_text = directory_name_year_text + "/" + month
directory_name_month_python = directory_name_year_python + "/" + month
directory_name_month_dcim = directory_name_year_dcim + "/" + month



for file in our_files.iterdir():
    directory = file.parent
    extension = file.suffix
    old_name = file.stem

    file_path_text_year = f"{directory_name_year_text}/{old_name}{extension}"
    file_path_python_year = f"{directory_name_year_python}/{old_name}{extension}"
    file_path_dcim_year = f"{directory_name_year_dcim}/{old_name}{extension}"

    file_path_text_month = f"{directory_name_month_text}/{old_name}{extension}"
    file_path_python_month = f"{directory_name_month_python}/{old_name}{extension}"
    file_path_dcim_month = f"{directory_name_month_dcim}/{old_name}{extension}" 


    if extension == ".txt":
        if not os.path.exists(directory_name_year_text):
            os.mkdir(directory_name_year_text)
        else:
            pass

        if not os.path.exists(directory_name_month_text):
            os.mkdir(directory_name_month_text)
        else:
            pass
        os.replace(file, file_path_text_month)
    elif extension == ".py":
        if not os.path.exists(directory_name_year_python):
            os.mkdir(directory_name_year_python)
        else:
            pass

        if not os.path.exists(directory_name_month_python):
            os.mkdir(directory_name_month_python)
        else:
            pass
        os.replace(file, file_path_python_month)
    elif extension == ".jpg":
        if not os.path.exists(directory_name_year_dcim):
            os.mkdir(directory_name_year_dcim)
        else:
            pass

        if not os.path.exists(directory_name_month_dcim):
            os.mkdir(directory_name_month_dcim)
        else:
            pass
        os.replace(file, file_path_dcim_month)


