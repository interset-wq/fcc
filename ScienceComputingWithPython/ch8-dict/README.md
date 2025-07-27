# Learn Algorithm Design by Building a Shortest Path Algorithm

在 Python 中，float('inf') 表示正无穷大，是一种特殊的浮点数值

Algorithms are step-by-step procedures that developers use to perform calculations and solve computational problems.

In this project, you'll learn how to use functions, loops, conditional statements, and dictionary comprehensions to implement a Shortest Path algorithm.

Graphs are data structures representing relations between pairs of elements. These elements, called nodes, can be real-life objects, entities, points in space or others. The connections between the nodes are called the edges.

图是表示元素对之间关系的数据结构。这些元素被称为节点，可以是现实生活中的对象、实体、空间中的点或其他事物。节点之间的连接称为边。

Here's a visual representation of a graph:

![](https://cdn.freecodecamp.org/curriculum/python/graph1-example.png)

For example, a graph can be used to represent two points in the space, A and B, connected by a path. A graph like this will be made of two nodes connected by an edge.

例如，图可用于表示空间中的两个点 A 和 B，这两个点由一条路径连接。这样的图由通过一条边连接的两个节点构成。

A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.

当图的边被赋予权重（表示距离、时间或其他量化值）时，该图被称为加权图。

Now you are going to start developing the algorithm to calculate the shortest path between each node in your new graph.

The algorithm will start at a specified node. Then it will explore the graph to find the shortest path between the starting node, or source, and all the other nodes.

While the algorithm explores the graph, it should keep track of the currently known shortest distance between the starting node and the other nodes.

## list()

The list() type constructor enables you to build a list from an iterable.

将可迭代类型转换为列表，对字典使用时，返回键的列表

## dictionary comprehension 字典推导式

With a dictionary comprehension, you can create a dictionary starting from an existing dictionary:

    {key: val for key in dict}

In the example above, val is the value that key will have in the new dictionary, and dict is the existing dictionary.

Dictionary comprehensions support conditional if/else syntax too:

    {key: val_1 if condition else val_2 for key in dict}

In the example above, dict is the existing dictionary. When condition evaluates to True, key will have the value val_1 , otherwise val_2.

## min()

min() takes also a keyword-only argument. Passing a function as an additional argument to min(), you can modify the way the list items are compared.

The result of the line you've just written in the previous step is the node that comes first in alphabetical order. Instead you want to select the unvisited node having the smallest distance from the starting node.

Pass key=distances.get as the second argument to your min() call. In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.

## extend()

The `.extend()` method, allows you to add elements from an iterable to the end of a list:

    my_list = ['larch', 'birch']
    tree_list = ['fir', 'redwood', 'pine']
    my_list.extend(tree_list)
    print(my_list) # Output: ['larch', 'birch', 'fir', 'redwood', 'pine']

## remove()

The `.remove()` method removes from a list the first matching element that is passed as the argument:

    my_list = ['larch', 1, True, 1]
    my_list.remove(1)
    print(my_list) # Output: ['larch', True, 1]

## 三目运算符

Python provides a concise way to write if/else conditionals by using the ternary syntax:

    val_1 if condition else val_2

The expression above evaluates to val_1 if condition is true, otherwise to val_2.

## data type 数据类型

So far, you have already met different data types:

- Immutable data types, such as integers, strings, tuples, and Booleans.
- Mutable data types, such as lists, and dictionaries.
- A dictionary is identified by a pair of curly braces, {}.

## iterate keys 遍历字典的键

To iterate over the keys of a dictionary, you can simply put the dictionary into a for loop. The code below would print each key in the dictionary dict:

    for i in dict:
        print(i)

## iterate values 遍历字典的值

If you want to iterate over the values of the dictionary keys, one way is to use the `.values()` method.

## iterate both keys and values 同时遍历字典的键和值

Finally, if you want to be able to go through the key-value pairs, you can use the .items() method.

As you can see from the output, `.items()` creates a data structure that stores each key-value pair in a distinct tuple. To iterate over the elements in those tuples you can add a second loop variable:

    for i, j in dict.items():
        print(i, j)

## del 删除字典的键

You can remove a key-value pair from a dictionary by using the del keyword:

    my_dict = {
        'name': 'Michael',
        'occupation': 'Lumberjack'
    }

    del my_dict['occupation']