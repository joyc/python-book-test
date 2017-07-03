#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete - Delete all keywords of contents.
#        py.exe mcb.pyw delete <keyword> - Delete keywords from contents.

import shelve, pyperclip, sys

# init shelve file for save data.
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Delete all clipboard content.
    elif sys.argv[1] == 'delete':
        for i in list(mcbShelf.keys()):
            del mcbShelf[i]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
# Delete clipboard <keyword> content.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2].lower() in mcbShelf.keys():
    del mcbShelf[sys.argv[2]]

mcbShelf.close()