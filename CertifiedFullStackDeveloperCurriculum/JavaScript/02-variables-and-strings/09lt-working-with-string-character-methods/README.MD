# Working with String Character Methods 字符方法ASCII和数字相互转换

In this lecture you will learn about ASCII character encoding and how to use JavaScript's charCodeAt() and fromCharCode() methods to convert between characters and their numerical ASCII values.

## What Is ASCII, and How Does It Work with charCodeAt() and fromCharCode()?

In programming, understanding how characters are represented as numbers is fundamental. This is where ASCII comes in. ASCII, short for American Standard Code for Information Interchange, is a character encoding standard used in computers to represent text. It assigns a numeric value to each character, which is universally recognized by machines.

在编程中，理解字符如何表示为数字是基础。这就是 ASCII 的用武之地。ASCII 是美国信息交换标准代码的缩写，是计算机中用于表示文本的字符编码标准。它为每个字符分配一个数值，该值被机器普遍识别。

In this lecture, we will explore what ASCII is, how it works, and how you can use JavaScript methods like charCodeAt() and fromCharCode() to interact with ASCII values.

在本讲座中，我们将探讨什么是 ASCII、它是如何工作的，以及如何使用 charCodeAt（） 和 fromCharCode（） 等 JavaScript 方法与 ASCII 值进行交互。

ASCII is a system for encoding characters such as letters, digits, and symbols into numerical values. Each character is mapped to a specific number.

ASCII 是一种将字母、数字和符号等字符编码为数值的系统。每个字符都映射到一个特定的数字。

For example, the capital letter A is represented by the number 65 in ASCII, while the lowercase a is represented by 97. This encoding allows computers to store and manipulate text.

例如，大写字母 A 在 ASCII 中由数字 65 表示，而小写字母 a 由 97 表示。这种编码允许计算机存储和作文本。

The ASCII standard covers 128 characters including:

ASCII 标准涵盖 128 个字符，包括：

Uppercase and lowercase English letters (A-Z, a-z). 大写和小写英文字母（A-Z、a-z）。
Numbers (0-9).  数字 （0-9）。

Common punctuation marks and symbols (!, @, #, and so on). 常见标点符号和符号（！、@、# 等）。

Control characters (such as newline and tab). 控制字符（例如换行符和制表符）。

In JavaScript, you can easily access the ASCII code of a character using the charCodeAt() method. This method is called on a string and returns the ASCII code of the character at a specified index.

在 JavaScript 中，您可以使用 charCodeAt（） 方法轻松访问字符的 ASCII 代码。此方法是在字符串上调用的，并返回指定索引处字符的 ASCII 代码。

Let’s take a look at an example:
我们来看一个例子：

Example Code  示例代码

let letter = "A";
console.log(letter.charCodeAt(0));  // Output: 65

In this example, A is the first character of the string, and calling charCodeAt(0) returns its ASCII value, 65.

在此示例中，A 是字符串的第一个字符，调用 charCodeAt（0） 将返回其 ASCII 值 65。

You can also use this method with other characters to find their ASCII values:

您还可以将此方法与其他字符一起使用以查找其 ASCII 值：

Example Code  示例代码

let symbol = "!";
console.log(symbol.charCodeAt(0));  // Output: 33

Here, the ASCII code for the exclamation mark ! is returned as 33.

在这里，感叹号的 ASCII 代码 ！ 返回为 33。

While charCodeAt() helps you retrieve the ASCII value of a character, the fromCharCode() method allows you to do the opposite: convert an ASCII code into its corresponding character.

charCodeAt（） 可以帮助您检索字符的 ASCII 值，而 fromCharCode（） 方法允许您执行相反的作：将 ASCII 代码转换为其相应的字符。

Let's see this in action:
让我们看看它的实际效果：

Example Code  示例代码

let char = String.fromCharCode(65);
console.log(char);  // Output: A

In this example, fromCharCode(65) converts the ASCII value 65 back to the character A.

在此示例中，fromCharCode（65） 将 ASCII 值 65 转换回字符 A。

Another example would be converting the number 97 to its corresponding lowercase letter:

另一个例子是将数字 97 转换为其相应的小写字母：

Example Code  示例代码

let char = String.fromCharCode(97);
console.log(char);  // Output: a

These methods are particularly useful when you need to manipulate or compare characters based on their ASCII values.

当您需要根据字符的 ASCII 值作或比较字符时，这些方法特别有用。

For instance, you might use charCodeAt() to check if a character is uppercase, lowercase, or a digit by comparing its ASCII value.

例如，您可以使用 charCodeAt（） 通过比较字符的 ASCII 值来检查字符是大写、小写还是数字。

On the other hand, fromCharCode() can be used to dynamically generate characters from their ASCII codes.

另一方面，fromCharCode（） 可用于从其 ASCII 代码动态生成字符。

