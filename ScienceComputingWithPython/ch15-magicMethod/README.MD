# Learn Special Methods by Building a Vector Space通过创建一个向量空间学习特殊方法

Python special methods are called in response to specific operations and enable you to customize the behavior of your objects in a detailed and effective way.

In this project, you are going to explore some of the most common special methods while learning about vectors by building a vector space.

A vector is an object that has a length (or magnitude) and a direction and it cannot be expressed by a single number. In physics, vectors are commonly used to represent forces, velocities, accelerations, and other quantities.

向量是一个既有长度（模norm）又有方向的对象。

In this project you are going to build a vector space, a set in which a series of operations is defined between the elements in that set. You'll learn all the details very soon.

A vector can be defined by two coordinates, x and y, in the Euclidean plane. The distance between the origin of the axes and the point (x, y) will be its length, or norm. And the vector direction will point towards (x, y).

![](https://cdn.freecodecamp.org/curriculum/python/2dvector.png)

## 魔术方法

Python offers various methods that include both a leading and trailing double underscore in their names. You may already be familiar with some, such as `__init__` and `__str__`. These methods, which follow the `__<name>__` naming pattern, are referred to as special methods, magic methods, or dunder (which stands for double underscore) methods.

Defining special methods in a class affects the behavior of that class. They are called under the hood in specific situations (e.g. `__init__` during instantiation, `__str__ `when the object is printed or passed to `str()`). In this project, you are going to learn some of the most commonly used special methods.

A vector can have a number `n` of dimensions (components). Here's a representation of a 3-dimensional vector:

So far, you created a 2-dimensional vector. You want to be able to represent vectors with a different number of dimensions without rewriting the necessary code for each specific case. For that, you will use inheritance.

![](https://cdn.freecodecamp.org/curriculum/python/3dvector.png)

Inheritance enables you to define a class from an existing one. The new class, called child, inherits all the methods and properties of the existing class, called parent.

    class Tree:
        def sprout(self):
            print('Making new leaves!')

    class Oak(Tree):
        pass
    
    Oak().sprout() # Output: Making new leaves!

In the example above, the child class Oak inherits from Tree and inherits the sprout method from the parent class Tree.

### super

`super()` enables you to refer implicitly to the parent class: `super().__init__(x, y)` calls the `__init__` method of the parent class.

### 强制使用关键字参数

In Python, you can enforce the use of keyword-only arguments by adding a `*` as an additional argument to the function or method signature. Modify both __init__ methods by adding a * as the second parameter (after self). Every parameter placed after that will require the use of a keyword argument in the function/method call.

### `__dict__` 属性

Every object in Python has a special attribute named `__dict__`, which is a dictionary that stores the object attributes.

在 Python 中，每个对象都有一个名为`__dict__`的特殊属性，它是一个字典，用于存储对象的属性。

对实例的 `.__dict__` 属性返回实例属性的字典，键是`__init__`中去除`self.`前缀的变量名

### vars()函数

The `vars()` built-in function takes an object as its argument and returns the `__dict__` attribute of that object.

内置函数 `vars()` 传入一个对象，返回这个对象的 `.__dict__` 属性的返回值

### `__str__` 和 `__repr__`

While the `__str__` method returns a human-readable string representation of an object, the `__repr__` method is supposed to return the string needed to instantiate the object.

- `__str__` 方法返回的是对象的人类可读字符串表示
- `__repr__` 方法理论上应返回能够用于实例化该对象的字符串，如果未定义 `__str__`，print(obj) 也会 fallback 到 `__repr__`

### 内置函数getattr()

Python 的内置函数 `getattr()` 用于获取对象的属性值，它可以动态地访问对象的属性，尤其适用于不确定属性名称的场景。传入对象和属性名，返回这个属性名对应的属性值

### `.__class__.__name__` 属性

You can access the name of a class with `__class__.__name__`. 

通过对象的`.__class__.__name__` 属性可以返回类名

### `__getattribute__` 魔术方法

The `__getattribute__` method is called under the hood any time you try to access an instance attribute. If the attribute is not found at the instance level, the method will search for it at the class level, and eventually in parent classes.

`__getattribute__` 方法在你每次尝试访问实例属性时都会在底层被调用。如果在实例级别未找到该属性，这个方法会去类级别查找，最终还会到父类中去搜索。

### `__getattr__` 魔术方法

`__getattr__` is another special method that plays a role in accessing attributes.

`__getattr__` 是另一个在属性访问过程中发挥作用的特殊方法。

The default implementation of `__getattribute__` is to raise an `AttributeError` when the requested attribute is not an instance attribute or it is not present in the class tree.

`__getattribute__` 的默认实现是：当请求的属性既不是实例属性，也不存在于类的继承体系中时，就会抛出 AttributeError 异常。

In that case, `__getattr__` is called if defined by the class. You can consider it as a sort of fallback when the usual attribute accessing procedure fails.

在这种情况下，如果类中定义了 `__getattr__`，那么就会调用它。你可以把它看作是常规属性访问流程失败时的一种 “兜底机制”。

As you can see from the output, although you defined `__getattr__` in your class, this method is not called yet. This happens because the default attribute access occurs through `__getattribute__`. Therefore, you can see the attribute value printed on the terminal.

从输出结果可以看出，尽管你在类中定义了 `__getattr__`，但这个方法目前还没有被调用。这是因为默认的属性访问是通过 `__getattribute__` 进行的。因此，你能看到属性值被打印到终端

### `__add__` 魔术方法

To create a vector space, you need to define how vectors should behave in several cases. Vectors can be added, forming a new vector.

The special method `__add__` can be implemented to override what happens by default when two objects are added together using the `+` operator.

特殊方法 `__add__` 可以通过实现来重写两个对象使用 + 运算符进行相加时的默认行为。

The `other` parameter of your `__add__` method represents the operand placed at the right side of the `+` operator in an addition operation.

### NotImplemented

在 Python 中，`NotImplemented` 是一个特殊的单例对象（singleton），用于表示某个操作在当前上下文下无法实现，通常在自定义魔术方法（如算术运算、比较运算相关方法）中作为返回值使用。

In Python, `NotImplemented` is a special value used to indicate that an operation is not implemented for a specific case.

`NotImplemented` does not raise an exception immediately. Instead, it signals to ask to the other operand how to perform the operation. If the request cannot be satisfied, a `TypeError` is returned by default.

Because you want to be able to sum two vectors only if they belong to the same class, return `NotImplemented` from the if statement you created in the previous step.

You can unpack a dictionary into keyword arguments by using the `**` operator:

`**` 运算符，用于字典解包，将字典转换为关键字参数

    def spam(a, b):
        return a + b

    my_dict = {a: 11, b: 4}

    spam(**my_dict) # 15 
    # 相当于spam(a=11, b=4)

### `.__class__` 魔术属性

在 Python 中，__class__ 是一个特殊的魔术属性（magic attribute），用于获取对象所属的类。

Return an instance of the current class by using __class__ and passing **kwargs as the argument.

### `__sub__` 魔术方法

减法

In the same way `__add__` is called under the hood when two objects are added together, the `__sub__` method is called implicitly in case of subtraction.

### `__mul__` 魔术方法

乘法

The special method `__mul__` can be implemented to specify what should happen when the current instance is multiplied by another object.

Vectors can be multiplied by a scalar, i.e. a number that multiplies each single component. The result of scalar multiplication is a vector with the same orientation as the original vector but a different magnitude.

Implement the scalar multiplication by checking if other is either an `int` or a `float`. If it is, return a new instance of the current class that has each component of the starting vector multiplied by other. This will be the vector resulting from the scalar multiplication.

Make sure the methods can be applied to compute the scalar multiplication of vectors with any number of dimensions.

### `__eq__` 魔术方法

比较运算：等于

The `__eq__` method can be implemented to specify what should happen in case the comparison operator (==) is used to compare an object with something else.

You want to compare two vectors, only when they belong to the same class. For that create an if statement that checks if self and other do not belong to the same class and return NotImplemented in that case.

### `__ne__` 魔术方法

比较运算：不等

The `__ne__` method is called under the hood when the != operator is used. Define a `__ne__` method with two parameters self and other. From your new method, return the opposite of self == other.

### `__lt__` 魔术方法

比较运算：小于

The `__lt__` method is called under the hood when the < operator is used to compare an object with something else.

### `__gt__` 魔术方法

比较运算：大于

The `__gt__` method is called under the hood when the > operator is used to compare an object with something else.

After the __lt__ method, in the same way you did for __lt__, implement the __gt__ method. Pay attention to use the appropriate operator.

### `__le__` 魔术方法

比较运算：小于等于

There are still two possible comparisons to implement. The `__le__` method is called when the <= operator is used to compare two objects.

### `__ge__` 魔术方法

比较运算：大于等于

The last method you need is `__ge__`, which is called when the >= is used to compare two objects.

The cross product, or vector product, is defined between 3-dimensional vectors and results in a third vector perpendicular to both of them.

The R3Vector class inherits from R2Vector, meaning it has access to all the methods and properties defined in R2Vector. A child class can implement additional features. You already saw a way to change the implementation of a method. Now, you are going to give the child class R3Vector a new method instead.

Within the R3Vector class, define a cross method and give it two parameters: self, and other.