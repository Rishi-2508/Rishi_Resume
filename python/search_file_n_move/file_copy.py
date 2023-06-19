'''
filename : file_copy
description : function to copy files from source to destination folder,append date in filename and retouch
owner : Rishi Shingare [rbs3]
date : 11-May-2023
external libraries : Pandas
'''

def file_copy(ip,files_path,path):

    import pandas as pd
    import shutil
    import os

    #pd.options.mode.chained_assignment = None                 #worning tunned off

    df = pd.read_excel(ip)                                    #read posting details excel      
    
    #filtered on file and destination path avialable 
    df_working = df.loc[(df['file_avilable']=='Yes')&(df['desitionation_path_available']=='Yes')].copy()
    
    finalpostingfname = df_working["Description"]
    finalpostingfnamelist = finalpostingfname.tolist()
    file_source = []
    file_name = []
    
    file_copied = 0
    file_renamed = 0
    
    #find only matching files in source again to get full path and filename with extemtion
    for root,dirs,files in os.walk (files_path):   
        for each in finalpostingfnamelist:
            for eachfile in files:
                if each + "." in eachfile:
                    file_source.append(root + '//' + eachfile)
                    file_name.append(eachfile)
                    

    #append source and file name to filtered framework
    df_working["file_source"] = file_source
    df_working["file_name"] = file_name
    
    #export filterd frame work to excel
    df_working.to_excel(path + '//files_uploaded.xlsx',index = False)
    
    #loop through filtered framework
    for index, row in df_working.iterrows():
        #prod
        shutil.copyfile(row["file_source"],row["rc_path"] + "//"+ row["file_name"])
        file_copied += 1
        extn = os.path.splitext(row["file_name"])[1]                                             #find extention
        #prod
        os.rename(row["rc_path"] + "//"+ row["file_name"],row["rc_path"]  + "//"+row['Description_updated']+extn)
        file_renamed  += 1

        
    print (f"\nFiles copied from Source to destination : {file_copied}")
    print (f"Files renamed with proper date format on destination : {file_renamed}")

    #filtered on file not found
    df_filenot = df.loc[(df['file_avilable']=='No')].copy()
    #filtered on destination not available
    df_destnot = df.loc[(df['desitionation_path_available']=='No')].copy()

    #export file not found to excel
    df_filenot.to_excel(path + '//file_not_found.xlsx',index = False)
    #export destination  not found to excel
    df_destnot.to_excel(path + '//destination_not_found.xlsx',index = False)

    return (file_copied)
    
