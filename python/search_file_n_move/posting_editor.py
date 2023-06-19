'''
filename : posting_editor
description : function to edit posting details file and create rc path and append effective date in filename
owner : Rishi Shingare 
date : 08-May-2023
external libraries : pandas
'''


def posting_editor(filename,path,ip,baserc):
    import pandas as pd
        

    df = pd.read_excel(ip)                                             #Read posting detials excel
    
    fund = df["Fund"]                                                  #read fund    
    bu = df ["RC Fund or BU"]                                          #read bu
    report_type = df["Report File Type"]                               #read report type
    edate = df["Current Effective Date"]                               #read effective date  
    fdate = edate.dt.strftime('%Y%m%d')                                #format edate in YYYYMMDD
    postingfname = df["Description"]                                   #read file name
    psotingnewname = postingfname + "_" + fdate                        #append effective name in postingfname

    #check if bu and fund is same or not and then create rc path accordingly
    if fund.equals(bu):
        rcpath = baserc + "//" + fund  + "//" + report_type
    else:
        rcpath = baserc + "//" + bu  + "//" + report_type
    
    #add rc path and update file name in dataframe
    df["rc_path"] = rcpath                                     
    df["Description_updated"] = psotingnewname
    
    #export update dataframe to existing excel
    df.to_excel(ip,index = False)
    
    #return(ip,path)
