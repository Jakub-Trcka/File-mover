import os
from datetime import datetime
from pathlib import Path

def name(directory, file, format, e, n):
    

    if e == format:
        
        date = n.split("_")[1]

        year = date[0:4]
        month = date[4:6]


        directory_n_year = Path(str(directory) + "/" + str(year))
        directory_n_month = Path(str(directory_n_year) + "/" + str(month))
        file_path_year = f"{directory_n_year}/{n}{e}"
        file_path_month = f"{directory_n_month}/{n}{e}" 




        
        if not os.path.exists(file_path_year):
            os.mkdir(file_path_year)

        if not os.path.exists(file_path_month):
            os.mkdir(file_path_month)

        os.replace(file, file_path_month)

    
def now(directory, file, format, e, n):
    

    if e == format:
        now = datetime.now()
        current_time = now.strftime("%D")
        month = current_time.split('/')[0]
        year = '20' + current_time.split('/')[2]

        

        directory_n_year = Path(str(directory) + "/" + str(year))
        directory_n_month = Path(str(directory_n_year) + "/" + str(month))
        file_path_year = f"{directory_n_year}/{n}{e}"
        file_path_month = f"{directory_n_month}/{n}{e}" 



    
        if not os.path.exists(directory_n_year):
            os.mkdir(directory_n_year)

        if not os.path.exists(directory_n_month):
            os.mkdir(directory_n_month)

        os.replace(file, file_path_month)




def NoMatterSuffix(directory, file, full_name):

    now = datetime.now()
    current_time = now.strftime("%D")
    month = current_time.split('/')[0]
    year = '20' + current_time.split('/')[2]

    

    directory_n_year = Path(str(directory) + "/" + str(year))
    directory_n_month = Path(str(directory_n_year) + "/" + str(month))
    file_path_year = f"{directory_n_year}/{full_name}"
    file_path_month = f"{directory_n_month}/{full_name}" 




    if not os.path.exists(directory_n_year):
        os.mkdir(directory_n_year)

    if not os.path.exists(directory_n_month):
        os.mkdir(directory_n_month)

    os.replace(file, file_path_month)








def create_folder(directory):
    if not os.path.exists(directory):
            os.mkdir(directory)









def CreateName(path, format, file, e, n):
    create_folder(path)
    name(path, file, format, e, n)


def CreateNow(path, format, file, e, n):
    create_folder(path)
    now(path, file, format, e, n)

def CreateNoMatterSuffix(path, file, full_name):
    create_folder(path)
    NoMatterSuffix(path, file, full_name)
