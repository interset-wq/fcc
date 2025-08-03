# Learn Regular Expressions by Building a Password Generator 通过创建密码生成器学习正则表达式

A Python module is a file that contains a set of statements and definitions that you can use in your code.

In this project, you'll learn how to import modules from the Python standard library. You'll also learn how to use Regular Expressions by building your own password generator program.

## 内置函数 all()

在 Python 中，内置函数 `all()` 用于判断可迭代对象（如列表、元组、集合、字符串等）中的所有元素是否都为真。如果所有元素都为真，返回 `True` ；否则返回 `False` 。若可迭代对象为空，也返回 `True` 。

Instead of using a loop and a counter variable, you can achieve the same result with a different approach, which you are going to implement in the next few steps.

all() is a built-in Python function that returns True if all the elements inside a given **iterable** evaluate to `True` . Otherwise, it returns `False` .

Having `all([expression for i in iterable])`, means that a new list is created by evaluating expression for each i in iterable. After the `all()` function iterates over the newly created list, the list is deleted automatically, since it is no longer needed.

Memory can be saved by using a generator expression. Generator expressions follow the syntax of list comprehensions but they use parentheses instead of square brackets.

Change your list comprehension into a generator expression by removing the square brackets.

当使用 `all([expression for i in iterable])` 时，这意味着会通过为可迭代对象中的每个i求值expression来创建一个新列表。在all()函数迭代完这个新创建的列表后，该列表会因不再需要而被自动删除。

通过使用生成器表达式可以节省内存。生成器表达式遵循列表推导式的语法，但它们使用圆括号而不是方括号。

all()函数不建议传入列表推导式，建议用生成器表达式替代列表推导式，即把列表推导式的方括号改为小括号

## import

It is a common convention to place import statements at the top of your code. And additionally, in case of multiple import statements, sort them in alphabetical order to improve readability.

导入多个模块时，导入顺序按照字母顺序

## standarded lib 标准库

### string lib

存储字符串常量的标准库

#### constant `string.ascii_lowercase`

You can access the utilities defined inside the imported module through the dot notation. The dot notation works by appending a dot followed by the utility name to the module name. For example, here's how to access the `ascii_lowercase` constant:

    import string


    print(string.ascii_lowercase)
    # Output: abcdefghijklmnopqrstuvwxyz

### random lib

生成伪随机数，由于其确定性，不能用于加密

Every time the code runs, you should see a random character from the all_characters string. This is exactly what you want to achieve to create a random password.

However, the algorithm on which random relies makes the generated pseudo-random numbers predictable. Therefore, although the random module is suitable for the most common applications, it cannot be used for cryptographic purposes, due to its deterministic确定性的 nature.

#### function `random.random()`

The random module contains a pseudo-random 伪随机 number generator. Most of its functionalities depend on the random() function, which returns a floating point number in the range between 0.0 (inclusive) and 1.0 (exclusive).

返回区间 `[0, 1)` 之间的随机浮点数

#### function `random.choice()`

The choice() function from the random module takes a sequence and returns a random item of the sequence.

传入一个序列，返回这个序列中的某个元素

### secrets lib

类似于random，生成比random更安全的伪随机数

just like random lib

Although the effect might seem equal to `random.choice()`, secrets ensures you the most secure source of randomness that your operating system can provide.

### re lib

In your pattern, you can add a quantifier after a character to specify how many times that character should be repeated. For example, the + quantifier means it should repeat one or more times.

Add a + quantifier to your pattern.

`[]` 其中之一

A character class is indicated by square brackets and matches one character among those specified between the brackets. For example, `ma[dnt]` matches either `mad`, `man`, or `mat`.

`-` 范围

Character classes also allow you to indicate a range of characters to match. You need to specify the starting and the ending characters separated by an hyphen, `-`. Characters follow the Unicode order.

`^` 否定

The caret, `^`, placed at the beginning of the character class, matches all the characters except those specified in the class.

`.` 任意单个字符

The dot `.` character is a wildcard that matches any character in a string — except for a newline character by default. Modify pattern to match the entire string by replacing the current pattern with a . followed by the + quantifier.

转义字符

If you need to match a character that has a special meaning in the pattern, such as . or +, you can escape it by prepending a backslash character, `\.` For example, this matches a literal plus sign: `\+`.

纯字符串

Python provides a particular type of string called raw string. Raw strings are prefixed with a `r`. The key distinction from regular strings lies in how they handle the backslash character: in raw strings, backslashes are treated as literal characters rather than escape characters. When writing regular expressions, using raw strings is a good practice, since they can usually contain a lot of \ characters.

常用缩写

The character class `\d` is a shorthand for `[0-9]`. Replace this character class with the shorthand inside your first constraint tuple.

In a character class, you can combine multiple ranges by writing one range after another inside the square brackets (without any additional characters). For example: `[a-d3-6]` is the combination of `[a-d]` and `[3-6]`.

In the same way the `[0-9]` class is equivalent to `\d`, the `[^0-9]` class is equivalent to `\D`. Alphanumeric characters can be matched with `\w` and non-alphanumeric characters can be matched with `\W`.

Replace the `[^a-zA-Z0-9]` character class with `\W`.

Since the underscore character `_` is a valid character for variable names, it is included in the `\w` character class (equivalent to `[a-zA-Z0-9_]`), which can be conveniently used to match variable names.

Therefore, the `\W` character class is equivalent to `[^a-zA-Z0-9_]` with the underscore character that is not matched. For this reason you cannot use it to match all your special characters.

Now, combine your raw string with an f-string and interpolate your symbols variable inside the character class. Remember that you can interpolate a variable within an f-string using curly brackets { }.

#### re.compile()

A regular expression, or regex, is a pattern used to match a specific combination of characters inside a string. It is a valid alternative to if/else conditional statements when you need to match or find patterns inside a string for validation purposes, character replacement, and others.

The `compile()` function from the `re` module compiles the string passed as the argument into a regular expression object that can be used by other re methods.

#### function `re.search()` & method pattern.search(string)

The search() function from the re module analyzes the string passed as the argument looking for the first place where the regex pattern matches the string.

use method:

    pattern = re.compile('i')
    string = 'i like python'
    pattern.search(string)

use function:

    pattern = 'i'
    string = 'i like python'
    re.search(pattern, string)

#### findall()

just like search()

To check that the generated password meets the required features, you are going to use the findall() function from the re module. It's similar to search but it returns a list with all the occurrences of the matched pattern.