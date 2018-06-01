# reverseargv.py 
# 反转并打印命令行参数
import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

print(' '.join(reversed(sys.argv[1:])))