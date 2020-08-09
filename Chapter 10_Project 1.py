# Chapter 10
# Practice Project 1

# Only copy pdf files from 'd:\test\...' to new folder named 'pdfBackup'

####### A FOLDER NAMED 'pdfBackup' NEEDS TO BE CREATED UNDER 'd:\test\' FIRST #######

import os, re, shutil, pprint

os.chdir('d:\\')

def copyFile():                    
  folder = os.path.abspath('.\\test')
  for fold, sub, file in os.walk(folder):
     for files in file:
       if files.endswith('.pdf'):
          shutil.copy(os.path.join(fold,files),'.\\pdfBackup')
       continue
