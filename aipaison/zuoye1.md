现在已经学习了Python安装内置数据结构、控制流、函数等内容。给大家留5道题作为作业吧。

1. 乘法口诀表.
要求：编写一个程序，执行时输出乘法口诀表:
```
❯ python 1.py
1*1=1	
1*2=2	2*2=4	
1*3=3	2*3=6	3*3=9	
1*4=4	2*4=8	3*4=12	4*4=16	
1*5=5	2*5=10	3*5=15	4*5=20	5*5=25	
1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36	
1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49	
1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64	
1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81
```
提示：print默认输出后会换行，可以通过print参数控制是否换行。

2. 列表去重
要求：

编写一个函数，可以去除一个列表中重复的元素，并且保持元素的顺序：
```
In  : l = [1, 3, 6, 9, 3, 4, 1, 3]                                                                             
In  : unique(l)
Out: [1, 3, 6, 9, 4]
```
提示：集合、Python3.6内置支持、列表解析（还没讲）、yield（还没讲）

3. 列表排序
现在有2个列表：
```
In : A = [1, 3, 7, 10, 5, 2]

In : B = [2, 3, 5]
```
B 是 A 的子集，但顺序是乱的，编写一个函数用 A 中的元素顺序对 B 排序:
```
In  : my_sort(A, B)
Out: [3, 5, 2]
```
提示：使用列表自带的方法，enumerate

4. FIZZBUZZ
遍历并打印1到20，如果数字能被3整除，显示Fizz；如果数字能被5整除，显示Buzz；如果能同时被3和5整除，就显示FizzBuzz：
```
❯ python 4.py
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
```
5. 编写过滤1-100中的素数的函数
提示：使用filter

---
答案：

1. 乘法口诀表
```
for m in range(1, 10):
    for n in range(1, m+1):
       print('{}*{}={}'.format(n, m, m * n), end='\t')
    print()
```
主要考察了for循环和print的end参数，默认的end参数的值是'\n'表示换行，而这个需求里面m值相同时不要换行，所以需要修改end参数的值不让它换行。

列表去重
列表去重最基本版：
```
def unique(items):
    seen = set()
    rs = []
    for i in items:
        if i not in seen:
            rs.append(i)
            seen.add(i)
    return rs
```
使用了for喜欢和集合。但是这样内容太长了，改良版本：
```
def unique1(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]
```
这里面涉及了列表解析

也可以使用yield:
```
def unique2(items):
    seen = set()
    for i in items:
        if i not in seen:
            yield i
            seen.add(i)
assert list(unique2(l)) == [1, 3, 6, 9, 4]
```
最后是终极解决方案。课程里面说了，Python3.6之后可以记录插入字典的键值对顺序，所以可以这么写：
```
def unique3(items):
    return list(dict.fromkeys(items))
```
列表排序

我记得之前知乎看到过这个问题，找不到原贴了。基础版本是：
```
def my_sort(a, b):
    rs = []
    for i in a:
        if i in b:
            rs.append(i)
    return rs
```    
也可以使用enumerate和字典：
```
def my_sort1(a, b):
    index_map = {
        k: i
        for i, k in enumerate(a)
    }
    return sorted(b, key=lambda x: index_map[x])
```
终极答案是：
```
def my_sort2(a, b):
    return sorted(b, key=a.index)
```

FIZZBUZZ

主要考验if的用法：
```
def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    return str(n)

print(' '.join(fizzbuzz(n) for n in range(1, 21)))
```
注意最后可以不用写else，直接return str(n)

编写过滤1-100中的素数的函数

基本答案是：
```
def is_prime(n):
    if n == 1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2, n):
            if not n % x:
                return False
        return True


print(list(filter(is_prime, range(1, 101))))
```
这里有个问题，2的倍数肯定不是素数，上面的函数可以改成：
```
def is_prime(n):
    if n == 1:
        return False
    elif n==2:
        return True
    else:
        for i in range(3, int(math.sqrt(n)+1), 2):
            if not n % i:
                return False
        return True
```
最后。一开始留作业时我提示了加缓存，抱歉误导大家了 😢 缓存这个下次作业我在想个好的题目