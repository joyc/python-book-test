def newfoo(arg1, arg2, *nkw, **kw):
    "display regular args and all variable args"
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" %(eachKW, kw[eachKW])


# newfoo('wolf', 3, 'projects', frend=90, gamble=96)
# newfoo(2, 4, *(6, 8), **{'foo': 10, 'bar': 12})

aTuple = (6, 7, 8)
aDict = {'z': 9}
newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)