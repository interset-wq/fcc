# Learn Lambda Functions by Building an Expense Tracker通过开支计算器学习lambda表达式

Lambda functions give you a concise way to write small, throwaway functions in your code.

In this project, you'll explore the power of Lambda Functions by creating an expense tracker. Your resulting app will demonstrate how you can use Lambda Functions for efficient, streamlined operations.

## list method

- `.append(elem)` append elements to the end
- `.insert(index, elem)` use index to insert element
- `.pop(index)` use index to delete an element
- `.pop()` give it nothing, it will delete the last element

## lambda

Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. They are defined by the lambda keyword, and they use the following syntax:

    lambda x: expr

In the example above, x represents a parameter to be used in the expression expr, and it acts just like any parameter in a traditional function. expr is the expression that gets evaluated and returned when the lambda function is called.

## map()

Lambda functions can be valuably combined with the map() function, which executes a specified function for each element in a collection of objects, such as a list:

    map(lambda x: x * 2, [1, 2, 3])

The function to execute is passed as the first argument, and the iterable is passed as the second argument.

The result of the example above would be [2, 4, 6], where each item in the list passed to map() has been doubled by the action of the lambda function.

You should see something like `<map object at 0xd273a8>` printed on the console, which is the string representation of the map object returned by map().

o obtain a readable output you need to turn the map object into a list. Do it by passing the map() call as the argument to the list() function.

The sum() function returns the sum of the items in the iterable which is passed as its argument. You are going to use sum() together with map() and lambda functions to get the total amount of expenses.

## filter()

The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:

    filter(my_function, my_list)

filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.

The result of the example above is an iterator containing the elements of my_list for which my_function returns True.