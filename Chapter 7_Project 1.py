# Chaptor 7

# Practice Project 1
# Here are two functions that return the same result. 

import re

def pswTestLong():
  while True:
     print('Please input a password that contains at least 8 letters includs number, lowercase, and uppercase.')
     pw = input()
     num = re.compile(r'[0-9a-zA-Z]{8,}')                   # At least 8 characters
     try:
       if num.search(pw).group() != None:
          lower = re.compile(r'[a-z]')                      # At least 1 lowercase letter

          if lower.search(pw).group() != None:
             upper = re.compile(r'[A-Z]')                   # At least 1 uppercase letter

             if upper.search(pw).group() != None:
                dig = re.compile(r'[0-9]')                  # At least 1 number

                if dig.search(pw).group() != None:
                   special = re.compile(r'^((?!\W).)*$')    # No special characters

                   if special.search(pw).group() != None:
                       print('Great job, this is a strong password!')
                       break
     except:
          print('The password is invalid! Try again...')
     
    
    
def pswTestShort():
  while True:
     print('Please input a password that contains at least 8 characters includ number, lowercase, and uppercase.')
     pw = input()
     num = re.compile(r'''
          (?=.*\d)                 # At least 1 number
          (?=.*[a-z])              # At least 1 lowercase letter
          (?=.*[A-Z])              # At least 1 uppercase letter
          (?=^((?!\W).)*$)         # No special characters
          ([0-9a-zA-Z]{8,}         # At least 8 characters
          )''',re.VERBOSE)
     try:
          if num.search(pw).group() is not None:
               print('Great job, this is a strong password!')
               break
     except:
          print('The password is invalid! Try again...')
    
