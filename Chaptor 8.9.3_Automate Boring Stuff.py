# Chaptor 8.9


# Practice Project 3

import os, re, pprint

os.chdir('d:\\')   # REDIRECT TO YOUR OWN PRACTICE FILE PATH.

out = open('cb_file.txt','w')

#def namel():
al = os.listdir(os.getcwd())
res = []
for i in range(len(al)):
     match = re.compile(r'.*.txt$')
     mo = match.search(al[i])
     if mo is not None:
          txtl = al[i]               
          file = open(txtl)
          con = file.readlines()
          for v in range(len(con)):
                    mat = re.compile('cb')
                    m = mat.search(con[v])
                    if m is not None:
                             new = con[v].rstrip('\n')
                             res += [new]
pprint.pprint(res)
                    
out.write(pprint.pformat(res))
out.close()
