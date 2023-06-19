'''
filename :ip_details
description : provide input paths, base output path and file name
owner : Rishi Shingare 
date : 17-May-2023
external libraries : None
'''


def ip_details ():

    #posting details file name
    filename = "posting_details.xlsx"             

    #posting datails file path
    path = "//folder1//folder2//folder3//folder4//folder5//folder6"

    #posting file details full name with path
    ip = path + "//" + filename

    #base output path for firm
    baserc = "//folder1//folder2//reports//firm_name"

    #publishing files (files need to movee) source path (available/downloaded here) 
    files_path = "//folder1//folder2//folder3//folder4//Publishing//publishing_files//"

    return (filename,path,ip,baserc,files_path)
