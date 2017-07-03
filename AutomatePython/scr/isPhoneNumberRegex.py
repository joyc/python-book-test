import re

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')

phoneNumRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{4}                           # first 4 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)               # 第二个参数表示忽略正则的空格和注释

mo = phoneNumRegex.search('My number is 080-8169-8088.')
#print('Phone number found: ' + mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)