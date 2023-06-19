'''
filename : search_file
description : function to search files to post in source folder
owner : Rishi Shingare [rbs3]
date : 09-May-2023
external libraries : Pandas
'''

def search_file(ip,files_path):
    import os
    import pandas as pd

    df = pd.read_excel(ip)

    postingfname = df["Description"]
    postingfnamelist = postingfname.tolist()                     # conver filename to list
    totalfiles =  len(postingfnamelist)
    file_not_found = []
    file_found = []
    
    for root,dirs,files in os.walk (files_path):     #find files in source
        for each in postingfnamelist:
            for eachfile in files:    
                if each + "." in eachfile:
                    file_found.append(each)
                    
                    
    
    for each in postingfnamelist:                                #create list of not found
        if each not in file_found:
            file_not_found.append(each)
            #print (each)

    print (f"\nTotal files in excel : {totalfiles}")
    print (f"Files found in folder through script  : {len(file_found)}")
    print (f"Files not found in folder through script  : {len(file_not_found)}")

        
    df["file_avilable"] = df.Description.isin(file_found).astype(int).map({1:'Yes',0:'No'})
    
    df.to_excel(ip,index = False)

    return (totalfiles)
