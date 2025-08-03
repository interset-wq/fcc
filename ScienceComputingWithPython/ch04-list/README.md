# Learn Python List Comprehension by Building a Case Converter Program通过创建大小写转换程序学习列表推导式

List Comprehension is a way to construct a new Python list from an iterable types: lists, tuples, and strings. All without using a for loop or the `.append()` list method.

In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

The project has two phases: first you'll use a for loop to implement the program. Then you'll learn how to use List Comprehension instead of a loop to achieve the same results.

## list comprehension

    spam = [i * 2 for i in iterable]

List comprehensions accept conditional statements, to evaluate the provided expression only if certain conditions are met:

    spam = [i * 2 for i in iterable if i > 0]

Still, the final result is not exactly what you want to achieve. You need to execute a different expression for the characters filtered out by the if clause. You'll use an else clause for that:

    spam = [i * 2 if i > 0 else -1 for i in iterable]

Note that, differently from the `if` clause, the `if`/`else` construct must be placed between the expression and the `for` keyword.