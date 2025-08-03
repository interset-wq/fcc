# Learn Recursion by Solving the Tower of Hanoi Puzzle通过解决汉诺塔问题学习递归

Recursion is a programming approach that allows you to solve complicated computational problems with just a little code.

In this project, you'll start with a loop-based approach to solving the tower of Hanoi mathematical puzzle. Then you'll learn how to implement a recursive solution.

In this project, you will solve the mathematical puzzle known as the Tower of Hanoi. The puzzle consists of three rods and a number of disks of different diameters.

The goal of this puzzle is moving the disks圆盘 from the first rod to the third rod杆, following specific rules that restrict placing a larger disk on top of a smaller one.

The goal of the Tower of Hanoi is moving all the disks to the last rod. To do that, you must follow three simple rules:

You can move only top-most disks
You can move only one disk at a time
You cannot place larger disks on top of smaller ones

The Tower of Hanoi puzzle can be solved in 2^n - 1 moves, where n is the number of disks. Declare a variable named number_of_moves and assign the total number of moves to this variable.

The power operator in Python is **.

In the Tower of Hanoi puzzle, you can identify the three rods according to their purpose:

The first rod is the source, where all the disks are stacked on top of each other at the beginning of the game.
The second rod is an auxiliary rod, and it helps in moving the disks to the target rod.
The third rod is the target, where all the disks should be placed in order at the end of the game.

To solve the puzzle with recursion, the first thing to do is break the original problem down into smaller sub-problems.

The final configuration with n disks piled up to the third rod in decreasing order can be obtained by moving:

n - 1 disks from the source to the auxiliary rod
the largest disk from the source to the target
and then the n - 1 disks from the auxiliary rod to the target.
So, the first thing the move function should do is calling itself with n - 1 as the first argument. But if you try to do so without defining a base case, you will get a RecursionError. This happens because the function keeps calling itself indefinitely.

## range

The syntax is `range(x, y, h)`, where x is the starting integer (inclusive), y is the last integer (not inclusive), and h is the difference between a number and the next one in the sequence.

The range() function returns an immutable sequence of numbers. As you can see, the data type of rods['A'] is range, but you want it to be a list.

Pass your range() call to the list() function to do that.