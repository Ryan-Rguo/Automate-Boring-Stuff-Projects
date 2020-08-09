# Chapter 10
# Practice Project 2

# Delete files with sizes over 100Mb from 'd:\test\'.

import os, pprint, send2trash

os.chdir('d:\\')

def deleteLarge():                    
   large = []
   folder = os.path.abspath('.\\test')
   for fold, sub, file in os.walk(folder):
      for files in file:
         path = os.path.join(fold,files)
         size = os.path.getsize(path)
         if size >= 100000000:
            large.append(path)        
            #send2trash.send2trash(path)     # Remove # to commence the delete.

   pprint.pprint(large)
