# Learn Classes and Objects by Building a Sudoku Solver数独谜题

Classes and objects are important programming concepts. These Object-Oriented Programming tools help developers to achieve code modularity, abstraction, and readability. And they promote reusability.

In this Sudoku Solver project, you'll learn how to use classes and objects to build a Sudoku grid and to solve a Sudoku puzzle.

## enumerate()

The enumerate built-in function takes an iterable as its argument and returns an enumerate object you can iterate over. It provides the count (which by default starts at zero) and the value from the iterable.

    iterable = ['a', 'b', 'c']
    for i, j in enumerate(iterable):
        print(i, j)

The loop from the example above would output the tuples 0, a, 1, b, and 2, c.

## tuple

A tuple can be unpacked, meaning that the elements contained in the tuple can be assigned to variables, like this:

    spam = ('lemon', 'curry')
    item1, item2 = spam

In the example above, item1 would have the value 'lemon' and item2 would have the value 'curry'.

## walrus operator海象运算符

The `:=` operator gives you the ability to assign variables in the middle of an expression. The syntax is: name := val, where name is the variable name and val is the variable value.

This construct is formally named assignment expressions, while the `:=` operator is commonly referred to as the walrus operator.

## __str__

The `__str__` method is a special method that is called under the hood when the object is printed using the print() function, or converted into a string using the str() function.

## try-except

The .index() method raises a ValueError exception when the value is not found. To prevent the program from halting execution, you'll nest this line of code inside a try block. The try statement is used to encapsulate code that might raise an exception. The except clause, on the other hand, offers alternative code to execute if an exception occurs:

    try:
        <code>
    except:
        <code>

## init

The instantiation creates an empty object. The __init__ method is a special method that allows you to instantiate an object to a customized state. When a class implements an __init__ method, __init__ is automatically called upon instantiation.