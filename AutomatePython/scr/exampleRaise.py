#! python3

import traceback
"""
**********
*        *
*        *
*        *
**********
error_log.txt
"""

def boxPoint(symbol, width, heigth):
    if len(symbol) != 1:
        try:
            raise Exception('"Symbol" needs to a string of length 1.')
        except:
            errorFile = open('error_log.txt', 'a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print('The traceback info was written error_log.txt')
    if (width < 2) or (heigth < 2):
        try:
            raise Exception('"width" and "heigth" must be greater or equal to 2.')
        except:
            errorFile = open('error_log.txt', 'a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print('The traceback info was written error_log.txt')

    print(symbol * width)

    for i in range(heigth - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)



boxPoint('**', 1, 1)

