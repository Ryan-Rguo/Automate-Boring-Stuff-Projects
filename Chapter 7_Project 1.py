# Chaptor 7

# Practice Project 1

import re

def pswTest():
  while True:
     print('Please input a password that contains at least 8 letters includs number, lowercase, and uppercase.')
     pw = input()
     num = re.compile(r'[0-9a-zA-Z]{8,}')
     try:
       if num.search(pw).group() != None:
          lower = re.compile(r'[a-z]')

          if lower.search(pw).group() != None:
             upper = re.compile(r'[A-Z]')

             if upper.search(pw).group() != None:
                dig = re.compile(r'[0-9]')

                if dig.search(pw).group() != None:
                   print('Great job, this is a strong password!')
                   break
     except:
          print('The password is too weak! Try again...')
     
pswTest()        # Remove the # to start testing.

