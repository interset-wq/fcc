# JavaScript Variables and Data Types Review 变量和数据类型

## Working with HTML, CSS, and JavaScript

While HTML and CSS provide website structure, JavaScript brings interactivity to websites by enabling complex functionality, such as handling user input, animating elements, and even building full web applications.

虽然 HTML 和 CSS 提供网站结构，但 JavaScript 通过启用复杂的功能（例如处理用户输入、动画元素，甚至构建完整的 Web 应用程序）为网站带来交互性。

## Data Types in JavaScript 数据类型

Data types help the program understand the kind of data it's working with, whether it's a number, text, or something else.

数据类型有助于程序了解它正在处理的数据类型，无论是数字、文本还是其他内容。

`number`: A number represents both integers and floating-point values. Examples of integers include 7, 19, and 90.

数字 ：数字表示整数和浮点值。整数的示例包括 7、19 和 90。

Floating point: A floating point number is a number with a decimal point. Examples include 3.14, 0.5, and 0.0001.

浮点 ：浮点数是带小数点的数字。示例包括 3.14、0.5 和 0.0001。

`string`: A string is a sequence of characters, or text, enclosed in quotes. "I like coding" and 'JavaScript is fun' are examples of strings.

字符串 ：字符串是用引号括起来的字符或文本序列。“我喜欢编码” 和 “JavaScript 很有趣” 是字符串的例子。

`boolean`: A boolean represents one of two possible values: true or false. You can use a boolean to represent a condition, such as isLoggedIn = true.

布尔值 ：布尔值表示两个可能的值之一：true 或 false。可以使用布尔值来表示条件，例如 isLoggedIn = true。

`undefined` and `null`: An undefined value is a variable that has been declared but not assigned a value. A null value is an empty value, or a variable that has intentionally been assigned a value of null.

未定义和空值： 未定义值是已声明但未分配值的变量。 空值是一个空值，或者一个有意被分配了 null 值的变量。

`object`: An object is a collection of key-value pairs. The key is the property name, and the value is the property value.

对象 ：对象是键值对的集合。键是属性名称，值是属性值。

Here, the pet object has three properties or keys: name, age, and type. The values are Fluffy, 3, and dog, respectively.

在这里，pet 对象具有三个属性或键：name、age 和 type。这些值分别为 Fluffy、3 和 dog。

    let pet = {
      name: "Fluffy",
      age: 3,
      type: "dog"
    };

`symbol`: The Symbol data type is a unique and immutable value that may be used as an identifier for object properties.

符号 ：符号数据类型是一个唯一且不可变的值，可用作对象属性的标识符。

In this example below, two symbols are created with the same description, but they are not equal.

在下面的示例中，创建了两个具有相同描述的符号，但它们不相等。

    const crypticKey1= Symbol("saltNpepper");
    const crypticKey2= Symbol("saltNpepper");
    console.log(crypticKey1 === crypticKey2); // false

BigInt: When the number is too large for the Number data type, you can use the BigInt data type to represent integers of arbitrary length.

BigInt：当数字对于 Number 数据类型来说太大时，您可以使用 BigInt 数据类型来表示任意长度的整数。

By adding an n to the end of the number, you can create a BigInt.

通过在数字末尾添加一个 n，您可以创建一个 BigInt。

    const veryBigNumber = 1234567890123456789012345678901234567890n;

## Variables in JavaScript 变量

Variables can be declared using the let keyword.

可以使用 let 关键字声明变量。

let cityName;

To assign a value to a variable, you can use the assignment operator =.

要为变量赋值，可以使用赋值运算符 =。

cityName = "New York";

Variables declared using let can be reassigned a new value.

使用 let 声明的变量可以重新分配一个新值。

cityName = "Los Angeles";
console.log(cityName); // Los Angeles

Apart from let, you can also use const to declare a variable. However, a const variable cannot be reassigned a new value.

除了 let，您还可以使用 const 来声明变量。但是，不能重新分配 const 变量的新值。

const cityName = "New York";
cityName = "Los Angeles"; // TypeError: Assignment to constant variable.

Variables declared using const find uses in declaring constants, that are not allowed to change throughout the code, such as PI or MAX_SIZE.

使用 const find 声明的变量在声明常量时使用，这些常量不允许在整个代码中更改，例如 PI 或 MAX_SIZE。

## Variable Naming Conventions 变量命名规范

Variable names should be descriptive and meaningful.

变量名称应该具有描述性和意义。

Variable names should be camelCase like cityName, isLoggedIn, and veryBigNumber.

变量名称应为驼峰命名法，如 cityName、isLoggedIn 和 veryBigNumber。

Variable names should not start with a number. They must begin with a letter, _, or $.

变量名称不应以数字开头。它们必须以字母 _ 或 $ 开头。

Variable names should not contain spaces or special characters, except for _ and $.

变量名称不应包含空格或特殊字符， 但 _ 和 $ 除外。

Variable names should not be reserved keywords.

变量名称不应是保留关键字。

Variable names are case-sensitive. age and Age are different variables.

变量名称区分大小写。age 和 age 是不同的变量。

## Strings and String immutability in JavaScript 字符串是不可变类型

Strings are sequences of characters enclosed in quotes. They can be created using single quotes and double quotes.

字符串是用引号括起来的字符序列。可以使用单引号和双引号创建它们。

let correctWay = 'This is a string';
let alsoCorrect = "This is also a string";

Strings are immutable in JavaScript. This means that once a string is created, you cannot change the characters in the string. However, you can still reassign strings to a new value.

字符串在 JavaScript 中是不可变的。这意味着一旦创建了字符串，就无法更改字符串中的字符。但是，您仍然可以将字符串重新分配给新值。

let firstName = "John";
firstName = "Jane"; // Reassigning the string to a new value

## String Concatenation in JavaScript 字符串拼接

Concatenation is the process of joining multiple strings or combining strings with variables that hold text. The + operator is one of the simplest and most frequently used methods to concatenate strings.

串联是连接多个字符串或将字符串与保存文本的变量组合的过程。+ 运算符是连接字符串的最简单和最常用的方法之一。

    let studentName = "Asad";
    let studentAge = 25;
    let studentInfo = studentName + " is " + studentAge + " years old.";
    console.log(studentInfo); // Asad is 25 years old.

If you need to add or append to an existing string, then you can use the += operator. This is helpful when you want to build upon a string by adding more text to it over time.

如果需要添加或追加到现有字符串，则可以使用 += 运算符。当您想要通过随着时间的推移向字符串添加更多文本来构建字符串时，这很有用。

    let message = "Welcome to programming, ";
    message += "Asad!";
    console.log(message); // Welcome to programming, Asad!

Another way you can concatenate strings is to use the concat() method. This method joins two or more strings together.

连接字符串的另一种方法是使用 concat（） 方法。此方法将两个或多个字符串连接在一起。

    let firstName = "John";
    let lastName = "Doe";
    let fullName = firstName.concat(" ", lastName);
    console.log(fullName); // John Doe

## Logging Messages with console.log() 控制台日志

The console.log() method is used to log messages to the console. It's a helpful tool for debugging and testing your code.

console.log（） 方法用于将消息记录到控制台。它是调试和测试代码的有用工具。

console.log("Hello, World!");
// Output: Hello, World!

## Semicolons in JavaScript 分号

Semicolons are primarily used to mark the end of a statement. This helps the JavaScript engine understand the separation of individual instructions, which is crucial for correct execution.

分号主要用于标记语句的结尾。这有助于 JavaScript 引擎理解各个指令的分离，这对于正确执行至关重要。

let message = "Hello, World!"; // first statement ends here
let number = 42; // second statement starts here

Semicolons help prevent ambiguities in code execution and ensure that statements are correctly terminated.

分号有助于防止代码执行中的歧义并确保语句正确终止。

## Comments in JavaScript 注释

Any line of code that is commented out is ignored by the JavaScript engine. Comments are used to explain code, make notes, or temporarily disable code.

JavaScript 引擎会忽略任何注释掉的代码行。注释用于解释代码、做笔记或暂时禁用代码。

Single-line comments are created using //.

单行注释是使用 创建的。

// This is a single-line comment and will be ignored by the JavaScript engine

Multi-line comments are created using /* to start the comment and */ to end the comment.

使用 /* 开始注释， 使用 */ 结束注释创建多行注释。

/*
This is a multi-line comment.
It can span multiple lines.
*/

## JavaScript as a Dynamically Typed Language 动态类型

JavaScript is a dynamically typed language, which means that you don't have to specify the data type of a variable when you declare it. The JavaScript engine automatically determines the data type based on the value assigned to the variable.

JavaScript 是一种动态类型语言，这意味着您在声明变量时不必指定变量的数据类型。JavaScript 引擎根据分配给变量的值自动确定数据类型。

let error = 404; // JavaScript treats error as a number
error = "Not Found"; // JavaScript now treats error as a string

Other languages, like Java, that are not dynamically typed would result in an error:

其他非动态类型化的语言（如 Java）将导致错误：

int error = 404; // value must always be an integer
error = "Not Found"; // This would cause an error in Java

## Using the `typeof` Operator

The typeof operator is used to check the data type of a variable. It returns a string indicating the type of the variable.

typeof 运算符用于检查变量的数据类型。它返回一个指示变量类型的字符串。

let age = 25;
console.log(typeof age); // "number"

let isLoggedIn = true;
console.log(typeof isLoggedIn); // "boolean"

However, there's a well-known quirk in JavaScript when it comes to null. The typeof operator returns "object" for null values.

然而，当涉及到 null 时，JavaScript 中有一个众所周知的怪癖。typeof 运算符返回 null 值的 “object”。

let user = null;
console.log(typeof user); // "object"
