'''
filename : check_destination
description : check if destination path is available or not
owner : Rishi Shingare [rbs3]
date : 10-May-2023
external libraries : None
'''

def check_destination(ip):
    import pandas as pd
    import os

    df = pd.read_excel(ip)                             #open excel
    
    destination = df["rc_path"]                        #get destination path
    disti_list = destination.tolist()                  #conver it to list    
    valid_desti = []
    invalid_desti = []

    for each in disti_list:
        if os.path.exists(each):                       #check if path is available or not
            valid_desti.append(each)
            
        else:
            invalid_desti.append(each)
            
    print (f"\nTotal destinations as per excel : {len(disti_list)}")
    print (f"Valid destinations [Report Templates created ]  : {len(valid_desti)}")
    print (f"Invalide Destinations [Report Templates NOT created ]  : {len(invalid_desti)}")
    
    #map if path is available or not [i.e. report template is created or not]
    df["desitionation_path_available"] = df.rc_path.isin(valid_desti).astype(int).map({1:'Yes',0:'No'})
    df.to_excel(ip,index = False)

    #return (valid_desti,invalid_desti)
