"""
For Copying and Renaming images in the dataset
to one single directory for simplicity....
"""
import os
import shutil
import pandas as pd
lst_files = []
for dir_name,sub_dir_list, file_list in os.walk('MURA-v1.1/valid/XR_WRIST/'):         #For all body parts in train & valid sets
    for file_name in file_list:
        if ".png" in file_name.lower():
            lst_files.append(os.path.join(dir_name, file_name))
for i in range (len(lst_files)):
    a, b, c = lst_files[i].split('\\')[0], lst_files[i].split('\\')[1], lst_files[i].split('\\')[2]
    lst_files[i] = a + '/' + b + '/' + c
    id, bin, img = lst_files[i].split('/')[-3], lst_files[i].split('/')[-2], lst_files[i].split('/')[-1]
    src = lst_files[i]
    dest = '/home/Addy/Desktop/MURA-v1.1/valid/WRIST/'
    #os.chdir(dest)
    stt=id+"_"+bin+"_"+img
    shutil.copy(src,dest)
    shutil.move(dest+c,dest+stt)
    #os.rename(img, stt)
