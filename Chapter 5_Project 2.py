# Chapter 5

# Practice Project 2

inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']


def add(bag, prize):

     for x in range(len(prize)):
          if prize[x] in bag:
               bag[prize[x]] += 1
          else:
               bag.setdefault(prize[x], 1)
     print(bag)


def lists(bag):
     total = 0
     for k, v in bag.items():
          print(str(v) + ' ' + k)
          total += v
     print('Total amount ' + str(total))

