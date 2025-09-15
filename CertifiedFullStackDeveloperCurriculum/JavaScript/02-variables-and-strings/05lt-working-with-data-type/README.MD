# Working with Data Types 数据类型

In the following lectures, you will learn how to work with data types in JavaScript. You will also learn how dynamic typing differs from static typing, the typeof operator, and the typeof null bug.

## What Is Dynamic Typing in JavaScript, and How Does It Differ from Statically Typed Languages?

JavaScript is a dynamically typed language, meaning you don't need to specify the data type of a variable when you declare it. Instead, the type is determined based on the value assigned to the variable while the program is running. This allows you to change the type of a variable throughout the program.

JavaScript 是一种动态类型语言，这意味着您在声明变量时无需指定变量的数据类型。相反，类型是根据程序运行时分配给变量的值确定的。这允许您在整个程序中更改变量的类型。

Let's look at an example:

让我们看一个例子：

let example = "Hello";
example = 42;

In this example, we have a variable called example with the data type of string. But then we update value to be a number instead.

在这个例子中，我们有一个名为 example 的变量，数据类型为 string。但是，我们将 value 更新为数字。

The flexibility of dynamic typing makes JavaScript more forgiving and easy to work with for quick scripting, but it can also introduce bugs that may be harder to catch, especially as your program grows larger.

动态类型的灵活性使 JavaScript 更加宽容且易于使用以快速编写脚本，但它也可能引入可能更难捕获的错误，尤其是当您的程序变得越来越大时。

In statically typed languages like Java or C++, you must declare the data type of a variable when you create it, and that type cannot change.

在 Java 或 C++ 等静态类型语言中，您必须在创建变量时声明变量的数据类型，并且该类型不能更改。

For instance, if you declare a variable as integer, you can only assign it integer values. If you try to assign it a different type, the program will throw an error.

例如，如果您将一个变量声明为整数 ，则只能为其赋值整数值。如果您尝试为其分配不同的类型，程序将抛出错误。

Here's an example in Java language:

这是一个 Java 语言示例：

int value = 42; // value must always be an integer
value = "Hello"; // This would cause an error in Java

The difference between dynamic typing and static typing lies in the flexibility vs. the safety of your code. Dynamically typed languages offer flexibility but at the cost of potential runtime errors.

动态类型和静态类型之间的区别在于代码的灵活性与安全性。动态类型语言提供了灵活性，但代价是潜在的运行时错误。

Statically typed languages enforce stricter rules that can prevent certain errors, but they require more upfront declaration and offer less flexibility in changing types.

静态类型语言强制执行更严格的规则，可以防止某些错误，但它们需要更多的预先声明，并且在更改类型时提供较少的灵活性。

Here is another example of creating a variable with a type set to number then changing it to later be of type string:

这是另一个创建类型设置为 number 的变量的示例，然后将其更改为字符串类型：

let data = 100;  // Initially a number
data = "New data";  // Dynamically changes to a string

In a statically typed language, this kind of change would not be allowed, as the data type would be fixed.

在静态类型语言中，不允许进行这种更改，因为数据类型是固定的。

In conclusion, JavaScript's dynamic typing allows variables to change types freely, which offers flexibility but can lead to unexpected errors during execution.

总之，JavaScript 的动态类型允许变量自由更改类型，这提供了灵活性，但在执行过程中可能会导致意外错误。

Statically typed languages like Java require you to specify variable types upfront, which helps catch errors before the program runs but offers less flexibility.
像 Java 这样的静态类型语言要求您预先指定变量类型，这有助于在程序运行之前捕获错误，但灵活性较差。

## How Does the typeof Operator Work, and What Is the typeof null Bug in JavaScript?
typeof 运算符如何工作，JavaScript 中的 typeof null 错误是什么？
The typeof operator in JavaScript is a simple yet powerful tool that lets you see the data type of a variable or value. It always returns a string indicating the type.
JavaScript 中的 typeof 运算符是一个简单而强大的工具，可让您查看变量或值的数据类型。它始终返回一个指示类型的字符串。

Let's take a look at a few examples:
让我们看几个例子：

let num = 42;
console.log(typeof num); // "number"
In this first example, we have created a variable called num and assigned it the number 42. When you use the typeof operator on the variable named num, it will return the string number.
在第一个示例中，我们创建了一个名为 num 的变量，并为其分配了数字 42。当您在名为 num 的变量上使用 typeof 运算符时，它将返回字符串 number。

Here is another example of using the typeof operator on variable called isUserLoggedIn:
这是在名为 isUserLoggedIn 的变量上使用 typeof 运算符的另一个示例：

let isUserLoggedIn = true;
console.log(typeof isUserLoggedIn); // "boolean"
When you use the typeof operator on the isUserLoggedIn variable, it will return a string boolean because the boolean true was assigned to the variable.
当您在 isUserLoggedIn 变量上使用 typeof 运算符时，它将返回一个字符串布尔值 ，因为布尔值 true 已分配给该变量。

Using the typeof operator can be especially useful when you're debugging or trying to understand what kind of data you're working with in your code.
当您调试或尝试了解您在代码中使用的数据类型时，使用 typeof 运算符特别有用。

However, there's a well-known quirk in JavaScript when it comes to null.
然而，当涉及到 null 时，JavaScript 中有一个众所周知的怪癖。

Let's take a look at an example:
我们来看一个例子：

let exampleVariable = null;
console.log(typeof exampleVariable); // "object"
In this example, we have a variable called exampleVariable and have assigned it the value of null. But when we use the typeof operator, it returns the string object.
在此示例中，我们有一个名为 exampleVariable 的变量，并为其分配了 null 值。但是当我们使用 typeof 运算符时，它会返回字符串对象 。

This is widely considered a bug in JavaScript, dating back to its early days. The reason for this behavior is rooted in the way JavaScript was originally designed.
这被广泛认为是 JavaScript 中的一个错误，可以追溯到早期。这种行为的原因源于 JavaScript 最初的设计方式。

When the language was first implemented, values like null were represented as a special type of object, leading to this unexpected result.
当该语言首次实现时，像 null 这样的值被表示为一种特殊类型的对象，导致了这种意外的结果。

Unfortunately, this has become a part of the language, and while it's confusing, it's something you'll need to be aware of.
不幸的是，这已经成为语言的一部分，虽然它令人困惑，但这是您需要注意的事情。

