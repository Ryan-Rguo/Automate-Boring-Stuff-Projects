# Chapter 7

# Practice Project 2

import re

def rip():
  #while True:         # The while loop is unnecessary, just for repeat test.
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
