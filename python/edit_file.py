'''
remove only pipes line i.e 2nd and 2nd last line
remove extra pipes from first and last line
move file to another folder
'''


import glob
import os
import datetime as dt

today = dt.datetime.now().date()

#get latest file
list_of_files = glob.glob('//folder1//folder2//folder3//Firm_name//folder3//Testfiles//file_name_T00001T_*')
latest_file = max(list_of_files, key=os.path.getctime)
rlia_file = open(latest_file, "r").readlines()

#get rid of 2nd and 2nd last line
rlia_file.pop(1)
rlia_file.pop(-2)

#get rid of extra pipes on first and last line
newfirst = rlia_file[0][0:-16]
rlia_file[0] = newfirst + '\n'
newlast = rlia_file[-1][0:-17]
newlast_one = newlast.replace("||","|")
rlia_file[-1] = newlast_one

#get latest file name and stamp
filetime = dt.datetime.fromtimestamp(os.path.getctime(latest_file)).date()
latest_file_split = latest_file.split('/')
latest_file_split_name = latest_file_split[len(latest_file_split)-1]

#write to new file 
if filetime == today:

    file_details = rlia_file
    new_file = open('//folder1//folder2//folder3//Firm_name//FIRM//folder4//'+ latest_file_split_name, 'w')
    for line in file_details:
        new_file.write(line)
    new_file.close()

else:
    print("File not refreshed yet")
