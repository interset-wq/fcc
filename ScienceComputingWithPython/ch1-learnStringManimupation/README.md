# Learn String Manipulation by Building a Cipher通过创建密码学习字符串操作

Python is a powerful and popular programming language widely used for data science, data visualization, web development, game development, machine learning and more.

In this project, you'll learn fundamental programming concepts in Python, such as variables, functions, loops, and conditional statements. You'll use these to code your first programs.

## slice切片

### index

use `[index]` to acquire a char in the string, just like a list

my_str = "hello world"
print(my_str[0]) # h

### method

- `str.find(char)` give it a char, it will return the index of the char in the str. If the char is not found, it returns `-1`
- `.index()` just like `.find()`, but it throws a `ValueError` exception if it is unable to find the substring.
- `str.lower()` give it nothing. retutn lowercase version od str
- `str.isalpha()` give it nothing. if str are letters, return `True`

### built-in function

#### print()

it can take multiple arguments, separated by a comma.

#### len()

acquire the length of the string

#### type()

return data type

## Project

### Caesar cipher

The first kind of cipher you are going to build is called a Caesar cipher. Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after 3 positions in the alphabet, and replace the original letter with the new letter.