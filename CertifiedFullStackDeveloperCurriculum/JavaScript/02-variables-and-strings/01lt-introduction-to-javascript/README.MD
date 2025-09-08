## Introduction to JavaScript

In these lectures, you will learn the fundamentals of JavaScript. Topics covered include, but are not limited to, variables, data types, how JavaScript interacts with HTML and CSS, strings, and much more.

## What Is JavaScript, and How Does It Work with HTML and CSS?

JavaScript is a powerful programming language that brings interactivity and dynamic behavior to websites.

JavaScript 是一种功能强大的编程语言，可为网站带来交互性和动态行为。

While HTML and CSS are markup languages used to structure content and style elements on a page, JavaScript goes beyond those by enabling more complex functionality, such as handling user input, animating elements, and even building full web applications.

虽然 HTML 和 CSS 是用于构建页面上的内容和样式元素的标记语言，但 JavaScript 通过支持更复杂的功能来超越这些语言，例如处理用户输入、动画元素，甚至构建完整的 Web 应用程序。

For example, when you click a button, submit a form, or hover over a menu, JavaScript determines how the page behaves.

例如，当您单击按钮、提交表单或将鼠标悬停在菜单上时，JavaScript 会确定页面的行为方式。

Here's an example of how these three work together:

以下是这三者如何协同工作的示例：

<!DOCTYPE html>
<html>
<head>
  <style>
    h1 {
      color: green;
    }
  </style>
</head>
<body>
  <h1>Hello, World!</h1>
  <button onclick="alert('Button clicked!')">Click me</button>
</body>
</html>

In this example, HTML is used to define the content: a heading (an h1 tag) and a button (the button tag).

在此示例中，HTML 用于定义内容：标题（h1 标签）和按钮（ 按钮标签）。

CSS is used to apply styles to the heading, such as making the text green. JavaScript is used to display an alert message when the button is clicked.

CSS 用于将样式应用于标题，例如将文本设为绿色。JavaScript 用于在单击按钮时显示警报消息。

To sum up, HTML provides structure, CSS adds styling, and JavaScript enables behavior, creating a complete and interactive web experience.

综上所述，HTML 提供结构，CSS 添加样式，JavaScript 支持行为，从而创建完整的交互式 Web 体验。

## What Is a Data Type, and What Are the Different Data Types in JavaScript?

In JavaScript, a data type refers to the kind of value a variable holds.

在 JavaScript 中，数据类型是指变量所包含的值类型。

A variable is a named container that stores a value of a specific data type, allowing you to reference and manipulate it throughout your code. Data types help the program understand the kind of data it's working with, whether it's a number, text, or something else.

变量是一个命名容器，用于存储特定数据类型的值，允许您在整个代码中引用和作它。数据类型有助于程序了解它正在处理的数据类型，无论是数字、文本还是其他内容。

JavaScript has several basic data types that you'll use in your programs. We'll explore each data type in greater detail in future lectures. For now, here is a brief introduction of the different data types in JavaScript.

JavaScript 有几种基本数据类型，您将在程序中使用它们。我们将在以后的讲座中更详细地探讨每种数据类型。现在，这里简要介绍一下 JavaScript 中的不同数据类型。

The first data type we will look at is the Number type.

我们将查看的第一个数据类型是 Number 类型。

A Number represents both integers and floating-point values. Examples of integers include 7, 19, and 90. Examples of floating point numbers include 3.14 and 5.2. A floating point number is a number with a decimal point.

数字表示整数和浮点值。整数的示例包括 7、19 和 90。浮点数的示例包括 3.14 和 5.2。浮点数是带有小数点的数字。

The next data type is a String.

下一个数据类型是 String。

A String is a sequence of characters, or text, enclosed in quotes. Here are two examples:

字符串是用引号括起来的字符或文本序列。下面是两个例子：

"Hello, world"
'JavaScript'

Another data type used in JavaScript is the Boolean type.

JavaScript 中使用的另一种数据类型是布尔类型。

A Boolean represents one of two possible values: true or false. You can use a boolean to check if a page is loading, or if a user is logged in or not.

布尔值表示两个可能的值之一：true 或 false。您可以使用布尔值来检查页面是否正在加载，或者用户是否已登录。

The next two data types used in JavaScript are undefined and null.

JavaScript 中使用的接下来的两种数据类型是 undefined 和 null。

undefined means a variable has been declared but hasn't been given a value yet. null means the variable has been intentionally set to "nothing" and does not hold any value. We will explore more on how this works in future lectures.

undefined 表示已声明变量但尚未被赋予值。null 表示变量已被故意设置为“无”并且不包含任何值。我们将在以后的讲座中更多地探讨这是如何运作的。

The next data type we will look at is the Object type.

我们将查看的下一个数据类型是 Object 类型。

An Object is a more complex data type that can hold collections of key-value pairs. Let's break this down. The key (also called a property name), is like a label for the data, whereas the value, is the actual data you want to store. Here is an example:

对象是一种更复杂的数据类型，可以保存键值对的集合。让我们来分解一下。键（也称为属性名称）类似于数据的标签，而值是您要存储的实际数据。这是一个例子：

let book = {
  title: "The Great Gatsby",
  author: "F. Scott Fitzgerald",
  year: 1925
};

In this object, title, author, and year are the keys (or property names). The Great Gatsby, F. Scott Fitzgerald, and 1925 are the corresponding values.

在此对象中，title、author 和 year 是键（或属性名称）。《 了不起的盖茨比》、《F·斯科特·菲茨杰拉德 》和 《1925》是相应的值。

Each key-value pair in an object is called a property. So we can say that this book object has three properties. This is just a basic introduction to objects and their properties. In future lectures, we'll go deeper into more advanced concepts.

对象中的每个键值对称为属性。所以我们可以说这个书对象有三个属性。这只是对对象及其属性的基本介绍。在以后的讲座中，我们将更深入地探讨更高级的概念。

The last two data types are the Symbol and BigInt data types.

最后两种数据类型是 Symbol 和 BigInt 数据类型。

A Symbol is a special type of value in JavaScript that is always unique and cannot be changed. It's often used to create unique labels or identifiers for properties:

符号是 JavaScript 中的一种特殊类型的值，它始终是唯一的且无法更改。它通常用于为属性创建唯一标签或标识符：

// Creating two symbols
const symbol1 = Symbol('mySymbol');
const symbol2 = Symbol('mySymbol');
console.log(symbol1 === symbol2); // Outputs: false

In this example, we create two symbols with the same description, but they are unique.

在此示例中，我们创建了两个具有相同描述的符号，但它们是唯一的。

BigInt is used for very large numbers that exceed the limit of the Number type:

BigInt 用于超过 Number 类型限制的非常大的数字：

const bigNumber = 1234567890123456789012345678901234567890n;
console.log(bigNumber);
// Outputs: 1234567890123456789012345678901234567890n

In this example, we create a BigInt by adding n at the end of a very large number.

在这个例子中，我们通过在一个非常大的数字的末尾加上 n 来创建一个 BigInt。

Understanding these data types helps you handle and work with various kinds of data in your programs, as each type has its own characteristics and behaviors.

了解这些数据类型有助于处理和处理程序中的各种数据，因为每种类型都有自己的特征和行为。

## What Are Variables, and What Are Guidelines for Naming JavaScript Variables?
什么是变量，命名 JavaScript 变量的准则是什么？
In JavaScript, variables act as containers for storing data that you can access and modify throughout your program.
在 JavaScript 中，变量充当存储数据的容器，您可以在整个程序中访问和修改这些数据。

You can think of variables as boxes that hold values. With variables, you can keep track of things like numbers or text and refer to these values whenever you need them in your program.
您可以将变量视为保存值的框。使用变量，您可以跟踪数字或文本等内容，并在程序中需要时引用这些值。

One way to declare a variable in JavaScript, is to use the let keyword. You will learn more about the let keyword as well as other ways to declare variables in future lectures.
在 JavaScript 中声明变量的一种方法是使用 let 关键字。您将在以后的讲座中了解有关 let 关键字以及声明变量的其他方法的更多信息。

Here's an example of using let to declare a variable called age:
以下是使用 let 声明名为 age 的变量的示例：

let age;
Right now, the age variable does not have a value assigned to it. To assign a value to a variable you will need to use the assignment operator like this:
目前， 年龄变量没有分配值。要为变量赋值，您需要使用赋值运算符，如下所示：

let age = 25;
The assignment operator looks like an equals sign (=) but it doesn't check for equality. You'll learn about the correct operators for checking equality in future lectures.
赋值运算符看起来像等号 （=），但它不检查相等性。您将在以后的讲座中了解检查相等性的正确运算符。

The assignment operator is used to assign a value to a variable. This process of assigning a value to a variable is known as initialization.
赋值运算符用于为变量赋值。为变量赋值的过程称为初始化。

One advantage of using the let keyword to declare variables is that you can reassign values to them. In programming, reassignment means giving a new value to a variable that already has one.
使用 let 关键字声明变量的一个优点是可以为它们重新分配值。在编程中，重新赋值意味着为已经具有新值的变量赋予一个新值。

Here is an example of reassigning the value for the age variable:
以下是重新分配年龄变量值的示例：

age = 30;
Now the age variable holds the value of 30. Notice that the let keyword wasn't needed again because the age variable was already declared, so there's no need to declare it a second time.
现在，age 变量的值为 30。请注意，由于已经声明了 age 变量，因此不再需要 let 关键字，因此无需再次声明它。

When using reassignment, you only need to reference the variable name. Reassignment is useful because it allows you to update and change the value stored in a variable as your program runs. A good example of this would be updating points in a game.
使用重赋值时，只需引用变量名称即可。重新赋值很有用，因为它允许您在程序运行时更新和更改存储在变量中的值。一个很好的例子是在游戏中更新积分。

Naming variables may seem straightforward, but there are some rules and best practices to ensure your code is readable and functional.
命名变量可能看起来很简单，但有一些规则和最佳实践可以确保您的代码可读且功能正常。

Your variable names should describe what the data represents. For example, instead of using a name like x, a more descriptive name such as age or points makes your code easier to understand.
变量名称应描述数据所代表的内容。例如，不要使用像 x 这样的名称，而使用更具描述性的名称（例如年龄或分数 ）可以使您的代码更易于理解。

Variables in JavaScript must begin with a letter, an underscore (_), or a dollar sign ($). They cannot start with a number.
JavaScript 中的变量必须以字母、下划线 （_） 或美元符号 （$） 开头。他们不能以数字开头。

Variable names are case-sensitive, meaning the word age in all lowercase and the word Age with a capital A are considered different variables.
变量名称区分大小写，这意味着所有小写的单词 age 和大写 A 的单词 age 被视为不同的变量。

This is why it's important to stick with a consistent naming convention like camelCase. camelCase is where the first word is all lowercase and each subsequent word starts with an uppercase letter.
这就是为什么坚持一致的命名约定（如驼峰命名法）很重要的原因。驼峰命名法是第一个单词全部小写，后续每个单词都以大写字母开头。

Here is an example of using the camelCase naming convention for a variable:
以下是对变量使用驼峰命名法约定的示例：

let thisIsCamelCase;
There are certain keywords in JavaScript that you cannot use as variable names, such as let, const, function, or return, as they are reserved for the language itself.
JavaScript 中的某些关键字不能用作变量名称，例如 let、const、function 或 return，因为它们是为语言本身保留的。

You should also avoid using special characters like exclamation points (!) or at (@) symbols, in your variable names. It is best to keep variable names readable by using letters, numbers, underscores, or dollar signs.
您还应该避免在变量名称中使用特殊字符，例如感叹号 （！） 或 at （@） 符号。最好使用字母、数字、下划线或美元符号使变量名称保持可读性。

By following these guidelines, your code will be cleaner and more manageable as it grows in complexity.
通过遵循这些准则，您的代码将随着复杂性的增加而变得更干净、更易于管理。

## How Do let and const Work Differently When It Comes to Variable Declaration, Assignment, and Reassignment?
在变量声明、赋值和重新赋值方面，let 和 const 的工作方式有何不同？
When working with JavaScript, you'll often declare variables to store data that you plan to use throughout your program.
使用 JavaScript 时，您经常会声明变量来存储您计划在整个程序中使用的数据。

In modern JavaScript, let and const are the preferred ways to declare variables, but they differ in how they handle value assignment and reassignment.
在现代 JavaScript 中，let 和 const 是声明变量的首选方法，但它们在处理值赋值和重赋的方式上有所不同。

In this lecture, we'll explore how let and const differ in variable declaration, assignment, and reassignment.
在本讲座中，我们将探讨 let 和 const 在变量声明、赋值和重赋中有何不同。

The let keyword allows you to declare variables that can be updated or reassigned later. You can think of let as a flexible container – once you've stored a value in it, you can change that value as needed throughout your program.
let 关键字允许您声明以后可以更新或重新分配的变量。你可以把 let 看作是一个灵活的容器——一旦你在其中存储了一个值，你就可以在整个程序中根据需要更改该值。

Here's an example of declaring and assigning a variable with let:
以下是使用 let 声明和赋值变量的示例：

let score = 10;
In this case, the variable score is declared and assigned the value 10. If you want to update the value later, you can easily do that:
在这种情况下，将声明变量分数并分配值 10。如果您想稍后更新该值，您可以轻松地执行以下作：

score = 20;
Now, score holds the value 20. This makes let particularly useful when you know the value of a variable will change as your program runs.
现在，score 保持值 20。当您知道变量的值会随着程序的运行而变化时， 这使得 let 特别有用。

On the other hand, const is used to declare variables that are constant. Once you assign a value to a variable declared with const, you cannot reassign it.
另一方面，const 用于声明常量变量。将值赋值给用 const 声明的变量后，就无法重新赋值。

This makes const ideal for values that you don't want to change accidentally during the execution of your program.
这使得 const 非常适合您不想在程序执行期间意外更改的值。

Here's an example of declaring and assigning a variable with const:
以下是使用 const 声明和赋值变量的示例：

const maxScore = 100;
Once maxScore is assigned the value 100, it cannot be changed:
一旦 maxScore 被分配了值 100，就无法更改它：

maxScore = 200; // This will result in an error
Trying to reassign a value to a const variable will throw an error in your JavaScript console, as const variables are immutable once they are assigned.
尝试将值重新分配给 const 变量会在 JavaScript 控制台中抛出错误，因为 const 变量一旦被赋值就不可变。

You can declare a let variable without immediately assigning it a value, and you can assign it a value later:
您可以声明一个 let 变量，而无需立即为其赋值，并且可以稍后为其赋值：

let age;
age = 25;
Variables declared with const must be assigned a value at the time of declaration. If you try to declare a const variable without assigning it a value, you will get an error:
使用 const 声明的变量必须在声明时分配一个值。如果您尝试声明一个 const 变量而不为其赋值，您将收到一个错误：

const age; // Error: Missing initializer in const declaration
You should use let when you need to declare variables that will be reassigned later. For example, tracking a changing score or updating a value over time in your program.
当你需要声明稍后将重新分配的变量时，你应该使用 let。例如，跟踪不断变化的分数或随时间推移更新程序中的值。

Use const when you want to declare variables that should remain constant, like configuration values or settings that shouldn't be changed accidentally.
当您想要声明应保持不变的变量时，请使用 const，例如不应意外更改的配置值或设置。

You can also use the var keyword, but it's not as recommended anymore. The var is kind of like let, except it has a wider scope, which is more likely to cause problems in your program.
您也可以使用 var 关键字，但不再推荐它。var 有点像 let，只是它的作用域更广，这更有可能在程序中引起问题。

## What Is a String in JavaScript, and What Is String Immutability?
什么是 JavaScript 中的字符串，什么是字符串不变性？
In JavaScript, a string is a sequence of characters used to represent text data. Strings are one of the primitive data types in the language, along with numbers, booleans, null, and undefined.
在 JavaScript 中，字符串是用于表示文本数据的字符序列。字符串是该语言中的原始数据类型之一，还有数字、布尔值、 空值和未定义值 。

To create a string in JavaScript, you can use single quotes ('), or double quotes (").
要在 JavaScript 中创建字符串，可以使用单引号 （'） 或双引号 （“）。

Here is an example of creating two variables that hold string values:
下面是创建两个保存字符串值的变量的示例：

let singleQuotes = 'This is a string';
let doubleQuotes = "This is also a string";
Even though you can use single or double quotes to create strings, it's important to be consistent. If a string begins with a single quote, it must also end with a single quote.
尽管您可以使用单引号或双引号来创建字符串，但保持一致很重要。如果字符串以单引号开头，则它也必须以单引号结尾。

The same applies to double quotes. The following example will throw an error because it starts with a double quote and ends with a single quote:
这同样适用于双引号。以下示例将引发错误，因为它以双引号开头，以单引号结尾：

const improperStr = "Do not do this';
Another thing to take into account is that strings are immutable. In programming, immutability means that once something is created, it cannot be changed. So, when you create a string, you can't change its characters directly. Instead, you would create a new string if you want to make changes.
另一件需要考虑的事情是字符串是不可变的。在编程中，不变性意味着某物一旦被创建，就无法更改。因此，当您创建字符串时，您无法直接更改其字符。相反，如果要进行更改，则需要创建一个新字符串。

Here is an example of assigning a new string to a developer variable:
下面是将新字符串分配给开发人员变量的示例：

let developer = "Jessica";
developer = "Quincy";
Since strings are immutable, we can't update the first string directly. That is why we are assigning a new string to the developer variable.
由于字符串是不可变的，因此我们不能直接更新第一个字符串。这就是为什么我们要为 developer 变量赋值一个新字符串。

Strings are an important part of programming, and in future lectures, you will learn advanced techniques for manipulating them and harnessing their full potential to create dynamic and interactive applications.
字符串是编程的重要组成部分，在以后的讲座中，您将学习作字符串并充分利用其潜力来创建动态和交互式应用程序的高级技术。

## What Is String Concatenation, and How Can You Concatenate Strings with Variables?
什么是字符串串联，如何将字符串与变量连接起来？
In JavaScript, working with text is an essential part of coding, and often, you'll need to combine or join pieces of text together. This process is called string concatenation.
在 JavaScript 中，处理文本是编码的重要组成部分，通常，您需要将文本片段组合或连接在一起。此过程称为字符串串联。

In this lecture, we'll focus on how string concatenation works, specifically using the + operator, the += operator, and the concat() method.
在本讲座中，我们将重点介绍字符串串联的工作原理，特别是使用 + 运算符、+= 运算符和 concat（） 方法。

The + operator is one of the simplest and most frequently used methods to concatenate strings. It allows you to join multiple strings or combine strings with variables that hold text.
+ 运算符是连接字符串的最简单和最常用的方法之一。它允许您连接多个字符串或将字符串与保存文本的变量组合在一起。

Here's an example:  这是一个例子：

let firstName = "John";
let lastName = "Doe";

let fullName = firstName + " " + lastName; // John Doe
In this example, we used the + operator to concatenate the firstName and lastName variables along with a space (" ") to create the full name.
在此示例中，我们使用 + 运算符将 firstName 和 lastName 变量与空格 （“ ”） 连接起来以创建全名。

One disadvantage of using the + operator for string concatenation is that it can lead to spacing issues if you don't carefully manage the spacing between the concatenated strings.
使用 + 运算符进行字符串串联的一个缺点是，如果不仔细管理串联字符串之间的间距，可能会导致间距问题。

Here is an example where a space is missing:
下面是一个缺少空格的示例：

let firstName = "John";
let lastName = "Doe";

let fullName = firstName + lastName; // "JohnDoe"
Whenever you use the + operator to concatenate strings, it is important to double check for any potential spacing issues.
每当您使用 + 运算符连接字符串时，请务必仔细检查是否有任何潜在的间距问题。

If you need to add or append to an existing string, then you can use the += operator. This is helpful when you want to build upon a string by adding more text to it over time.
如果需要添加或追加到现有字符串，则可以使用 += 运算符。当您想要通过随着时间的推移向字符串添加更多文本来构建字符串时，这很有用。

Here's an example of appending one string to another using the += operator:
以下是使用 += 运算符将一个字符串附加到另一个字符串的示例：

let greeting = 'Hello';
greeting += ', John!';

// greeting is now the string Hello, John!
It is important to remember that strings are immutable which means once a string is created you can not alter it.
重要的是要记住，字符串是不可变的，这意味着一旦创建了字符串，就无法更改它。

In this case, the original string of Hello is not modified. Instead, greeting now references the new string of Hello, John!
在这种情况下，不会修改 Hello 的原始字符串。相反，问候语现在引用了新字符串 Hello， John！

Another way you can concatenate strings is to use the concat() method.
连接字符串的另一种方法是使用 concat（） 方法。

Before we begin learning about the concat() method, it is important to first understand what a method and a function are at a higher level.
在我们开始学习 concat（） 方法之前，首先了解更高级别的方法和函数是什么非常重要。

In programming, a function is a reusable block of code that performs a specific task and can be called with various inputs. A method, on the other hand, is a type of function that is associated with an object, meaning it operates on the data contained within that object.
在编程中，函数是执行特定任务的可重用代码块，并且可以通过各种输入调用。另一方面，方法是一种与对象关联的函数类型，这意味着它对该对象中包含的数据进行作。

In future lectures, we will dive much deeper into how functions, objects, and methods work in JavaScript. But for now, it is important to understand that JavaScript has dozens of methods you can use, like the concat() method.
在以后的讲座中，我们将更深入地探讨函数、对象和方法在 JavaScript 中的工作原理。但就目前而言，重要的是要了解 JavaScript 有数十种您可以使用的方法，例如 concat（） 方法。

Here's an example of using the concat() method to join two strings together:
以下是使用 concat（） 方法将两个字符串连接在一起的示例：

let str1 = 'Hello';
let str2 = 'World';

let result = str1.concat(' ', str2); // Hello World
In this example, we use the concat() method to join str1, a space (' '), and str2 into a single string.
在此示例中，我们使用 concat（） 方法将 str1、空格 （' '） 和 str2 连接成一个字符串。

To conclude, + operator is best for simple concatenation, especially when you need to combine a few strings or variables.
总而言之，+ 运算符最适合简单串联，尤其是当您需要组合几个字符串或变量时。

The += operator is useful when building up a string step by step or appending new content to an existing string variable.
+= 运算符在逐步构建字符串或将新内容附加到现有字符串变量时非常有用。

Finally, the concat() method is beneficial when you need to concatenate multiple strings together.
最后，当您需要将多个字符串连接在一起时，concat（） 方法非常有用。

## What Is console.log Used For, and How Does It Work?
console.log 有什么用途，它是如何工作的？
In JavaScript, console.log() is a simple yet powerful tool used to display messages or output information to the browser's console. It's mostly used by developers to debug and inspect code while working on their programs.
在 JavaScript 中，console.log（） 是一个简单但功能强大的工具，用于显示消息或将信息输出到浏览器的控制台。它主要由开发人员在处理程序时用于调试和检查代码。

You can use console.log() to log text or variables to the console and ensure your code is running correctly.
您可以使用 console.log（） 将文本或变量记录到控制台，并确保您的代码正确运行。

To use console.log(), you call the method with the value or message you want to output inside the parentheses. Here are some examples:
要使用 console.log（）， 您需要在括号内使用要输出的值或消息调用该方法。这里有些例子：

console.log("Hello, world!");

let num = 5;
console.log(num);
The first example prints Hello, world! in the browser's console, while the second example prints the value 5.
第一个示例在浏览器的控制台中打印 Hello， world！，而第二个示例打印值 5。

Here is another example of working with console.log():
这是使用 console.log（） 的另一个示例：

let name = "Alice";
console.log("Hello, " + name + "!"); // Outputs: Hello, Alice!
The console.log() method helps you monitor your code as it runs, making it easier to spot mistakes and understand how your program behaves.
console.log（） 方法可帮助您在代码运行时监控代码，从而更轻松地发现错误并了解程序的行为方式。

## What Is the Role of Semicolons in JavaScript, and Programming in General?
分号在 JavaScript 和一般编程中的作用是什么？
In JavaScript, and many other programming languages, semicolons help delineate statements and improve code readability.
在 JavaScript 和许多其他编程语言中，分号有助于描述语句并提高代码可读性。

In JavaScript, a semicolon (;) is used to indicate the end of a statement.
在 JavaScript 中，分号 （;） 用于指示语句的结尾。

Just as a period (.) marks the end of a sentence in English, a semicolon signifies the end of an executable line of code. This allows the JavaScript engine to distinguish between separate commands.
正如句点 （.） 在英语中标记句子的结尾一样，分号表示可执行代码行的结尾。这允许 JavaScript 引擎区分单独的命令。

For example:  例如：

let variableOne = 5;  // Declare a variable and assign a value
let variableTwo = 10; // Declare another variable and assign a value
In this code, the semicolons at the end of each line mark the end of each statement. Without them, the JavaScript engine might have trouble interpreting where one statement ends and another begins.
在此代码中，每行末尾的分号标记每个语句的末尾。如果没有它们，JavaScript 引擎可能无法解释一个语句的结束位置和另一个语句的开始位置。

Semicolons are primarily used to mark the end of a statement. This helps the JavaScript engine understand the separation of individual instructions, which is important for correct execution.
分号主要用于标记语句的结尾。这有助于 JavaScript 引擎理解各个指令的分离，这对于正确执行非常重要。

let a = 1;   // Statement ends here
let b = 2;   // Another statement starts here
While JavaScript has Automatic Semicolon Insertion (ASI) that can add semicolons automatically, explicitly including them improves code clarity and helps prevent errors that may arise from unexpected ASI behavior.
虽然 JavaScript 具有自动分号插入 （ASI），可以自动添加分号，但显式包含分号可以提高代码清晰度，并有助于防止意外 ASI 行为可能引起的错误。

Semicolons are used in many programming languages, including C, C++, and Java.
分号用于许多编程语言，包括 C、C++ 和 Java。

Semicolons mark the end of statements or instructions, helping the compiler or interpreter parse the code correctly. A compiler translates high-level programming language code into machine-readable code, which creates an executable file.
分号标记语句或指令的结尾，帮助编译器或解释器正确解析代码。编译器将高级编程语言代码转换为机器可读代码，从而创建可执行文件。

By clearly delineating statements, semicolons contribute to the readability and maintainability of code. Semicolons help prevent ambiguities in code execution and ensure that statements are correctly terminated.
通过清楚地描述语句，分号有助于提高代码的可读性和可维护性。分号有助于防止代码执行中的歧义并确保语句正确终止。

Semicolons are a fundamental part of JavaScript and many other programming languages.
分号是 JavaScript 和许多其他编程语言的基本组成部分。

They mark the end of statements, improve code readability, and help avoid errors related to Automatic Semicolon Insertion.
它们标记语句的结尾，提高代码可读性，并有助于避免与自动分号插入相关的错误。

By understanding and using semicolons properly, you can write more reliable and maintainable code.
通过正确理解和使用分号，您可以编写更可靠和可维护的代码。

## What Are Comments in JavaScript, and When Should You Use Them?
JavaScript 中的注释是什么，什么时候应该使用它们？
Comments in programming are used to provide additional context for the code or leave notes for yourself and others.
编程中的注释用于为代码提供额外的上下文或为自己和他人留下注释。

Comments are lines or blocks of text that are ignored by the JavaScript engine when your code is executed. They are there solely for the benefit of people reading the code, whether that's you or someone else.
注释是执行代码时 JavaScript 引擎忽略的行或文本块。它们的存在只是为了阅读代码的人的利益，无论是你还是其他人。

JavaScript provides two ways to add comments to your code: single-line comments and multi-line comments.
JavaScript 提供了两种向代码添加注释的方法：单行注释和多行注释。

Single-line comments are created using two forward slashes (//). Here is an example:
单行注释是使用两个正斜杠 （） 创建的。这是一个例子：

// I am a single line comment in JavaScript
This type of comment is great for brief explanations or clarifications.
这种类型的评论非常适合简短的解释或澄清。

Here is a real world example from the freeCodeCamp curriculum project files:
以下是 freeCodeCamp 课程项目文件中的一个真实示例：

// This is to allow English to build without having to download the i18n files.
// It fails when trying to resolve the i18n-curriculum path if they don't exist.
const curriculumLocale = process.env.CURRICULUM_LOCALE ?? 'english';
const I18N_CURRICULUM_DIR = path.resolve(
  __dirname,
  curriculumLocale === 'english' ? '.' : 'i18n-curriculum/curriculum'
);
Do not worry about trying to understand what the code is actually doing because it is more advanced than what you have learned so far. Instead, focus on the comment left by the developer. This comment provides important context for why this code exists.
不要担心试图理解代码的实际作用，因为它比您迄今为止所学的更高级。相反，请关注开发人员留下的评论。此注释提供了此代码存在原因的重要上下文。

Comments like this are important for those working on teams for two reasons:
像这样的评论对于那些在团队中工作的人来说很重要，原因有两个：

Other developers working on the project will understand the purpose of this code.
从事该项目的其他开发人员将了解此代码的用途。

It helps prevent unnecessary changes or deletions without consulting the team, which could lead to bugs or issues.
它有助于防止在未咨询团队的情况下进行不必要的更改或删除，这可能会导致错误或问题。

Another type of comment is multi-line comments. Here is the basic syntax:
另一种类型的注释是多行注释。这是基本语法：

/*
 I am a multiline comment.
 This is helpful for longer explanations.
*/
Multi-line comments are useful when you need to write longer descriptions, explanations, or notes in your code.
当您需要在代码中编写更长的描述、解释或注释时，多行注释非常有用。

Let's take another look at the freeCodeCamp curriculum project files to see how multiline comments can be used in the real world.
让我们再看看 freeCodeCamp 课程项目文件，看看如何在现实世界中使用多行注释。

/* Since there can be more than one way to complete a certification (using the
legacy curriculum or the new one, for instance), we need a certification
field to track which certification this belongs to. */
const dupeCertifications = [
  {
    certification: 'responsive-web-design',
    dupe: '2022/responsive-web-design'
  }
];
const hasDupe = dupeCertifications.find(
  cert => cert.dupe === meta.superBlock
);
Just like before, ignore all of the JavaScript code because it uses concepts that haven't been taught yet. Instead, focus on the comment left by the developer.
就像以前一样，忽略所有 JavaScript 代码，因为它使用了尚未教授的概念。相反，请关注开发人员留下的评论。

A developer on the team, or even a new contributor working on the project, can understand why this piece of code is here and have the full context before working on this area of the project.
团队中的开发人员，甚至是从事该项目的新贡献者，都可以理解为什么这段代码会出现在这里，并在处理项目的这一领域之前了解完整的上下文。

While comments are useful in programming, it is important to avoid over-commenting. You don't need to comment on every single line of code, especially if the code is straightforward and self-explanatory.
虽然注释在编程中很有用，但重要的是要避免过度注释。您不需要对每一行代码进行注释，尤其是当代码简单明了且不言自明的情况下。

Here is an example of using comments to explain the obvious:
下面是一个使用注释来解释显而易见的示例：

// This code uses the const keyword to create a new variable called price.
// We are assigning the number 10 to the price variable.
const price = 10;
In this situation, there is no need to add any comments here because the code is self-explanatory. The goal is to enhance readability, not clutter the code with unnecessary explanations.
在这种情况下，无需在此处添加任何注释，因为代码是不言自明的。目标是提高可读性，而不是用不必要的解释使代码变得混乱。

If you want to add comments to your personal projects as you are learning to code, that is fine. But once you start working on real world projects with other developers, it is important not to use comments for code that is self-explanatory.
如果您想在学习编码时为您的个人项目添加注释，那很好。但是，一旦您开始与其他开发人员一起处理实际项目，重要的是不要对不言自明的代码使用注释。

It is also important not to use comments to help explain away confusing, overly complicated, or poorly written code. In those situations, it is best to refactor, or change, your code so other developers will better understand what is going on.
同样重要的是，不要使用注释来帮助解释令人困惑、过于复杂或写得不好的代码。在这些情况下，最好重构或更改您的代码，以便其他开发人员更好地了解正在发生的事情。

Comments are powerful tools for documenting your code and making it easier to understand. You should use comments to provide context or leave notes for yourself and others.
注释是记录代码并使其更易于理解的强大工具。您应该使用评论来提供上下文或为自己和他人留下笔记。

