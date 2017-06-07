# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 19:34:31 2017

@author: Shekhar
"""
import os
def file_path(folder_adress,file_name):
    file_path=folder_adress+"//"+file_name
    return file_path



folder_adress=r"C:/Users/Akhil/Desktop"
file_name_read="companies optics.txt"
path1=file_path(folder_adress,file_name_read)


with open(path1, "r") as file_handle_read:
    list1=(file_handle_read.read().split("\n"))

list2=[None]*len(list1)
for company in range(len(list1)):
    list2[company]="not applied"

    
file_name_write="test file.csv"
path2=file_path(folder_adress,file_name_write) 

with open(path2,"w") as file_handle_write:
    for i in range(len(list2)):
        file_handle_write.write(list1[i]+','+list2[i]+'\n')
        
   
folder_adress=r"C:/Users/Akhil/Desktop"
folder_name="companies"
path1=file_path(folder_adress,folder_name)
os.mkdir(path1)

   
     
        
        
    
        
    
    

    
    

  
    
    

