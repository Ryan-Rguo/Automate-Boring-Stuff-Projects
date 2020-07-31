# Chaptor 5.6


# Practice Project 1

print('Practice Project 1')
inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

print('Inventory')

def invent(lists):
  total = 0

  for k, v in lists.items():
    
    print(str(v) + ' ' + k)
    total += v
  print('Total amount ' + str(total))
    
invent(inv)

print(end='\n') 



# Practice Project 2

print('Practice Project 2')
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
inv2 = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def add(bag, prize):

    for x in range(len(prize)):
        if prize[x] in bag:
            bag[prize[x]] += 1
        else:
            bag.setdefault(prize[x], 1)


print('Inventory')

def invent(lists):
  total = 0

  for k, v in lists.items():
    
    print(str(v) + ' ' + k)
    total += v
  print('Total amount ' + str(total))

add(inv2, loot)
invent(inv2)
             
