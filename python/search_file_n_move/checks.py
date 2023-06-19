'''
filename : checks
description : QC checks to avoid errors while running scripts
owner : Rishi Shingare 
date : 17-May-2023
external libraries : pandas
'''


def checks(filename,path,ip,baserc,files_path ):

    import pandas as pd
    import os

    
    subfolder = ""

    dir_list = os.listdir(files_path)

    #check if file_path has subdirectory or not 
    for each in dir_list:
        if not os.path.isfile(files_path + each):
            subfolder = "Yes"
            print ((files_path + each))
            break
        else:
            subfolder = "No"


    if subfolder == "No":
        pass
    else:
        print(f"\nSub folder is available in {files_path}\nMove all file from subfolder to {files_path}\nRemove all subfolders and try again")



    #check posting details excel headers , it it has all necessory headers or not 
    posting_columns = ['Current Effective Date', 'Description', 'Report File Type', 'RC Fund or BU', 'Fund', 'Fund or BU NUMBER', 'Type', 'Frequency']

    df = pd.read_excel(ip)

    if (list(df.columns)) == posting_columns:
        posting_file_checks = True
    else:
        posting_file_checks = False

    if posting_file_checks:
        pass
    else:
        print (f"\nposting deatils file column is mismath , it should have below columns \n{posting_columns}")

    return (subfolder,posting_file_checks)
