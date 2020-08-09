# Chapter 15
# Practice Project 3

# Brute-Force PDF Password Breaker.

import PyPDF2, os

os.chdir('d:\\a\\b\\cats')

def breakPas():
     pdfFile = open('demo_en.pdf','rb')
     pdfReader = PyPDF2.PdfFileReader(pdfFile)
     dictionary = open('dictionary.txt','r')
     passwords = dictionary.readlines()
     print('Start decrypting...')
     for i in range(len(passwords)):
          password = passwords[i].rstrip('\n')
          
          if pdfReader.decrypt(password) == 0:
               if pdfReader.decrypt(password.lower()) == 0:
                    if (i+1)%100 == 0:       # Show current status...
                         print('Tried ' + str(i+1) + ' times')
               else:
                    print('The password for the file is ' + password.lower())
                    break
 
          else:
               print('The password for the file is ' + password)
               break
     print('Done')


