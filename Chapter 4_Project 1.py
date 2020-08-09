# Chapter 4

# Practice Project 1

spam = ['apples','bananas','tofu','cats']

def list(content):
    num = ''
    for i in range(len(content)-1):
        num += str(content[i] + ', ')
    num += str('and ' + content[-1])
    return num

