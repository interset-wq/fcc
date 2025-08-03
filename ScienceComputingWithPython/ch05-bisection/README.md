# Learn the Bisection Method by Finding the Square Root of a Number通过求一个数的平方根学习二分法

Numerical methods are used to approximate solutions to mathematical problems that are difficult or impossible to solve analytically.

In this project, you will explore the numerical method of bisection to find the square root of a number by iteratively narrowing down the possible range of values that contain the square root.

## more

Give the square_root_bisection function the following parameters:

square_target: The number for which you want to find the square root.
tolerance (optional): The acceptable difference between the square of the approximate root value and the actual target value (default is 1e-7). The tolerance 1e-7 implies that the solution will be accurate to within 0.0000001 of the true value and is a good default choice that balances accuracy and performance.
max_iterations (optional): The maximum number of iterations to perform (default is 100). If the method doesn't converge within this limit, you'll assume the solution is not found.

## raise

The raise statement allows you to force a specific exception to occur. It consists of the raise keyword followed by the exception type, and enables you to provide a custom error message:

    raise ValueError("Invalid value")

When the code above runs, a ValueError is raised and the message "Invalid value" is shown to the user.

## range

Now you'll repeatedly narrow down the interval by finding the midpoint of the current interval and comparing the square of the midpoint with the target value.

For that, inside the else block, create a for loop that runs up to max_iterations times.

For your loop, use the range function, which generates a sequence of numbers you can iterate over. The syntax is range(start, stop, step), where start is the starting integer (inclusive), stop is the last integer (not inclusive), and step is the difference between a number and the previous one in the sequence.

Also, use _ as a loop variable. The _ acts as a placeholder and is useful when you need to use a variable but don't actually need its value.

## abs

The abs() function returns the absolute value of a number, which is always positive, regardless of the number sign. You will use it to check that the estimated square root is close enough to the actual value.

## is

In Python, the is keyword checks for object identity. It's used to determine if two variables point to the same object in memory. In contrast to is, the equality operator (==) determines if the values of two objects are the same, regardless of whether they are the same object in memory.

Outside the for loop, create an if statement to check if root is None. If it is, print the message 'Failed to converge within {max_iterations} iterations.'. Remember to format the message using an f-string.