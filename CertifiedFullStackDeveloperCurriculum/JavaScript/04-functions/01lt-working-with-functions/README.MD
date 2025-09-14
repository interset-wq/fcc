# Working with Functions

In these lectures, you will learn how to reuse a block of code with functions. You will learn what the purpose of a function is and how they work, and how scope works in programming.

## What Is the Purpose of Functions, and How Do They Work?

Functions are reusable pieces of code that perform a specific task or calculate a value. Think of functions as a machine that takes some input, does some operations on it, and then produces an output. Here is an example of declaring a function:
函数是可重用的代码片段，用于执行特定任务或计算值。可以将函数想象成一个机器，它接收一些输入，对其进行一些操作，然后产生输出。以下是声明函数的示例：

function greet() {
  console.log("Hello, Jessica!");
}

In this example, we have declared a function called greet. Inside that function, we have a console.log that logs the message Hello, Jessica!. If we tried to run this code, we would not see the message appear in the console. This is because we need to call the function.
在这个示例中，我们声明了一个名为 greet 的函数。在该函数内部，有一个 console.log 用于记录消息 Hello, Jessica! 。如果我们尝试运行这段代码，将不会在控制台中看到消息显示。这是因为我们需要调用该函数。

A function call, or invocation, is when we actually use or execute the function. To call a function, you will need to reference the function name followed by a set of parentheses:
函数调用，或称为执行，是指我们实际使用或执行函数。要调用函数，需要引用函数名称，后跟一组括号：

```js
function greet() {
  console.log("Hello, Jessica!");
}

greet(); // "Hello, Jessica!"
```

Now the message of Hello, Jessica! will be logged to the console. But what if we wanted the message to say Hello, Nick! or Hello, Anna!? We don't want to write a new function each time we greet a different user. Instead, we can create a reusable function that uses function parameters and arguments.
现在消息 Hello, Jessica! 将会被记录到控制台。但如果我们想让消息显示 Hello, Nick! 或 Hello, Anna! 呢？我们不想每次问候不同的用户时都编写一个新的函数。相反，我们可以创建一个可重用的函数，该函数使用函数参数和实参。

Parameters act as placeholders for the values that will be passed to the function when it is called. They allow functions to accept input and work with that input. Arguments are the actual values passed to the function when it is called. Here is an updated version of the greet function that uses parameters and arguments:
参数充当占位符，用于存储在调用函数时传递给函数的值。它们允许函数接收输入并处理该输入。实参是在调用函数时传递给函数的实际值。这是使用参数和实参的 greet 函数的更新版本：

``` js
function greet(name) {
  console.log("Hello, " + name + "!");
}

greet("Alice"); // Hello, Alice!
greet("Nick"); // Hello, Nick!
```

The name serves as the parameter while the strings Alice and Nick serve as the arguments. Now we have a reusable function that can be used dozens of times throughout our code with different arguments.
name 作为参数，而字符串 Alice 和 Nick 作为实参。现在我们有一个可重用的函数，可以在整个代码中使用不同的实参多次。

When a function finishes its execution, it will always return a value. By default, the return value will be `undefined`. Here is an example:
当函数完成执行时，它总会返回一个值。默认情况下，返回值将是 undefined 。这里有一个示例：

function doSomething() {
    console.log("Doing something...");
}

let result = doSomething();
console.log(result); // undefined

If you need your function to return a specific value, then you will need to use the return statement. Here is an example of using a return statement to return the sum of two values:
如果你需要你的函数返回一个特定值，那么你需要使用 return 语句。这里是一个使用 return 语句返回两个值之和的例子：

``` js
function calculateSum(num1, num2) {
  return num1 + num2;
}

console.log(calculateSum(3, 4)); // 7
```

Often times you will be using the return statement, because you can use that value that was output from the function later on in your code.
通常情况下你会使用 return 语句，因为你可以使用函数输出的值在代码的其他部分。

So far, we've been working with named functions, but you can also create what's called an anonymous function. An anonymous function is a function without a name that can be assigned to a variable like this:
到目前为止，我们一直在处理命名函数，但你也可以创建一种称为匿名函数的东西。匿名函数是一个没有名称的函数，可以像这样赋值给一个变量：

``` js
const sum = function (num1, num2) {
  return num1 + num2;
};

console.log(sum(3, 4)); // 7
```

In this example, we have a const variable called sum and we are assigning it an anonymous function that returns the sum of num1 and num2. We are then able to call sum and pass in the numbers 3 and 4 to get the result of 7.
在这个例子中，我们有一个 const 变量叫做 sum ，我们把它赋值为一个匿名函数，这个函数返回 num1 和 num2 的和。然后我们能够调用 sum 并传入数字 3 和 4 来得到结果 7 。

Functions support default parameters, allowing you to set default values for parameters. These default values are used if the function is called without an argument for that parameter. Here's an example:
函数支持默认参数，允许您为参数设置默认值。如果函数调用时没有为该参数提供实参，则使用这些默认值。这里有一个例子：

``` js
function greetings(name = "Guest") {
  console.log("Hello, " + name + "!");
}

greetings(); // Hello, Guest!
greetings("Anna"); // Hello, Anna!
```

In this example, if no argument is provided for name, it defaults to Guest.
在这个例子中，如果为 name 没有提供参数，它将默认为 Guest 。

In summary, functions allow you to write reusable and organized code. They can take inputs (parameters), perform actions, and return outputs.
总而言之，函数允许你编写可重用和有组织的代码。它们可以接收输入（参数），执行操作，并返回输出。

## What Are Arrow Functions, and How Do They Work?
什么是箭头函数，以及它们是如何工作的？
In the previous lecture, you learned how to work with functions, which are reusable pieces of code that help make your code more modular, easier to maintain, and more efficient. All previous examples used the regular function syntax, like this:
在上一节课中，你学习了如何使用函数，这些是可重用的代码片段，它们有助于使你的代码更加模块化、易于维护和高效。所有之前的示例都使用了常规函数语法，如下所示：

function greetings(name) {
  console.log("Hello, " + name + "!");
}
But another way to write functions in JavaScript is to create an arrow function expression. Here is how you can refactor the previous example to use arrow function syntax instead:
但 JavaScript 中编写函数的另一种方式是创建箭头函数表达式。以下是如何将之前的示例重构为使用箭头函数语法：

const greetings = (name) => {
  console.log("Hello, " + name + "!");
};
In this revised example, we are creating a const variable called greetings and assigning it an anonymous function. Most of the syntax will look familiar to you except for the missing function keyword and the addition of the arrow (=>) between the name parameter and the function body. If your parameter list only has one parameter in it, then you can remove the parentheses like this:
在这个修改后的示例中，我们创建了一个名为 const 的变量 greetings 并将其分配给一个匿名函数。除了缺少 function 关键字和在 name 参数与函数体之间添加箭头（ => ）之外，大部分语法对你来说应该很熟悉。如果你的参数列表只有一个参数，那么你可以像这样去掉括号：

const greetings = name => {
  console.log("Hello, " + name + "!");
};
If your arrow function has no parameters, then you must use the parentheses like this:
如果你的箭头函数没有参数，那么你必须像这样使用括号：

const greetings = () => {
  console.log("Hello");
};
When first learning about functions, you had to wrap the function body in curly braces. But if your function body only contains a single line of code, you can remove the curly braces like this:
在学习函数时，你必须用大括号将函数体括起来。但如果你的函数体只包含一行代码，你可以像这样去掉大括号：

const greetings = name => console.log("Hello, " + name + "!");
It is important to note that removing the parentheses and curly braces for regular function syntax will not work. You will get errors if you tried to do something like this:
需要注意的是，对于普通函数语法，去掉括号和大括号是不行的。如果你尝试这样做，你会得到错误：

// This will produce syntax errors 
function greetings name console.log("Hello, " + name + "!");
These types of one line functions only work if you are using the arrow function syntax. Another key concept is the return statement. Here is an example of using the arrow function syntax to calculate the area:
这种类型的单行函数只有在使用箭头函数语法时才有效。另一个关键概念是 return 语句。这里有一个使用箭头函数语法计算面积的例子：

const calculateArea = (width, height) => {
  const area = width * height;
  return area;
};

console.log(calculateArea(5, 3)); // 15
We are creating a variable inside the function called area and then returning that variable. But we could clean up our code a bit and return the calculation itself:
我们在函数内部创建了一个名为 area 的变量，然后返回该变量。但我们可以稍微清理一下代码，直接返回计算结果：

const calculateArea = (width, height) => {
  return width * height;
}; 
If you tried to remove the curly braces and place the calculation on the same line, then you would get an Uncaught SyntaxError: Unexpected token 'return' message:
如果你尝试去掉花括号并将计算结果放在同一行，你就会得到一个 Uncaught SyntaxError: Unexpected token 'return' 错误信息：

const calculateArea = (width, height) => return width * height;
The reason why you are getting this error, is because you need to remove the return statement. When you remove that return statement, the error will disappear and the function will still implicitly return the calculation.
出现这个错误的原因是你需要去掉 return 语句。当你去掉那个 return 语句后，错误就会消失，函数仍然会隐式返回计算结果。

const calculateArea = (width, height) => width * height;
So when should you use the arrow function syntax? Well, it depends. Many developers use it consistently in their personal projects. However, when working on a team, the choice usually depends on whether the existing codebase uses regular functions or arrow functions. In future lectures, we'll cover when to use arrow functions and when to avoid them.
那么什么时候应该使用箭头函数语法呢？这取决于具体情况。许多开发者在个人项目中始终如一地使用它。然而，在团队协作时，选择通常取决于现有代码库是使用普通函数还是箭头函数。在未来的课程中，我们将讨论何时使用箭头函数以及何时避免使用它们。

## What Is Scope in Programming, and How Does Global, Local, and Block Scope Work?
编程中的作用域是什么，以及全局作用域、局部作用域和块作用域是如何工作的？
Scope in programming refers to the visibility and accessibility of variables in different parts of your code. It determines where variables can be accessed or modified. In JavaScript, understanding scope is crucial for writing clean, efficient, and bug-free code. There are three main types of scope: global scope, local scope, and block scope.
编程中的作用域指的是变量在代码不同部分的可见性和可访问性。它决定了变量可以在哪里被访问或修改。在 JavaScript 中，理解作用域对于编写干净、高效且无 bug 的代码至关重要。主要有三种作用域类型：全局作用域、局部作用域和块作用域。

Global scope is the outermost scope in a JavaScript program. Variables declared in the global scope are accessible from anywhere in your code, including within functions and blocks. These variables are often called global variables. While global variables can be convenient, they should be used sparingly as they can lead to naming conflicts and make your code harder to maintain. Here's an example of a global variable:
全局作用域是 JavaScript 程序中最外层的作用域。在全局作用域中声明的变量可以在代码的任何地方访问，包括在函数和块内部。这些变量通常被称为全局变量。虽然全局变量很方便，但应该谨慎使用，因为它们可能导致命名冲突并使代码更难维护。这里是一个全局变量的示例：

let globalVar = "I'm a global variable";

function printGlobalVar() {
    console.log(globalVar);
}

printGlobalVar(); // Output: "I'm a global variable"
In this example, globalVar is declared in the global scope and can be accessed inside the printGlobalVar function.
在这个示例中， globalVar 声明在全局作用域中，可以在 printGlobalVar 函数内部访问。

Local scope, on the other hand, refers to variables that are only accessible within a function. Here's an example of local scope:
局部作用域另一方面指的是仅在函数内部可访问的变量。以下是局部作用域的示例：

function greet() {
    let message = "Hello, local scope!";
    console.log(message);
}

greet(); // Output: "Hello, local scope!"
console.log(message); // This will throw an error
In this code, message is a local variable within the greet function. It can be used inside the function, but trying to access it outside the function will result in an error.
在这个代码中， message 是 greet 函数内的局部变量。它可以在函数内部使用，但尝试在函数外部访问它会导致错误。

Block scope is a concept introduced with the let and const keywords in ES6. A block is any code section within curly braces, {}, such as in if statements, for loops, or while loops. The concept of loops will be taught in an upcoming lecture.
块作用域是随着 ES6 中的 let 和 const 关键字引入的概念。块是指花括号 {} 内的任何代码段，例如在 if 语句、 for 循环或 while 循环中。循环的概念将在接下来的讲座中讲解。

Variables declared with let or const inside a block are only accessible within that block. Here's an example of block scope:
在块内部使用 let 或 const 声明的变量仅在该块内可访问。以下是块作用域的示例：

if (true) {
    let blockVar = "I'm in a block";
    console.log(blockVar); // Output: "I'm in a block"
}
console.log(blockVar); // This will throw an error
In this example, blockVar is only accessible within the if block. Trying to access it outside the block will result in an error. Understanding these different types of scope is essential for managing variable accessibility and avoiding unintended side effects in your code.
在这个例子中， blockVar 只能在 if 块内部访问。试图在块外部访问它会导致错误。理解这些不同类型的范围对于管理变量可访问性和避免代码中的意外副作用至关重要。

Global variables should be used sparingly, as they can lead to naming conflicts and make your code harder to maintain. Local variables help to keep different parts of your code isolated, which is especially useful in larger programs. Block scoping with let and const provides even finer control over variable accessibility, helping to prevent errors and make your code more predictable. Mastering these basic concepts of global, local, and block scope will provide a solid foundation for understanding more advanced topics.
全局变量应该谨慎使用，因为它们可能导致命名冲突并使代码更难维护。局部变量有助于将代码的不同部分隔离开来，这在大型程序中尤其有用。 let 和 const 的块级作用域提供了更精细的变量可访问性控制，有助于防止错误并使代码更具可预测性。掌握全局、局部和块级作用域的基本概念将为理解更高级的主题打下坚实的基础。
