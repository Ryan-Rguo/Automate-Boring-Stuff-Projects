# Chaptor 4.10


# Practice Project 1

spam = ['apples','bananas','tofu','cats']

def list(content):
    num = ''
    for i in range(len(content)-1):
        num += str(content[i] + ', ')
    num += str('and ' + content[-1])
    return num

print(list(spam))


# Practice Project 2

grid = [['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.']]



for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i],end='')
    print(end='\n')


