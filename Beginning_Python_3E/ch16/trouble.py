import halts, sys

name = sys.argv[1]
if halts.check(name, name):
    while True: pass
