# Working with Numbers and Common Number Methods, Not started
In these lectures, you will learn about numbers and common number methods. These include isNaN(), parseInt(), parseFloat(), and toFixed().

## How Does isNaN Work?  isNaN 是如何工作的？
In JavaScript, NaN stands for "Not a Number". It's a special value that represents an unrepresentable or undefined numerical result. NaN is a property of the global object, and it's also considered a type of number in JavaScript, which might seem counterintuitive at first.
在 JavaScript 中， NaN 代表"不是数字"。它是一个特殊值，表示无法表示或未定义的数值结果。 NaN 是全局对象的一个属性，它也被视为 JavaScript 中的一种数字类型，这最初可能看起来有些反直觉。

NaN is typically the result of operations that should return a number but can't produce a meaningful numerical value. For example:
NaN 通常是那些应该返回数字但无法产生有意义的数值结果的操作的结果。例如：

let result = 0 / 0;
console.log(result); // Output: NaN
In this case, dividing zero by zero is mathematically undefined, so JavaScript returns NaN. One peculiar property of NaN is that it's not equal to anything, including itself:
在这种情况下，零除以零在数学上是未定义的，所以 JavaScript 返回 NaN 。 NaN 的一个奇特属性是它不等于任何东西，包括它自己：

console.log(NaN === NaN); // Output: false
This unique behavior makes it challenging to check if a value is NaN using standard comparison operators. To address this, JavaScript provides the isNaN() function. The isNaN() function property is used to determine whether a value is NaN or not. However, it's important to understand how isNaN() works, as it can sometimes produce unexpected results. Here's how isNaN() behaves:
这种独特的行为使得使用标准比较运算符检查 NaN 值变得困难。为了解决这个问题，JavaScript 提供了 isNaN() 函数。 isNaN() 函数属性用于判断一个值是否为 NaN 。然而，理解 isNaN() 的工作原理很重要，因为它有时会产生意想不到的结果。以下是 isNaN() 的行为：

console.log(isNaN(NaN));       // true
console.log(isNaN(undefined)); // true
console.log(isNaN({}));        // true

console.log(isNaN(true));      // false
console.log(isNaN(null));      // false
console.log(isNaN(37));        // false

console.log(isNaN("37"));      // false: "37" is converted to 37
console.log(isNaN("37.37"));   // false: "37.37" is converted to 37.37
console.log(isNaN(""));        // false: empty string is converted to 0
console.log(isNaN(" "));       // false: string with a space is converted to 0

console.log(isNaN("blabla"));  // true: "blabla" is not a number
As you can see, isNaN() first attempts to convert the parameter to a number. If it can't be converted, it returns true. This behavior can lead to some surprising results, especially when dealing with strings that can be coerced into numbers.
如您所见， isNaN() 首先尝试将参数转换为数字。如果无法转换，则返回 true 。这种行为可能导致一些令人惊讶的结果，尤其是在处理可以被强制转换为数字的字符串时。

Due to these potential inconsistencies, ES6 introduced Number.isNaN(). This method does not attempt to convert the parameter to a number before testing. It only returns true if the value is exactly NaN:
由于这些潜在的不一致性，ES6 引入了 Number.isNaN() 。这种方法在测试之前不会尝试将参数转换为数字。只有当值正好是 NaN 时，它才会返回 true ：

console.log(Number.isNaN(NaN));        // true
console.log(Number.isNaN(Number.NaN)); // true
console.log(Number.isNaN(0 / 0));      // true

console.log(Number.isNaN("NaN"));      // false
console.log(Number.isNaN(undefined));  // false
console.log(Number.isNaN({}));         // false
console.log(Number.isNaN("blabla"));   // false
Number.isNaN() provides a more reliable way to check for NaN values, especially in cases where type coercion might lead to unexpected results with the global isNaN() function. In practice, when dealing with numerical operations or user inputs that should be numbers, it's often necessary to check for NaN to handle errors or unexpected inputs gracefully. For example:
Number.isNaN() 提供了一种更可靠的方法来检查 NaN 值，特别是在类型强制可能导致全局 isNaN() 函数产生意外结果的情况下。在实际应用中，在处理数值运算或应为数字的用户输入时，通常需要检查 NaN 以优雅地处理错误或意外输入。例如：

function divide(a, b) {
  let result = a / b;
  if (Number.isNaN(result)) {
    return "Error: Division resulted in NaN";
  }
  return result;
}

console.log(divide(10, 2));  // 5
console.log(divide(10, 0));  // Infinity
console.log(divide(0, 0));   // "Error: Division resulted in NaN"
In this example, we're using Number.isNaN() to catch cases where the division operation results in NaN, allowing us to handle this scenario appropriately. Understanding NaN and how to properly check for it is crucial for writing robust JavaScript code, especially when dealing with mathematical operations or parsing user inputs.
在这个例子中，我们使用 Number.isNaN() 来捕获除法运算结果为 NaN 的情况，从而可以适当地处理这种场景。理解 NaN 以及如何正确检查它对于编写健壮的 JavaScript 代码至关重要，尤其是在处理数学运算或解析用户输入时。

## How Do the parseFloat() and parseInt() Methods Work?
parseFloat() 和 parseInt() 方法是如何工作的？
parseFloat() and parseInt() are two essential methods in JavaScript for converting strings to numbers. These methods are particularly useful when dealing with user input or processing data that comes in string format but needs to be treated as numerical values.
parseFloat() 和 parseInt() 是 JavaScript 中用于将字符串转换为数字的两个重要方法。当处理用户输入或需要将字符串格式数据视为数值时，这些方法特别有用。

Let's start with parseFloat(). This method parses a string argument and returns a floating-point number. It's designed to extract a number from the beginning of a string, even if the string contains non-numeric characters later on. Remember that floats are numbers with decimal points. Here's how parseFloat() works:
我们先来看 parseFloat() 。这个方法解析一个字符串参数并返回一个浮点数。它设计用来从字符串开头提取数字，即使字符串后面包含非数字字符。记住，浮点数是带有小数点的数字。 parseFloat() 的工作原理如下：

console.log(parseFloat("3.14"));     // Output: 3.14
console.log(parseFloat("3.14 abc")); // Output: 3.14
console.log(parseFloat("3.14.5"));   // Output: 3.14
console.log(parseFloat("abc 3.14")); // Output: NaN
As you can see, parseFloat() starts parsing from the beginning of the string and continues until it encounters a character that can't be part of a floating-point number. If it can't find a valid number at the start of the string, it returns NaN (Not a Number).
如您所见， parseFloat() 从字符串开头开始解析，直到遇到不能作为浮点数一部分的字符为止。如果它在字符串开头找不到有效的数字，则返回 NaN （不是数字）。

parseInt(), on the other hand, parses a string argument and returns an integer. Like parseFloat(), it starts from the beginning of the string, but it stops at the first non-digit character. Here's how parseInt() works:
另一方面， parseInt() 解析一个字符串参数并返回一个整数。与 parseFloat() 类似，它从字符串开头开始，但在第一个非数字字符处停止。 parseInt() 的工作原理如下：

console.log(parseInt("42"));       // Output: 42
console.log(parseInt("42px"));     // Output: 42
console.log(parseInt("3.14"));     // Output: 3
console.log(parseInt("abc123"));   // Output: NaN
parseInt() stops parsing at the first non-digit it encounters. For floating-point numbers, it returns only the integer part. If it can't find a valid integer at the start of the string, it returns NaN.
parseInt() 在遇到第一个非数字时停止解析。对于浮点数，它只返回整数部分。如果它在字符串开头找不到有效的整数，则返回 NaN 。

Both methods have some noteworthy behaviors. They ignore leading whitespace:
这两种方法都有一些值得注意的行为。它们忽略前导空格：

console.log(parseFloat("  3.14"));  // Output: 3.14
console.log(parseInt("  42"));      // Output: 42
They handle plus and minus signs at the beginning of the string:
它们处理字符串开头的加号和减号：

console.log(parseFloat("+3.14"));  // Output: 3.14
console.log(parseInt("-42"));      // Output: -42
It's worth noting that while these methods are powerful, they have some limitations. For instance, they don't handle all number formats, such as scientific notation, directly. For more complex parsing needs, you might need to use additional techniques or libraries.
值得注意的是，虽然这些方法很强大，但它们也有一些局限性。例如，它们不能直接处理所有数字格式，如科学计数法。对于更复杂的解析需求，你可能需要使用额外的技术或库。

In conclusion, parseFloat() and parseInt() are valuable tools for converting strings to numbers in JavaScript. Understanding how they work and their specific behaviors allows you to handle numeric data more effectively in your applications, especially when dealing with user inputs or external data sources.
总之， parseFloat() 和 parseInt() 是在 JavaScript 中将字符串转换为数字的有价值工具。了解它们的工作原理及其特定行为，使你能够更有效地处理应用程序中的数值数据，尤其是在处理用户输入或外部数据源时。

## What Is the toFixed() Method, and How Does It Work?
toFixed()方法是什么，它是如何工作的？
The .toFixed() method is a built-in JavaScript function that formats a number using fixed-point notation. It's particularly useful when you need to control the number of decimal places in a number, especially for displaying currency values or when working with precise measurements.
.toFixed() 方法是 JavaScript 的内置函数，使用固定小数点记数法格式化数字。当你需要控制数字的小数位数时，它特别有用，尤其是在显示货币值或处理精确测量时。

The .toFixed() method is called on a number and takes one optional argument, which is the number of digits to appear after the decimal point. It returns a string representation of the number with the specified number of decimal places. Here's a basic example of how .toFixed() works:
.toFixed() 方法被调用在数字上，并接受一个可选参数，即小数点后要出现的位数。它返回一个字符串表示的数字，具有指定的小数位数。以下是 .toFixed() 工作的基本示例：

let num = 3.14159;
console.log(num.toFixed(2)); // Output: "3.14"
In this case, we're limiting the number of decimal places to two. So, 3.14159 becomes 3.14. It's important to note that .toFixed() returns a string, not a number. This is because the method is primarily intended for formatting numbers for display, not for further calculations.
在这种情况下，我们将小数位数限制为两位。所以， 3.14159 成为 3.14 。需要注意的是 .toFixed() 返回的是字符串，而不是数字。这是因为该方法主要用于显示格式化的数字，而不是用于进一步的计算。

The .toFixed() method rounds the number to the nearest value that can be represented with the specified number of decimal places. This rounding behavior is important to understand:
.toFixed() 方法将数字舍入到最接近的、可以用指定的小数位数表示的值。理解这种舍入行为很重要：

console.log((3.14159).toFixed(3));  // Output: "3.142"
console.log((3.14449).toFixed(3));  // Output: "3.144"
console.log((3.14550).toFixed(3));  // Output: "3.146"
As you can see, .toFixed() rounds up when the next digit is 5 or greater, and rounds down otherwise. If you call .toFixed() without arguments, it defaults to 0 decimal places:
如你所见， .toFixed() 在下一个数字是 5 或更大时会向上舍入，否则向下舍入。如果你不带参数调用 .toFixed() ，它默认保留 0 位小数：

let num = 3.14159;
console.log(num.toFixed()); // Output: "3"
The .toFixed() method can be particularly useful when working with financial calculations or displaying prices:
在处理财务计算或显示价格时， .toFixed() 方法特别有用：

let price = 19.99;
let taxRate = 0.08;
let total = price + (price * taxRate);

console.log("Total: $" + total.toFixed(2)); // Output: "Total: $21.59"
In this example, .toFixed(2) ensures that the total is always displayed with two decimal places, which is standard for currency in many countries.
在这个例子中， .toFixed(2) 确保总金额始终显示为两位小数，这是许多国家货币的标准格式。

In conclusion, the .toFixed() method is a powerful tool for formatting numbers in JavaScript, particularly when you need to control the display of decimal places. While it's primarily used for formatting output, remember its behavior, especially when precise calculations are needed.
总之， .toFixed() 方法是 JavaScript 中格式化数字的强大工具，尤其是在你需要控制小数位显示时。虽然它主要用于格式化输出，但请记住它的行为，特别是在需要精确计算时。