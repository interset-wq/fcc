# review

## 字符串

### 字符串下标

字符串可以像列表一样通过下标取值


```python
my_str = "hello world"
print(my_str[0]) # h
```

### 字符串切片

通过 `string[start:stop:step]` 的写法对字符串切片。左闭右开区间，step默认值是1，写法很灵活，start,stop,step三者都可以省略，但是至少要有一个 `:`


```python
my_string = 'camperbot'
print(my_string[0:6]) # camper
print(my_string[0:6:3]) # cp
print(my_string[:]) # camperbot
print(my_string[::-1]) # tobrepmac
```

### 字符串方法

- `.find(char)` 传入一个字符 `char`，返回这个字符的下标。如果这个字符不在字符串中，返回 `-1`
- `.index(substring)` 类似于 `.find()`，在字符串中没有找到 `substring` 抛出异常 `ValueError`
- `.lower()` 返回原字符串的小写形式
- `.isalpha()` 判断字符是否全都是英文字母，返回布尔值


```python
my_str = "hello world"
print(my_str.isalpha()) # False

print(my_str.find('e')) # 1
print(my_str.find('he')) # 0
print(my_str.find('z')) # -1

print(my_str.index('e')) # 1
print(my_str.index('he')) # 0
print(my_str.index('z')) # 抛出异常ValueError
```

- 类方法 `str.maketrans()` 传入字典，定义一个替换字典。也可对字符串对象使用，作用效果和对 `str` 完全相同。这个方法需要配合`.translate()`使用
- `.translate()` 传入`str.maketrans()`返回的替换字典，在字符串中用字典的值去替换键的字符，全部替换


```python
my_string = "tamperlot"
translation_table = str.maketrans({'t': 'c', 'l': 'b'})
translated_string = my_string.translate(translation_table)
print(my_string, translated_string)
```

- `.join()` 方法 传入元素为字符串的列表，将其连接为一个字符串


```python
my_list = ['html', 'css', 'javascript']
my_str = ', '.join(my_list)
print(my_str) # html, css, javascript
```

- `.isupper()` 判断字符串中字母是否全大写


```python
my_str1 = 'ABC'
my_str2 = 'Abc'
print(my_str1.isupper()) # True
print(my_str2.isupper()) # False
```

- `.strip()` 删除字符串左右两侧特定字符


```python
my_str = '_abc_'
new_str = my_str.strip('_')
print(new_str) # abc
```

### f字符串格式控制

f字符串中的变量可以通过 `:` 进行格式控制

- `+` 显示正负号，0显示为正号


```python
num = 6
my_str = f'the num is {num:+}'
print(my_str) # the num is +6
```

- `<n` 左对齐，`^n` 居中对齐，`>n` 右对齐。用数字替换 `n`，n表示字符串的长度，在 `<` `^` `>` 之前还可以添加填充占位符，默认是空格


```python
my_str1 = f'{"Hello World":-^20}'
my_str2 = f'{"Hello World":^20}'
print(my_str1)
print(my_str2)

# ----Hello World-----
#     Hello World   
```

- `!s` 前面不需要`:`，将其他数据类型转换为字符串


```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"
    
my_dog = Dog('cool', 3)
my_str = f'this is {my_dog!s}' # 相当于 
# my_str = f'this is {str(my_dog)}'
print(my_str) # this is Dog(name=cool, age=3)
```

- `.nf` 控制保留几位小数


```python
num = 3
my_str = f'this num is {num:.5f}'
print(my_str) # this num is 3.00000
```

    this num is 3.00000
    

## 内置函数

- `print()` 打印，可以传入多个参数，使用逗号分隔
- `len()` 返回字符串、列表等的长度
- `type()` 返回数据类型
- `int()` 将数据类型转换为整数
- `list()` 将数据类型转换为列表，对字典使用时，返回键列表
- `range(start, stop, step)` 生成迭代器，左闭右开区间，常用于for循环。如果循环变量在循环体中用不到，可以使用 `_` 表示循环变量
- `abs()` 返回一个数字的绝对值
- `sum()` 计算所有元素的和
- `max()` 返回列表中的最大值
- `min()` 返回最小值


```python
my_str = "hello world"
print(my_str, len(my_str), type(my_str), sep=', ') # hello world, 11, <class 'str'>
```

- `all()` 传入可迭代对象，返回布尔值。只有可迭代对象所有元素都是True时，才返回True。可以配合列表推导式使用，但是一般使用生成器表达式generator expression（把列表推导式的 `[]` 换成 `()`），这时可以只用一层括号
- `any()` 用于判断可迭代对象（如列表、元组、集合等）中是否存在至少一个为 True 的元素。


```python
numbers = [3, 5, 7, 9, 11]
result = all(x > 0 for x in numbers)
print(result)  # True
```

- `enumerate()` 用于for循环，同时遍历列表的下标和元素


```python
iterable = ['a', 'b', 'c']
for i, j in enumerate(iterable):
    print(i, j)

# 0 a
# 1 b
# 2 c
```

## 列表

### 列表方法

- `.append(elem)` 在列表末尾追加元素
- `.insert(index, elem)` 通过下标插入元素
- `.pop(index)` 使用下标删除元素，不传入下标时删除末尾的元素，返回删除的元素


```python
my_list = ['html', 'css', 'javascript']
my_list.append('python')
print(my_list) # ['html', 'css', 'javascript', 'python']
my_list.insert(1, 'c')
print(my_list) # ['html', 'c', 'css', 'javascript', 'python']
elem1 = my_list.pop()
print(my_list, elem1) # ['html', 'c', 'css', 'javascript'] python
elem2 = my_list.pop(0)
print(my_list, elem2) # ['c', 'css', 'javascript'] html
```

- `.extend()` 传入一个可迭代对象，将这个对象的所有元素追加到列表末尾


```python
my_list = ['larch', 'birch']
tree_list = ['fir', 'redwood', 'pine']
my_list.extend(tree_list)
print(my_list) # ['larch', 'birch', 'fir', 'redwood', 'pine']
```

- `remove()` 移除第一个匹配到的元素


```python
my_list = ['larch', 1, True, 1]
my_list.remove(1)
print(my_list) # ['larch', True, 1]
```

### 列表推导式List Comprehension

适用于列表、字符串、元组。

#### 普通的列表推导式


```python
my_list = [1, 2, 3]
spam = [i * 2 for i in my_list]
print(spam) # [2, 4, 6]
```

#### 单条件的列表推导式

满足条件的元素才执行


```python
my_list = [-1, 2, 3]
spam = [i * 2 for i in my_list if i > 0]
print(spam) # [4, 6]
```

#### 双条件的列表推导式


```python
my_list = [-2, -1, 2, 3]
spam = [i * 2 if i > 0 else -1 for i in my_list]
print(spam) # [-1, -1, 4, 6]
```

### 元组

使用元组可以同时为多个遍历赋值


```python
spam = ('lemon', 'curry')
item1, item2 = spam
print(item1, item2) # lemon curry
```

## lambda表达式

lambda表达式是一种匿名函数，适用于简单、一次性的场合。

语法 `lambda x: expr`

- `x` 函数表达式 `expr` 中需要用到的参数
- `expr` 函数表达式，并作为返回值

lambda表达式还经常用在`map()`函数和`filter()`函数中

### map()函数

map()函数需要传入一个函数（常用lambda表达式）和一个可迭代对象（列表等），返回map对象。

map()作用效果和列表推导式相同


```python
new_list = map(lambda x: x * 2, [1, 2, 3])
print(new_list) # <map object at 0x000001CEFF6E6E90>
print(list(new_list)) # [2, 4, 6]
```

### filter()函数

filter()函数需要传入一个函数和一个可迭代对象。通过传入的函数从可迭代对象中筛选，返回filter对象

filter()函数也可以通过列表推导式实现


```python
my_list = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x > 2, my_list)
print(new_list) # <filter object at 0x000001CEFF7262F0>
print(list(new_list)) # [3, 4, 5]
```

## raise语句主动抛出异常

`raise ValueError("Invalid value")`

## is关键字

`is` 关键字用于检查对象的标识（身份）。它被用来判断两个变量是否指向内存中的同一个对象。

与 `is` 不同，相等运算符（`==`）用于判断两个对象的值是否相同，而不考虑它们在内存中是否是同一个对象。

## 标准库string

存储了一些字符串常量

- `string.ascii_lowercase` 小写英文字母


```python
import string

print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
```

## 标准库random和secrets

二者用法相同，只是secrets生成的随机数比random更安全

- `random.random()` 返回0到1之间的随机小数，左闭右开区间
- `random.choice()` 传入一个序列，随机返回序列中的一个元素


```python
import random, secrets

my_list = [1, 2, 3]
print(random.random()) # 0.11336019783894691
print(random.choice(my_list), secrets.choice(my_list)) # 3 2
```

## 标准库re

正则表达式

- `+` 一次或多次
- `[]` 其中之一
- `-` 范围
- `^` 否定
- `.` 单个任意字符
- `\` 转义字符
- r字符串 禁用转义字符，可以和f字符串一起使用，rf或fr字符串
- `\d` `[0-9]`
- `\D` `[^0-9]`
- `\w` `[a-zA-Z0-9_]`
- `\W` `[^a-zA-Z0-9_]`

### 函数和方法

- `findall`
- `search`
- `sub` 替换

### 后向环视

在正则表达式模式中，环视（lookaround）是一种断言，它能匹配特定模式但不会消耗字符串中的字符。环视的一种类型是后向环视（lookbehind），它可分为肯定后向环视和否定后向环视，分别用(?<=...)和(?<!...)表示。

- 肯定后向环视(?<=...)：用于判断某个位置的前面存在与...部分匹配的内容。
- 否定后向环视(?<!...)：用于判断某个位置的前面不存在与...部分匹配的内容。


```python
import re
spam = 'black back bat'
re.sub('(?<=l)a', 'o', spam) == 'block back bat' # True
re.sub('(?<!l)a', 'o', spam) == 'black bock bot' # True
```

### 前向环视

另一种环视断言是前向环视（lookahead）。肯定前向环视和否定前向环视分别用(?=...)和(?!...)表示。它们用于在某个模式后跟随特定字符序列时进行匹配，且该字符序列不会被消耗（即不纳入最终匹配结果）：

- 肯定前向环视(?=...)：断言某个位置的后面存在与...匹配的内容，仅当满足此条件时，前面的模式才会被匹配。
- 否定前向环视(?!...)：断言某个位置的后面不存在与...匹配的内容，仅当满足此条件时，前面的模式才会被匹配。


```python
spam = 'black back bat'
re.sub('a(?=t)', 'o', spam) == 'black back bot' # True
re.sub('a(?!t)', 'o', spam) == 'block bock bat' # True
```

## 特殊值

- `float('inf')` 是一个特殊值，表示正无穷大

## 字典

### 字典推导式dictionary comprehension

- 普通的字典推导式 `{key: val for key in dict}`
- 单条件字典推导式 `{key: val_1 for key in dict if condition}`
- 双条件的字典推导式 `{key: val_1 if condition else val_2 for key in dict}`


```python
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)
# 输出: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

long_words = {word: len(word) for word in words if len(word) > 5}
print(long_words)
# 输出: {'banana': 6, 'cherry': 6}
```

### 字典方法

- `.values()` 常用于for循环，用于遍历字典的值
- `.items()` 常用于for循环，同时遍历字典的键和值

### del语句

通过键删除某个键值对


```python
my_dict = {
    'name': 'Michael',
    'occupation': 'Lumberjack'
}

del my_dict['occupation']
print(my_dict) # {'name': 'Michael'}
```

## 三目运算符

if-else语句的简介写法

语法 `val_1 if condition else val_2`


```python
num = -10
abs_num = num if num >= 0 else -num
print(abs_num) # 10
```

## 递归recursion

常用于解决数学问题


```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))  # 1
print(factorial(5))  # 120  
```

## 海象运算符

使用某个表达式的值为某个变量赋值

语法 `name := val`


```python
# num = int(input("请输入一个数字："))
# if num > 10:
#     print(num)

if (num := int(input("请输入一个数字："))) > 10:
    print(num)
```

## try-except语句

    try:
        <code>
    except:
        <code>

## 面向对象编程

### OOP相关的内置函数

- `vars(obj)` 返回对象的属性字典，与 `.__dict__` 魔术属性相同
- `getattr(obj, attr)` 传入对象和属性名，返回这个属性名对应的属性值
- `hasattr()` 传入一个对象和一个字符串作为参数，返回一个布尔值，判断对象是否有指定的属性。
- `isinstance()` 返回布尔值，用于判断一个对象是否是某个指定类（或其子类）的实例。

### 魔术方法

函数或方法中禁用位置参数，强制使用关键字参数：定义函数时，第一个参数设置为 `*`。定义方法时，`self`参数之后的一个参数设置为 `*`

在 Python 中，`NotImplemented` 是一个特殊的单例对象（singleton），用于表示某个操作在当前上下文下无法实现，通常在自定义魔术方法（如算术运算、比较运算相关方法）中作为返回值使用。

- `__init__()` 构造方法
    - `super()` 子类使用 `super().__init__()`
- `__str__()` 调用 `print()` 和 `str()` 时的字符串
- `__repr__()` 调用 `repr()` 时的字符串，没有定义 `.__str__()` 时，充当 `__str__()` 的作用，一般优先定义 `.__repr__()` 再定义 `__str__()`
- `__getattribute__()`
- `__getattr__()`
- `__add__()` 加法运算
- `__sub__()` 减法运算
- `__mul__()` 乘法运算
- `__eq__()` 比较运算：相等
- `__ne__()` 比较运算：不等于
- `__lt__()` 比较运算：小于
- `__gt__()` 比较运算：大于
- `__le__()` 比较运算：小于等于
- `__ge__()` 比较运算：大于等于
- `__init_subclass__` 当定义了`__init_subclass__`方法的类被继承时，该方法就会被调用，它能够对子类进行自定义配置。按照惯例，这个方法会接收一个名为cls（代表 “类”）的参数，该参数表示新创建的子类。


### 魔术属性

- `.__dict__` 返回对象的属性字典
- `.__class__.__name__` 返回类名
- `.__class__` 获取对象所属的类

### 接口interface

通过抽象类可以定义接口

导入抽象基类和装饰器 `from abc import ABC, abstractmethod`

抽象类必须要继承 `ABC` 类，抽象方法要使用装饰器`@abstractmethod`

## match-case选择语句

### 普通写法

    match value:
        case x:
            <code>
        case y:
            <code>

### 使用变量的写法

    match my_list:
        case [a]:
            print(a)
        case [a, b]:
            print(a, b)
