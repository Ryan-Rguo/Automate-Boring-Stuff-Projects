# Chaptor 8.9

### FOR TESTING, PLEASE RENAME THIS FILE TO "mcb.pyw" AND CREATE .BAT FILE ACCORDINGLY.

#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:  save <keyword>    - Saves clipboard to keyword.
#         delete <keyword>  - Delete keyword and value from shelf.
#         <keyword>         - Loads keyword to clipboard.
#         list              - Loads all keywords to clipboard.
#         delete            - Delete all keywords from shelf.

# Practice Project 1

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
     mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
     if sys.argv[2] in mcbShelf:
          mcbShelf.pop(sys.argv[2]) 
     else:
          pyperclip.copy('Length 3, but no keyword found.')
elif len(sys.argv) == 2:

     if sys.argv[1].lower() == 'list':
          pyperclip.copy(str(list(mcbShelf.keys())))
     elif sys.argv[1] in mcbShelf:
          pyperclip.copy(mcbShelf[sys.argv[1]])
     elif sys.argv[1].lower() == 'delete':
          mcbShelf.clear() 
     else:
          pyperclip.copy('Length 2, but no command matched')
else:
     pyperclip.copy('No match')

mcbShelf.close()
