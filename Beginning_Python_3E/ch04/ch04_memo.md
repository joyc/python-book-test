# 字典的用法

- 将字符串格式设置功能用于字典：要对字典执行字符串格式设置操作，不能使用format和命名参数，而必须使用`format_map`。

### 列表和字典的成员资格检查区别：
表达式`k in d`（d是字典）查找的是字典的键而不是值，而表达式`v in l`（l是列表）查找的是列表的值而不是索引。因此
相比于检查列表是否包含指定的值，检查字典是否包含指定的键的效率更高。
**数据结构越大，效率差距就越大**。

- `setdefault`用于获取与指定键相关联的值,如不存在则添加指定的键-值对。但是如果要给整个字典的全局设置默认值，可以使用模块collections中的defaultdict类。
- 如希望方法`popitem`以可预测的顺序弹出字典项，可用模块collections中的OrderedDict类
- 要按字母表排序，可先转换为小写。为此，可将sort或sorted的key参数设置为str.lower。例如，sorted("aBc", key=str.lower)返回['a', 'B', 'c']
- eval是一个类似于exec的内置函数。exec执行一系列Python语句，而eval计算用字符串表示的Python表达式的值，并返回结果（exec什么都不返回，因为它本身是条语句）。与exec一样，也可向eval提供一个命名空间。
- 函数exec将字符串作为代码执行。调用函数exec时只给它提供一个参数绝非好事。在大多数情况下，还应向它传递一个命名空间——用于放置变量的地方；否则代码将污染你的命名空间，即修改你的变量。
- 实际上，可向exec提供两个命名空间：一个全局的和一个局部的。提供的全局命名空间必须是字典，而提供的局部命名空间可以是任何映射。这一点也适用于eval。
- 