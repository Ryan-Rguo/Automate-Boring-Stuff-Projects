# Chaptor 7.18

import re

# Practice Project 1
def test():
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
                   print('This is a strong password')
                   break
     except:
          print('Password is invalid')
     
# test()        # Remove the # to start testing.


# Practice Project 2

def rip():
 while True:         # The while loop is not necessary, just for repeat test.
  print('Please input the word you need to work on')
  x = input()
  print('Please input the letter you need to strip from the both sides')
  y = input()
  if y == '':
    y = ' '
  front = re.compile(r'^(%s)*' %y) 
  x = front.sub(r'', x)
  back = re.compile('(%s)*$' %y)
  x = back.sub(r'', x)
  print('The result is ' + x)

# rip()         # Remove the # to start testing.
