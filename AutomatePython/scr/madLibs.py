#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create txt file.
textFile = open('C:\\Python\\MyScripts\\madlibs.txt', 'w')
textFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was\
unaffected by these events.')
textFile.close()

# open and read the txt file.
with open('C:\\Python\\MyScripts\\madlibs.txt') as f:
    text = f.read()

adjective = input('Enter an adjective:\n')
text = text.replace('ADJECTIVE', adjective, 1)

noun = input('Enter an noun:\n')
text = text.replace('NOUN', noun, 1)

verb = input('Enter an VERB:\n')
text = text.replace('VERB', verb, 1)

noun = input('Enter an noun:\n')
text = text.replace('NOUN', noun, 1)

print(text, end='')

with open('C:\\Python\\MyScripts\\madlibs.txt', 'w') as f:
    print(text, file=f, end='')