# Chapter 5

# Practice Project 1

inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def lists(bag):
     total = 0
     for k, v in bag.items():
          print(str(v) + ' ' + k)
          total += v
     print('Total amount ' + str(total))



             
