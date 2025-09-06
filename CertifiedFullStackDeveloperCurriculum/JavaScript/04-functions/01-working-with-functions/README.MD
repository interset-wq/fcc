# Working with Functions, Not started
In these lectures, you will learn how to reuse a block of code with functions. You will learn what the purpose of a function is and how they work, and how scope works in programming.

## What Is the Purpose of Functions, and How Do They Work?
函数的用途是什么，它们是如何工作的？
Functions are reusable pieces of code that perform a specific task or calculate a value. Think of functions as a machine that takes some input, does some operations on it, and then produces an output. Here is an example of declaring a function:
函数是可重用的代码片段，用于执行特定任务或计算值。可以将函数想象成一个机器，它接收一些输入，对其进行一些操作，然后产生输出。以下是声明函数的示例：

function greet() {
  console.log("Hello, Jessica!");
}
In this example, we have declared a function called greet. Inside that function, we have a console.log that logs the message Hello, Jessica!. If we tried to run this code, we would not see the message appear in the console. This is because we need to call the function.
在这个示例中，我们声明了一个名为 greet 的函数。在该函数内部，有一个 console.log 用于记录消息 Hello, Jessica! 。如果我们尝试运行这段代码，将不会在控制台中看到消息显示。这是因为我们需要调用该函数。

A function call, or invocation, is when we actually use or execute the function. To call a function, you will need to reference the function name followed by a set of parentheses:
函数调用，或称为执行，是指我们实际使用或执行函数。要调用函数，需要引用函数名称，后跟一组括号：

function greet() {
  console.log("Hello, Jessica!");
}

greet(); // "Hello, Jessica!"
Now the message of Hello, Jessica! will be logged to the console. But what if we wanted the message to say Hello, Nick! or Hello, Anna!? We don't want to write a new function each time we greet a different user. Instead, we can create a reusable function that uses function parameters and arguments.
现在消息 Hello, Jessica! 将会被记录到控制台。但如果我们想让消息显示 Hello, Nick! 或 Hello, Anna! 呢？我们不想每次问候不同的用户时都编写一个新的函数。相反，我们可以创建一个可重用的函数，该函数使用函数参数和实参。

Parameters act as placeholders for the values that will be passed to the function when it is called. They allow functions to accept input and work with that input. Arguments are the actual values passed to the function when it is called. Here is an updated version of the greet function that uses parameters and arguments:
参数充当占位符，用于存储在调用函数时传递给函数的值。它们允许函数接收输入并处理该输入。实参是在调用函数时传递给函数的实际值。这是使用参数和实参的 greet 函数的更新版本：

function greet(name) {
  console.log("Hello, " + name + "!");
}

greet("Alice"); // Hello, Alice!
greet("Nick"); // Hello, Nick!
The name serves as the parameter while the strings Alice and Nick serve as the arguments. Now we have a reusable function that can be used dozens of times throughout our code with different arguments.
name 作为参数，而字符串 Alice 和 Nick 作为实参。现在我们有一个可重用的函数，可以在整个代码中使用不同的实参多次。

When a function finishes its execution, it will always return a value. By default, the return value will be undefined. Here is an example:
当函数完成执行时，它总会返回一个值。默认情况下，返回值将是 undefined 。这里有一个示例：

function doSomething() {
    console.log("Doing something...");
}

let result = doSomething();
console.log(result); // undefined
If you need your function to return a specific value, then you will need to use the return statement. Here is an example of using a return statement to return the sum of two values:
如果你需要你的函数返回一个特定值，那么你需要使用 return 语句。这里是一个使用 return 语句返回两个值之和的例子：

function calculateSum(num1, num2) {
  return num1 + num2;
}

console.log(calculateSum(3, 4)); // 7
Often times you will be using the return statement, because you can use that value that was output from the function later on in your code.
通常情况下你会使用 return 语句，因为你可以使用函数输出的值在代码的其他部分。

So far, we've been working with named functions, but you can also create what's called an anonymous function. An anonymous function is a function without a name that can be assigned to a variable like this:
到目前为止，我们一直在处理命名函数，但你也可以创建一种称为匿名函数的东西。匿名函数是一个没有名称的函数，可以像这样赋值给一个变量：

const sum = function (num1, num2) {
  return num1 + num2;
};

console.log(sum(3, 4)); // 7
In this example, we have a const variable called sum and we are assigning it an anonymous function that returns the sum of num1 and num2. We are then able to call sum and pass in the numbers 3 and 4 to get the result of 7.
在这个例子中，我们有一个 const 变量叫做 sum ，我们把它赋值为一个匿名函数，这个函数返回 num1 和 num2 的和。然后我们能够调用 sum 并传入数字 3 和 4 来得到结果 7 。

Functions support default parameters, allowing you to set default values for parameters. These default values are used if the function is called without an argument for that parameter. Here's an example:
函数支持默认参数，允许您为参数设置默认值。如果函数调用时没有为该参数提供实参，则使用这些默认值。这里有一个例子：

function greetings(name = "Guest") {
  console.log("Hello, " + name + "!");
}

greetings(); // Hello, Guest!
greetings("Anna"); // Hello, Anna!
In this example, if no argument is provided for name, it defaults to Guest.
在这个例子中，如果为 name 没有提供参数，它将默认为 Guest 。

In summary, functions allow you to write reusable and organized code. They can take inputs (parameters), perform actions, and return outputs.
总而言之，函数允许你编写可重用和有组织的代码。它们可以接收输入（参数），执行操作，并返回输出。

