# Learn Interfaces by Building an Equation Solver通过构建方程求解器学习接口

Abstract classes enable you to define formal interfaces - objects acting as blueprints for classes.

抽象类让你可以定义正式的接口 —— 一个类的蓝图，用于定义类的属性和方法。

In this project, you'll discover how to implement an interface in Python while building a simple equation solver program.

An interface is like a blueprint for a class. An interface contains a set of methods and properties that a class should implement.

接口就像是类的蓝图。一个接口包括一系列类需要执行的方法和属性

## abc.ABC 抽象基类

`ABC` stands for **Abstract Base Classes**. The `ABC` class enables you to turn a regular class into an abstract class, which is a class that acts as a blueprint for concrete classes.

“ABC” 代表抽象基类（Abstract Base Classes）。ABC 类能够将一个普通类转变为抽象类，而抽象类是一种充当具体类蓝图的类。

In order to be recognized as an abstract method, a method should be decorated with the `@abstractmethod` decorator.

使用了装饰器 `@abstractmethod` 的方法会被识别为抽象方法

A decorator is used in Python to modify the behavior of a function. Here's an example of how to use a decorator named spam:

装饰器可以修改一个函数的行为

    @spam
    def foo():
        pass

Once a class inheriting from `ABC` has an abstract method, the class cannot be instantiated anymore. 

The other error occurs because the LinearEquation class must implement all the abstract methods defined in the interface. 

An interface doesn't have to define only abstract methods, but it can also implement methods to be inherited by the concrete classes.

接口并非只能定义抽象方法，它还可以实现一些方法，供具体类继承使用。

## 类型注解

In Python, data types are recognized during runtime (when the code is executed). Therefore, you don't have to specify the data type of a variable when you declare it. Nonetheless, you can annotate a variable to clarify that it will hold a specific data type with variable: `<data type> = value` or just variable: `<data type>`. Note that the Python interpreter does not enforce the types used to annotate variables, and normally you'd need external tools to do it.

Later on, you'll use this class attribute as a part of the validation process of the arguments passed to instantiate the equation objects.

## `__init_subclass__` 魔术方法

The `__init_subclass__` method is called whenever the class that defines it is subclassed and it enables to customize the child classes. The method takes a parameter named by convention cls (standing for "class"), which represents the new child class.

当定义了`__init_subclass__`方法的类被继承时，该方法就会被调用，它能够对子类进行自定义配置。按照惯例，这个方法会接收一个名为cls（代表 “类”）的参数，该参数表示新创建的子类。

## hasattr() 内置函数

The `hasattr` built-in function takes an object as its first argument and a string representing an attribute name as its second argument. It returns a boolean indicating if the object has the specified attribute.

传入一个对象和一个字符串作为参数，返回一个布尔值，指示对象是否有指定的属性。

Each equation object will be instantiated passing as many arguments as the coefficients of the equation, starting from n-th degree of  x  down to the zero-th degree, including the possible coefficient with the value of 0.

每个方程对象在实例化时，都要传入与方程系数数量相同的参数，这些参数从 x 的 n 次项系数开始，一直到 x 的 0 次项系数（即常数项），其中也包括可能为 0 的系数。

For example, LinearEquation(4, 5) would represent the equation  `4x+5=0` , with 4 being the coefficient of the first (highest here) degree and 5 the coefficient of the zero-th degree.

## isinstance() 内置函数

`isinstance()` 是 Python 的一个内置函数，用于判断一个对象是否是某个指定类（或其子类）的实例。

The `isinstance()` built-in function takes two arguments and returns a Boolean indicating if the object passed as the first argument is an instance of the class passed as the second argument.

    isinstance(7, int) # True

## any() 内置函数

`any()` 是 Python 的内置函数，用于判断可迭代对象（如列表、元组、集合等）中是否存在至少一个为 True 的元素。

## f字符串格式控制 `:+`

在 Python 的 f 字符串中，`:+` 是一种格式化说明符，主要用于控制数字（整数、浮点数等）的正负号显示，具体作用是：

- 对于正数，会显式地加上 + 号
- 对于负数，会正常显示 - 号
- 对于零，则显示 +0（或 +0.0 等，取决于数字类型）

As you can see, the + sign is missing from the output. The number sign is displayed by default only if negative. To change this behavior, you can write a colon after the expression to be evaluated within the curly braces of your f-string, and specify the option +. This will allow you to display the sign both for positive and negative numbers.

Modify the string in your two conditional clauses by adding :+ inside the curly braces after coefficient.

![](https://cdn.freecodecamp.org/curriculum/python/linear-equation.png)

## re.sub()

The `sub` function from the `re` module enables you to replace text inside a string based on a regex pattern.

    verse = 'Always look on the bright side of life'
    spam = re.sub('bright', 'spam', verse)
    spam == 'Always look on the spam side of life' # True

It takes three arguments: the regex pattern to match, the replacement, and the string on which you want to perform the replacement.

## 正则表达式——后向环视

In a regex pattern, a lookaround is an assertion that matches a certain pattern without consuming characters in the string. One kind of lookaround is the lookbehind, which can be either positive or negative. They are denoted by (?<=...) and (?<!...), respectively.

在正则表达式模式中，环视（lookaround）是一种断言，它能匹配特定模式但不会消耗字符串中的字符。环视的一种类型是后向环视（lookbehind），它可分为肯定后向环视和否定后向环视，分别用(?<=...)和(?<!...)表示。

- 肯定后向环视(?<=...)：用于判断某个位置的前面存在与...部分匹配的内容。
- 否定后向环视(?<!...)：用于判断某个位置的前面不存在与...部分匹配的内容。

    spam = 'black back bat'
    re.sub('(?<=l)a', 'o', spam) == 'block back bat' # True
    re.sub('(?<!l)a', 'o', spam) == 'black bock bot' # True

In the example above, the pattern (?<=l)a contains a positive lookbehind, which is used to match the a character only when preceded by an l. In the last line of the example, the pattern (?<!l)a contains a negative lookbehind, which is used to match the a character only if it is not preceded by an l. Note how, in both cases, the character contained in the lookbehind is not consumed.

## 正则表达式——前向环视

Another kind of lookaround assertion is the lookahead. Positive and negative lookahead are denoted by (?=...) and (?!...), respectively. They are used to match a pattern if followed by a certain sequence of characters, which is not consumed:

另一种环视断言是前向环视（lookahead）。肯定前向环视和否定前向环视分别用(?=...)和(?!...)表示。它们用于在某个模式后跟随特定字符序列时进行匹配，且该字符序列不会被消耗（即不纳入最终匹配结果）：

- 肯定前向环视(?=...)：断言某个位置的后面存在与...匹配的内容，仅当满足此条件时，前面的模式才会被匹配。
- 否定前向环视(?!...)：断言某个位置的后面不存在与...匹配的内容，仅当满足此条件时，前面的模式才会被匹配。

    spam = 'black back bat'
    re.sub('a(?=t)', 'o', spam) == 'black back bot' # True
    re.sub('a(?!t)', 'o', spam) == 'block bock bat' # True

In the example above, the pattern a(?=t) contains a positive lookahead, which is used to match the a character only when followed by a t. In the last line of the example, the pattern a(?!t) contains a negative lookahead, which is used to match the a character only if not followed by a t. Again, in both cases, the character contained in the lookahead is not consumed.

When the second-degree coefficient is positive, the parabola has a minimum point and opens upward, or it is called concave upwards. Instead, when the second-degree coefficient is negative, the parabola has a maximum point and opens downward, or it is called concave downwards.

![](https://cdn.freecodecamp.org/curriculum/python/parabola.png)
Declare a concavity variable and assign it either the string 'upwards' or 'downwards', depending on the concavity of the parabola. Also, declare a variable named min_max and assign it either the string 'min' or 'max', depending on if the vertex is a minimum or a maximum, respectively.

## f字符串格式控制——居中对齐和左右对齐

An interesting feature of f-strings is the capability of forcing the output to be right/left-aligned, or centered. After the expression to be evaluated is inside the curly braces, you need to write a colon followed by an alignment option (< to left-align, > to right-align, ^ to center) and a number representing the width, that is the number of characters in which you want to arrange the text. For example:

f 字符串有一个有趣的特性，就是能够强制输出内容左对齐、右对齐或居中对齐。在花括号内的待计算表达式之后，需要写一个冒号`:`，后跟一个对齐选项（`<` 表示左对齐，`>` 表示右对齐，`^` 表示居中对齐），再加上一个代表宽度的数字 —— 也就是你希望文本所占的字符数量。

    f'{"Hello World":>20}'

Printing the string from the example above would result in right-aligned text arranged in a space of 20 characters.

Between the colon and the alignment option, you can specify a fill character, which will be used to fill the space around the text within the specified width.

在 `:` 和 对齐选项之间还可以设置填充字符，用来填充宽度

Add a - between the colon and the ^ in your f-string.

## f字符串格式控制——类型转换

Another feature of f-strings enables you to convert the content of the replacement field (the curly braces) into a string by using a ! followed by the conversion type s. For example, f'{obj!s}' converts obj into a string and it is equivalent to f'{str(obj)}'.

f 字符串的另一个特性是，通过使用叹号!后跟转换类型s，可以将替换字段（即花括号内的内容）转换为字符串。例如，f'{obj!s}'会将obj转换为字符串，这与f'{str(obj)}'是等价的。

## match-case选择语句

Structural pattern matching is a Python construct that enables matching a pattern with a subject value, which is specified after the match keyword:

    match value:
        case x:
            <code>
        case y:
            <code>

Each pattern is specified after the case statement. If the match is positive, the code inside the case block is run.

## f字符串格式控制——小数点后保留小数位数

f-strings also enable you to set a specific precision to your numerical data by using the `.nf` format specifier, where n is the number of decimal digits to display.

## match-case选择语句

The structural pattern matching enables you to verify that the subject has a specific structure. In addition to that, it binds names in the pattern to elements of the subject. For example:

    match my_list:
        case [a]:
            print(a)
        case [a, b]:
            print(a, b)

Note that the align option and the width should be placed between the colon and the precision format specifier.