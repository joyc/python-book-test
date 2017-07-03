import re
# "|"|称为“ 管道”。希望匹配许多表达式中的一个时， 就可以使用它
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))

# "?"表明它前面的分组在这个模式中是可选的
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 418-4566-5777')
print(mo1.group())
mo2 = phoneRegex.search('My numer is 2566-8788')
print(mo2.group())

# "*" *意味着“ 匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())


# "+（加号） 则意味着“ 匹配一次或多次,加号前面的分组必须“ 至少出现一次”
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventyres of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)