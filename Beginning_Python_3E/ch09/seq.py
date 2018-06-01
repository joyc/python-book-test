# 生成无穷数字序列

def check_index(key):
    """
    指定的键是否是可接受的索引？

    键必须是非负整数，才是可接受的。
    如果不是整数，将引发TypeError异常；
    如果是负数，将引发IndexError异常（因为这个序列的长度是无穷的）
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError

class ArithmeticSequence:

    def __init__(self, start=0, step=1):
        """
        初始化这个算术序列

        start   -序列中的第一个值
        step    -两个相邻值的差
        changed -一个字典，包含用户修改后的值
        """
        self.start = start                              # 存储起始值
        self.step = step                                # 存储步长值
        self.changed = {}                               # 没有任何元素被修改

    def __getitem__(self, key):
        """
        从算术序列中获取一个元素
        """
        check_index(key)

        try: return self.changed[key]                  # 修改过？
        except KeyError:                               # 如果没有修改过，
            return self.start + key * self.step        # 就计算元素的值

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        """

        check_index(key)

        self.changed[key] = value                      # 存储修改后的值


# 带访问计数器的列表
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

# 特性属性函数property举例
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    # 调用函数property并将存取方法作为参数（获取方法在前，设置方法在后）并关联给size
    size = property(get_size, set_size)


# 检查字符串的迭代生成器
nested = [[1, 2], [3, 4], [5]]

def flatten(nested):
    try:
        # 不迭代类似于字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

>>> list(flatten(['foo', ['bar', ['baz']]]))
['foo', 'bar', 'baz']
