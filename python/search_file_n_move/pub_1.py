'''
file name : ddp_pub_1
description : run file for ddp auto pub
purpose : publishe crvl ddp files
date : May 08, 2023
owner : [Rishi Shingare]
'''

from posting_editor import posting_editor
from search_file import search_file
from check_destination import check_destination
from file_copy import file_copy
from checks import checks
from ip_details import ip_details


#set various inputs - chnage inputs accordingly
filename,path,ip,baserc,files_path = ip_details()

#qc checks before running script
subfolder,posting_file_checks = checks(filename,path,ip,baserc,files_path ) 

if subfolder == "No" and posting_file_checks :
    
    print ("\nAll checks are passed, script is running !!!")

    #call posting editor
    posting_editor(filename,path,ip,baserc)

    #search files in source
    totalfiles = search_file(ip,files_path)

    #check if path is available or not
    check_destination(ip)

    #copy file to destination, change filename and touch 
    file_copied= file_copy(ip,files_path,path)

    #final message
    print (f"\n{file_copied} out of {totalfiles} files has been posted successfully")
    print (f"\nBelow files has been created on {path}")
    print (f"\t'file_not_found'        : Contains list of files unable to find through script")
    print (f"\t'destination_not_found' : Contains list of files which needed a template set up")
    print (f"\t'files_uploaded'        : Conatains list of files uploaded successfully")

else:
    print ("\nScript abort !!! QC checks failed.")
