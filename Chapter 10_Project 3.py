# Chapter 10
# Practice Project 3 - 1

# Write a program that finds all files with a given prefix,
# such as spam001.txt, spam002.txt, and so on, in a single
# folder (d:\test) and locates any gaps in the numbering (such as if
# there is a spam001.txt and spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.

import os, re, shutil

os.chdir('d:\\')

def fillGap():                   
   folder = os.path.abspath('.\\test')
   num = 1
   for fold, sub, file in os.walk(folder):
     for files in file:
       a = re.search(r'^spam(0)(0)(\d).txt$',files)
       b = re.search(r'^spam(0)(\d\d).txt$',files)
       c = re.search(r'^spam(\d\d\d).txt$',files)
       if a is not None:
         if a.group(3) == num:
            num += 1
         else:
            newname = 'spam' + '00' + str(num) + '.txt'
            newpath = os.path.join(fold,newname)
            oldpath = os.path.join(fold,files)
            print('Renaming "%s" to "%s"...' %(files, newname))
            shutil.move(oldpath,newpath)
            num += 1
       elif b is not None:
          if b.group(2) == num:
            num += 1
          else:
            if len(str(num)) == 1:
               newname = 'spam' + '00' + str(num) + '.txt'
            elif len(str(num)) == 2:
               newname = 'spam' + '0' + str(num) + '.txt'
            newpath = os.path.join(fold,newname)
            oldpath = os.path.join(fold,files)
            print('Renaming "%s" to "%s"...' %(files, newname))
            shutil.move(oldpath,newpath)
            num += 1
       elif c is not None:
          if c.group(1) == num:
             num += 1
          else:
             if len(str(num)) == 1:
               newname = 'spam' + '00' + str(num) + '.txt'
             elif len(str(num)) == 2:
               newname = 'spam' + '0' + str(num) + '.txt'
             elif len(str(num)) == 3:
               newname = 'spam' + str(num) + '.txt'
             newpath = os.path.join(fold,newname)
             oldpath = os.path.join(fold,files)
             print('Renaming "%s" to "%s"...' %(files, newname))
             shutil.move(oldpath,newpath)
             num += 1


# Practice Project 3 - 2

# Addtional Challenge:
# Insert gaps into numbered files so that a new file can be added.

import os, re, shutil

os.chdir('d:\\')

def insertGaps():                   
   folder = os.path.abspath('.\\zt')
   num = 1
   for fold, sub, file in os.walk(folder):
     for files in file:
       a = re.search(r'^spam(0)(0)(\d).txt$',files)
       b = re.search(r'^spam(0)(\d\d).txt$',files)
       c = re.search(r'^spam(\d\d\d).txt$',files)
       if a is not None:
         if a.group(3) == num:
            num += 1
         elif str(num)[-1] == '9': # Insert gap for every filename ends with 9.
            num += 1
            if len(str(num)) == 1:
                newname = 'spam' + '00' + str(num) + '.txt'
            elif len(str(num)) == 2:
                newname = 'spam' + '0' + str(num) + '.txt'
            newpath = os.path.join(fold,newname)
            oldpath = os.path.join(fold,files)
            print('Renaming "%s" to "%s"...' %(files, newname))
            shutil.move(oldpath,newpath)
            num += 1
         else:
            newname = 'spam' + '00' + str(num) + '.txt'
            newpath = os.path.join(fold,newname)
            oldpath = os.path.join(fold,files)
            print('Renaming "%s" to "%s"...' %(files, newname))
            shutil.move(oldpath,newpath)
            num += 1
       elif b is not None:
            if str(num)[-1] == '9':
               num += 1
            if len(str(num)) == 1:
                newname = 'spam' + '00' + str(num) + '.txt'
            elif len(str(num)) == 2:
                newname = 'spam' + '0' + str(num) + '.txt'
            elif len(str(num)) == 3:
                newname = 'spam' + str(num) + '.txt'
            newpath = os.path.join(fold,newname)
            oldpath = os.path.join(fold,files)
            print('Renaming "%s" to "%s"...' %(files, newname))
            shutil.move(oldpath,newpath)
            num += 1
       elif c is not None:
             if str(num)[-1] == '9':
               num += 1
             if len(str(num)) == 1:
                newname = 'spam' + '00' + str(num) + '.txt'
             elif len(str(num)) == 2:
                newname = 'spam' + '0' + str(num) + '.txt'
             elif len(str(num)) == 3:
                newname = 'spam' + str(num) + '.txt'
             newpath = os.path.join(fold,newname)
             oldpath = os.path.join(fold,files)
             print('Renaming "%s" to "%s"...' %(files, newname))
             shutil.move(oldpath,newpath)
             num += 1
