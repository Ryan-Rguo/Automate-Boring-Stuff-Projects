# Chapter 6.7

# Practice Project

tableData = [['apples','orange','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


def printTable(table):
  maxLen = 0
  maxCob = []
  
  for i in range(len(table)):
    for v in range(len(table[i])):
      if len(table[i][v]) > maxLen:
        maxLen = len(table[i][v])
    maxCob += [maxLen]
    maxLen = 0

  for x in range(len(table[0])):
    for y in range(len(table)):
      print(table[y][x].rjust(maxCob[y]+1),end='')
    print(end='\n')
