# Learn Encapsulation by Building a Projectile Trajectory Calculator通过构建抛物线计算器学习封装

Encapsulation is a core OOP principle based on writing code that limits direct access to data.

In this project, you'll discover new concepts related to encapsulation, such as getters, setters, and name mangling, and you'll use them together with what you already learned to create a program that calculates a projectile trajectory.

封装是面向对象编程的核心原则，其基础是编写限制对数据直接访问的代码。

在本项目中，你将学习与封装相关的新概念，如 getter（访问器）、setter（修改器）和名称修饰，并且会结合已学知识创建一个计算 projectile 轨迹的程序。

You are going to build a program that calculates and draws the trajectory of a projectile given the angle, speed and height of the throw.

Start by importing math, you will use it a lot in this project as it has useful methods like math.radians, math.cos, math.sin and others.

Also create these variables to have the value of the gravitational acceleration and some special symbols that will be useful later (use copy and paste for these).

Example Code
GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


Create a Projectile class with an __init__ method that initializes the class using three arguments: the starting speed, the starting height, and the starting angle of the throw of the projectile, in this order.

Inside the __init__ method, assign these arguments to three private attributes: __speed, __height, and __angle. The angle provided will be in degrees; however, it should be stored internally in radians. To achieve this, use the math.radians() function to convert the angle from degrees to radians when assigning it to __angle.

The use of two underscores before an attribute name triggers name mangling in Python. This means the attributes are not directly accessible from outside the class using their given names, and must be accessed with the mangled names like ball._Projectile__height if needed externally, indicating these are intended for internal use only.

The class variable __slots__ has a special usage in Python classes. Declaring __slots__ and assigning it a sequence of strings restricts the creation of attributes to those included in that sequence. Also, it prevents the creation of the __dict__ special attribute and it allows for more efficient attribute access.

You should use the __slots__ variable inside the class to define which attributes the class has: assign to __slots__ a tuple containing 3 strings, each equal to one of the attribute names defined in the __init__.

The first thing to set up is a method that calculates the displacement of the projectile, which is the horizontal space traveled from the throw to when the projectile touches the ground.

Create a method __calculate_displacement, which has only self as a parameter, and return the displacement of the projectile.

Use the following formula to compute the projectile displacement:
d=v⋅cosθ⋅(v⋅sinθ+v2⋅sin2θ+2⋅g⋅h−−−−−−−−−−−−−−−√)g
 

In which  d
  is the displacement,  v
  is the starting speed,  θ
  is the angle and  h
  is the starting height of the projectile. For  g
  you can use the GRAVITATIONAL_ACCELERATION variable.

You should use the methods math.cos() and math.sin() for the trigonometric functions and math.sqrt() to calculate the square root. Also you should know that  xy
  is written as x ** y in python. Also  sin2θ
  means that the value resulting from the sine is then squared.

Remember that with name mangling you need to call the method as _Projectile__calculate_displacement if you want to test, or use it from outside of the class:

Example Code
ball = Projectile(10, 3, 45)
displacement_of_ball = ball._Projectile__calculate_displacement()

At this point you are ready to create the string representation. Start by creating an instance of the Projectile class. Below the class definition, create a ball variable and assign it a call to Projectile using 10, 3, 45 as arguments.

Define a __str__ method within the class, to give your instance a proper string representation, and make it return a string with the following format:

Example Code

Projectile details:
speed: 10 m/s
height: 3 m
angle: 45°
displacement: 12.6 m

It should start and end with a new line character, the angle has to be written as an integer in degrees and the displacement should be printed with one decimal digit.

You will find useful math.degrees to convert the angle from radians to degrees.

When you are ready you can print(ball) to test your function.

Now it's time to work on calculating the coordinates of the trajectory! Create a method of the Projectile class named __calculate_y_coordinate, it should have, other than self, an x parameter.

y=y0+xtanθ−gx22v20cos2θ
 

The above is the formula to calculate the vertical position  y
  for any given horizontal position  x
 , having the starting angle  θ
 , speed  v0
  and height  y0
 .

You will need to use math.tan() and math.cos() and remember that x ** y is the way to write  xy
 , and that the value of  g
  is in the variable GRAVITATIONAL_ACCELERATION.

Implement the method so that it returns the  y
  coordinate.

If you want to test the method, from outside of class, you can call ball._Projectile__calculate_y_coordinate() with a number as an argument after ball is declared.

Define a method named calculate_all_coordinates, which calculates the coordinates for all  x
  values from 0 up to the displacement rounded up (not inclusive), and then returns them as a list of tuples (x, y).

Then, call the calculate_all_coordinates method on the ball instance and assign the output to a new variable named coordinates.

You can use math.ceil() to round up a number to the smallest integer greater than or equal to that number.

It's time to talk about encapsulation and getters. You have written the three instance attributes to be private using a leading double underscore. Note that these attributes are called private by convention: although they can still be accessed from outside, it is agreed upon to not do that.

Getters are what can be used to get the values from outside. To define a getter, you define a method that returns the value of the desired attribute and give it a @property decorator:

Example Code
class Nest:
    ...
    @property
    def number_of_eggs(self):
        return self.__number_of_eggs
The decorator changes the method into a property, meaning that the method is not called like a regular method, but it's used like an attribute:

Example Code
n = Nest()
print(n.number_of_eggs)
In the example above, the private attribute __number of eggs is accessed through the number_of_eggs property of n.

Create a getter named speed and make it return the value of the private attribute __speed.

Now create the two getters for __height and __angle. Remember that for the angle, the value is given to the class in degrees, but is saved internally in radians, so have the getter return the degrees value. You can use math.degrees, and the round function for this.

Once you have the getters, you can write the setters, which allow you to set the value of an attribute in an indirect manner. Following the example of the last step, a setter would be written as:

Example Code
class Nest:
    ...
    @number_of_eggs.setter
    def number_of_eggs(self, new_value):
        self.__number_of_eggs = new_value
Same as the getter, a setter is not called like a method but used like an attribute:

Example Code
nest = Nest()
nest.number_of_eggs = 12
This way of writing calls the setter and set the new value.

For this step you will have to write the setters for the three private attributes. Remember that for the angle the value is received in degrees but saved internally in radians.

The __str__ method refers to the attributes of the class directly, but now that you have created the getters it is better to use those to obtain those values.

Edit the __str__ method to not reference the attributes anymore, but to use the getters.

It's good practice to give a representation to the class by using the __repr__ special method. While the __str__ method returns a readable string representation that's intended to be user friendly, __repr__ is intended for programmers. Often __repr__ provides a string that can be used to recreate the object.

Write the __repr__ method, which will return the string needed to instantiate the object.

You can test this by calling the repr function and passing it an instance of the class.

Going back to the projectile trajectory calculator, now you'll create a new class that accepts a list of coordinates and creates the trajectory drawing.

Create a new class Graph, which should be instantiated with a private attribute __coordinates where the list of coordinates is stored. Declare the __slots__ class variable and define the __init__ and __repr__ special methods.

Also, create a Graph instance passing the coordinates variable and assign it to a new graph variable.

Create a method create_coordinates_table, then at the end of the code print graph.create_coordinates_table()).

The method should use the __coordinates property and return a string containing all the coordinates, where x and y have always the same position, the values for x are always integers, and the values for y are always rounded to two decimal places:

Example Code
  x      y
  0   3.00
  1   3.90
  2   4.61
  3   5.12
  4   5.43
  5   5.55
  6   5.47
  7   5.19
  8   4.72
  9   4.05
 10   3.19
 11   2.13
 12   0.87  
The table should start with a newline character and end with a newline character.

Now it's time for the graph. Create a method create_trajectory and replace the last print call at the bottom of your code with print(graph.create_trajectory()).

As the first step of this new method, make a local copy of the coordinates but where all the values are rounded to integers. Save this new version of the coordinates in a variable named rounded_coords, and return this variable.