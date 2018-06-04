# yield函数代表生成器，方便从上次调用的地方继续调用
# 生成器lines在文件末尾添加一个空行。
def lines(file):
    for line in file: 
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []