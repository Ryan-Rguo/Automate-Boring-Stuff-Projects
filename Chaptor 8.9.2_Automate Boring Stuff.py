# Chaptor 8.9
 
# TESTING INSTRUCTION:
# PLEASE CREATE "MadLibs_input.txt" UNDER PATH D:\ AND SAVE BELOW CONTENT:
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

# Practice Project 2

import os, re

os.chdir('d:\\')

madin = open('MadLib_input.txt', 'r')
madout = open('MadLib_output.txt','a')
content = madin.read()

print('Enter an adjective:')
adjin = input().lower()
print('Enter a noun:')
nonin = input().lower()
print('Enter a verb:')
verin = input().lower()
print('Enter another noun:')
nonin2 = input().lower()

madadj = re.compile(r'ADJECTIVE')
content = madadj.sub(str(adjin), content)

madn1 = re.compile(r'NOUN')
content = madn1.sub(str(nonin), content, 1)

madver = re.compile(r'VERB')
content = madver.sub(str(verin), content)

madn2 = re.compile(r'NOUN')
content = madn2.sub(str(nonin2), content)

print(content)

madout.write(content + '\n')

madin.close()
madout.close()

