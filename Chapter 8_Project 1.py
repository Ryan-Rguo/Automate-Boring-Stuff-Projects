# Chapter 8
# Practice Project 1

# Sandwich Maker

import pyinputplus as pyip

breadMenu = {'wheat': 1.1, 'white': 1.2, 'sourdough': 1.3}
proteinMenu = {'chicken': 2.1, 'turkey': 2.2, 'ham': 2.3, 'tofu': 2.4}
cheeseMenu = {'cheddar': 3.1, 'Swiss': 3.2, 'mozzarella': 3.3}
otherMenu = {'mayo': 4.1, 'mustard': 4.2, 'lettuce': 4.3, 'tomato': 4.4}

def sandwichMaker():
    priceList = dict(breadMenu, **proteinMenu, **cheeseMenu, **otherMenu)
    orderItems = []

    print('Here is a process of making a sandwich.\n')

    orderItems.append(pyip.inputMenu(list(breadMenu.keys()),'1.Please choose your bread from below:\n'))

    orderItems.append(pyip.inputMenu(list(proteinMenu.keys()),'2.Please choose your protein:\n'))

    addCheese = pyip.inputYesNo('3.Do you want to add some cheese? (Yes/No)\n')
    if addCheese.lower() == 'yes':
        orderItems.append(pyip.inputMenu(list(cheeseMenu.keys()),'Please choose your cheese:\n'))

    addExtra = pyip.inputYesNo('4.Do you want something extra, like %s ? Yes/No\n' % list(otherMenu.keys()))
    if addExtra.lower() == 'yes':
        adds = list(otherMenu.keys())
        for i in range(len(otherMenu.keys())):
            if i == len(otherMenu.keys()) - 1:
                print('Do you want to add the ' + adds[0] + ' as well? Yes/No')
                if pyip.inputYesNo().lower() == 'yes':
                    orderItems.append(adds[0])
            else:
                extraInput = pyip.inputMenu(adds, 'Please choose your extras below, or just leave blank if that is enough.\n', blank=True)
                if extraInput == '':
                    break
                else:
                    orderItems.append(extraInput)
                    adds.remove(extraInput)

    orderAmount = pyip.inputInt('The amount of the sandwiches with above combination is: ',greaterThan=0,lessThan=100)

    print('\n' + ' ORDER DETAILS '.center(30,'-') + '\n')
    totalPrice = 0
    for i in range(len(orderItems)):
        itemPrice = priceList[orderItems[i]]
        print((str(i + 1) + '. ' + orderItems[i]).ljust(20,' ') + ('$%s' % format(priceList[orderItems[i]],'.2f')).rjust(10,' '))
        totalPrice += itemPrice
    print(''.rjust(30,'-'))
    print('Subtotal amount'.ljust(20) + ('$%s' % format(totalPrice,'.2f')).rjust(10))
    print(''.rjust(30,'='))
    print('Amount of Sand.'.ljust(20) + str(orderAmount).rjust(10))
    print('Total Amount'.ljust(20) + ('$%s' % format(totalPrice * orderAmount, '.2f')).rjust(10))

sandwichMaker()
