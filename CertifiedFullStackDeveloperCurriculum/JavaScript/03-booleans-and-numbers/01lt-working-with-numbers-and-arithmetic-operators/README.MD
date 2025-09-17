# Working with Numbers and Arithmetic Operators

In these lectures you will learn about the number type, arithmetic operators, and using them with numbers and strings.

## What Is the Number Type in JavaScript, and What Are the Different Types of Numbers Available? 所有数字都是Number类型

The Number type is one of the most used data types in JavaScript and other programming languages. Numbers might seem simple, but there's a lot to explore when it comes to numbers in JavaScript. So, let's take a deeper look. In JavaScript, the Number data type represents a numeric value.

Number 类型是 JavaScript 和其他编程语言中最常用的数据类型之一。数字可能看起来很简单，但当涉及到 JavaScript 中的数字时，还有很多东西需要探索。那么，让我们深入了解一下。在 JavaScript 中，Number 数据类型表示数值。

Unlike many other programming languages that separate integers and floating-point numbers into different types, JavaScript uses one unified Number type to account for numbers. This means you can work with whole numbers, decimals, and even special numeric values all under the same Number data type umbrella.

与许多其他将整数和浮点数分成不同类型的编程语言不同，JavaScript 使用一种统一的数字类型来解释数字。这意味着您可以在同一个数字数据类型保护伞下处理整数、小数甚至特殊数值。

Here's a basic example showing you integers, floating point numbers, and negative numbers are all of type number:

这是一个基本示例，显示整数、浮点数和负数都是 number 类型：

const wholeNumber = 50;
const decimalNumber = 4.5;
const negativeNumber = -7;

console.log(typeof wholeNumber); // number
console.log(typeof decimalNumber); // number
console.log(typeof negativeNumber); // number

JavaScript's Number type includes various kinds of numeric values, ranging from simple integers and floating-point numbers to special cases like Infinity and NaN, or "Not a Number". Let's break down the main types you'll encounter. Integers are whole numbers without any fractional or decimal part. They can be positive, negative, or zero. Here are some examples:

JavaScript 的 Number 类型包括各种数值，从简单的整数和浮点数到特殊情况，如 Infinity 和 NaN，或“不是数字”。让我们分解一下您将遇到的主要类型。整数是没有任何小数或小数部分的整数。它们可以是正数、负数或零。这里有些例子：

const positiveInteger = 100;
const negativeInteger = -25;
const zero = 0;

console.log(typeof positiveInteger); // number
console.log(typeof negativeInteger); // number
console.log(typeof zero); // number

Floating point numbers are numbers with decimal points. They're often referred to as just "floats" by JavaScript developers. Floats are useful when you need more precision, such as when you're dealing with measurements or currencies. Here are some examples:

浮点数是带小数点的数字。它们通常被 JavaScript 开发人员称为“浮点数”。当您需要更高的精度时，例如当您处理测量值或货币时，浮点数非常有用。这里有些例子：

const floatingPointNumber = 4.5;
const anotherFloat = 89.56;
const oneMoreFloat = 16.462;

console.log(typeof floatingPointNumber); // number
console.log(typeof anotherFloat); // number
console.log(typeof oneMoreFloat); // number

JavaScript can represent numbers that are beyond the maximum limit with Infinity. You'll encounter this when you try to divide a number by zero or on rare occasions, exceed the upper boundary of the Number type. Here's an example:

JavaScript 可以表示超出 Infinity 最大限制的数字。当您尝试将数字除以零时，或者在极少数情况下，您会遇到这种情况，超过数字类型的上限。这是一个例子：

const infiniteNumber = 1 / 0;
console.log(infiniteNumber); // Infinity
console.log(typeof infiniteNumber); // number

Sometimes in JavaScript, some mathematical operations don't result in a valid number. For instance, if you try to perform a mathematical operation on something that isn't a number, you'll get NaN, which stands for "Not a Number":

有时在 JavaScript 中，某些数学运算不会产生有效数字。例如，如果您尝试对非数字的东西执行数学运算，您将得到 NaN，它代表“不是数字”：

const notANumber = 'hello world' / 2;
console.log(notANumber); // NaN

Surprisingly, the type of NaN is also Number:

令人惊讶的是，NaN 的类型也是 Number：

const notANumber = 'hello world' / 2;
console.log(typeof notANumber); // number

Apart from the standard decimal system (base 10), JavaScript also supports numbers in different bases such as binary, octal, and hexadecimal. Binary is a base-2 system that uses only digits 1 and 0. Octal is a base-8 system that uses only digits 0 to 7. Hexadecimal is a base-16 system that uses digits 0 to 9 and letters a to f, like you see in CSS hex colors.

除了标准十进制系统（以 10 为基数）外，JavaScript 还支持不同基数的数字，例如二进制、八进制和十六进制。二进制是一个以 2 为基数的系统，仅使用数字 1 和 0。八进制是一个以 8 为基数的系统，仅使用数字 0 到 7。十六进制是一个以 16 为基数的系统，它使用数字 0 到 9 和字母 a 到 f，就像您在 CSS 十六进制颜色中看到的那样。

## What Are the Different Arithmetic Operators in JavaScript? 算术运算符

JavaScript provides tools to perform basic arithmetic operations on numbers, such as addition, subtraction, multiplication, and division. JavaScript also includes operators for more complex arithmetic operations, such as remainder and exponentiation.

JavaScript 提供了对数字执行基本算术运算的工具，例如加法、减法、乘法和除法。JavaScript 还包括用于更复杂算术运算的运算符，例如余数和求幂。

All these tools are called arithmetic operators. Let's look at these operators in detail, how to use them and how to combine them.

所有这些工具都称为算术运算符。让我们详细看看这些运算符，如何使用它们以及如何组合它们。

The addition operator is a plus sign (+). The addition operator allows you to find the total of two or more numbers. In addition operations, the order of the numbers doesn't matter:

加法运算符是加号 （+）。加法运算符允许您找到两个或多个数字的总和。在加法运算中，数字的顺序无关紧要：

const num1 = 10;
const num2 = 5;
const num3 = 15;

const result1 = num1 + num2;
const result2 = num2 + num1;
const result3 = num2 + num1 + num3;

console.log(result1); // 15
console.log(result2); // 15
console.log(result3); // 30

The subtraction operator is a minus sign (-). It allows you to find the difference between two numbers. Use the minus sign when you want to subtract a number from another number, usually a smaller one from a bigger one:

减法运算符是减号 （-）。它允许您找到两个数字之间的差异。当您想从另一个数字中减去一个数字时，请使用减号，通常是从较大的数字中减去较小的数字：

const difference = 10 - 5;
console.log(difference); // 5

If a smaller number comes first, you'll get a negative result:

如果数字较小在前，您将得到否定结果：

const difference = 5 - 10;
console.log(difference); // -5

You can also assign the numbers to variables and do the subtraction with the variable names:

您还可以将数字分配给变量并使用变量名称进行减法：

const num1 = 10;
const num2 = 5;
const result = num1 - num2;

console.log(result); // 5

In JavaScript, the multiplication operator is represented by an asterisk (*) and is used to find the product of two or more numbers. The order of the numbers you're multiplying does not matter:

在 JavaScript 中，乘法运算符由星号 （*） 表示，用于查找两个或多个数字的乘积。您要乘法的数字的顺序无关紧要：

const num1 = 10;
const num2 = 5;
const num3 = 15;

const result1 = num1 * num2;
const result2 = num2 * num1;
const result3 = num2 * num1 * num3;

console.log(result1); // 50
console.log(result2); // 50
console.log(result3); // 750

In JavaScript, the division operator is a slash (/), which differs from the division symbol used in traditional math (÷). You perform division operations with the division operator. The order of the numbers you're dividing matters in this case:

在 JavaScript 中，除法运算符是斜杠 （/），它不同于传统数学中使用的除法符号 （÷）。您可以使用除法运算符执行除法运算。在这种情况下，您要除法的数字的顺序很重要：

const num1 = 10;
const num2 = 5;
const num3 = 15;

const result1 = num1 / num2;
const result2 = num2 / num1;
const result3 = num2 / num1 / num3;

console.log(result1); // 2
console.log(result2); // 0.5
console.log(result3); // 0.03333333333333333

It's important to note that if you try to divide by zero, JavaScript will return Infinity:

重要的是要注意，如果你尝试除以零，JavaScript 将返回 Infinity：

const result = 10 / 0; 

console.log(result); // Infinity

Make sure to avoid those types of calculations so you don't end up with unexpected results in your code.

确保避免这些类型的计算，以免在代码中最终出现意外结果。

The remainder operator, represented by a percentage sign (%), returns the remainder of a division. The remainder in math is the leftover value after performing division:

余数运算符由百分号 （%） 表示，返回除法的余数。数学中的余数是执行除法后的剩余值：

const num1 = 10;
const num2 = 3;
const remainder = num1 % num2;

console.log(remainder); // 1

The exponentiation operator, represented by a double asterisk (**), raises one number to the power of another:

由双星号 （**） 表示的幂运算符将一个数字提高到另一个数字的幂：

const num1 = 2;
const num2 = 3;

const exponent = num1 ** num2;
console.log(exponent); // 8

It's possible to mix operators in a single operation or expression:

可以在单个作或表达式中混合运算符：

const result = 10 + 5 * 2 - 8 / 4;
console.log(result); // 18

When you mix different operators in a single expression, the JavaScript engine follows a system called operator precedence to determine the order of operations. Operator precedence determines the order in which operations are executed in expressions. You will learn more about operator precedence in future lectures.

当您在单个表达式中混合使用不同的运算符时，JavaScript 引擎会遵循称为运算符优先级的系统来确定作的顺序。运算符优先级决定了表达式中作的执行顺序。您将在以后的讲座中了解有关运算符优先级的更多信息。

## What Happens When You Try to Do Calculations with Numbers and Strings?
字符串参与数学运算

JavaScript is a language where things sometimes work in surprising, or even weird, ways. One such surprise occurs when you mix numbers and strings in calculations. The first thing you'll probably try is to add a number and a string. In JavaScript, the + operator does double duty. It handles both addition and string concatenation, which is a way to join two strings together.

JavaScript 是一种语言，事物有时会以令人惊讶甚至奇怪的方式工作。当您在计算中混合数字和字符串时，就会出现这样的惊喜。您可能要尝试的第一件事是添加一个数字和一个字符串。在 JavaScript 中，+ 运算符具有双重作用。它处理加法和字符串串联，这是一种将两个字符串连接在一起的方法。

When you use + with a number and a string, JavaScript decides to treat them both as strings and joins them together. If you check the type of the result with the typeof operator, you'd see it's indeed a string:

当您将 + 与数字和字符串一起使用时，JavaScript 决定将它们都视为字符串并将它们连接在一起。如果你使用 typeof 运算符检查结果的类型， 你会看到它确实是一个字符串：

const result = 5 + '10';

console.log(result); // 510
console.log(typeof result); // string

What do you think will happen if you switch the order of 5 and '10'?

你认为如果你把 5 和 “10” 的顺序换了会发生什么？

const result = '10' + 5;

console.log(result); // 105
console.log(typeof result); // string

You can see the same thing happened. JavaScript sees a string in '10' and a number in 5, so it converts the number to a string and concatenates them. This is known as type coercion. Type coercion is when a value from one data type is  converted into another.

你可以看到同样的事情发生了。JavaScript 看到 “10” 中的字符串和 5 中的数字，因此它将数字转换为字符串并将它们连接起来。这称为类型强制。类型强制是指将一种数据类型的值转换为另一种数据类型。

Things get more interesting when you try to perform other arithmetic operations like subtraction, multiplication, or division with a string and number. In these cases, JavaScript tries to convert the string into a number before doing the math – another type coercion! Here's what happens:

当您尝试执行其他算术运算（例如减法、乘法或用字符串和数字除法）时，事情会变得更加有趣。在这些情况下，JavaScript 会在进行数学运算之前尝试将字符串转换为数字——另一种类型强制！发生的情况如下：

const subtractionResult = '10' - 5;
console.log(subtractionResult); // 5
console.log(typeof subtractionResult); // number

const multiplicationResult = '10' * 2;
console.log(multiplicationResult); // 20
console.log(typeof multiplicationResult); // number

const divisionResult = '20' / 2;
console.log(divisionResult); // 10
console.log(typeof divisionResult); // number

In the examples above, JavaScript successfully converts the string '10' or '20' to a number and then performs the calculation. As a result, '10' - 5 yields 5, '10' * 2 gives 20, and '20' / 2 results in 10.

在上面的示例中，JavaScript 成功地将字符串 “10” 或 “20” 转换为数字，然后执行计算。结果，'10' - 5 产生 5，'10' * 2 产生 20，'20' / 2 产生 10。

But what if the string doesn't look like a number? Let's see what happens in that case:

但是，如果字符串看起来不像数字怎么办？让我们看看在这种情况下会发生什么：

const subtractionResult = 'abc' - 5;
console.log(subtractionResult); // NaN
console.log(typeof subtractionResult); // number

const multiplicationResult = 'abc' * 2;
console.log(multiplicationResult); // NaN
console.log(typeof multiplicationResult); // number

const divisionResult = 'abc' / 2;
console.log(divisionResult); // NaN
console.log(typeof divisionResult); // number

In the examples above, the string 'abc' does not represent a valid numeric value, so JavaScript cannot convert it into a meaningful number. When such conversion fails, JavaScript returns NaN, which stands for "Not a Number". NaN is a special value of the Number type that represents an invalid or unrepresentable number.

在上面的示例中，字符串 “abc” 不表示有效的数值，因此 JavaScript 无法将其转换为有意义的数字。当此类转换失败时，JavaScript 返回 NaN，代表“Not a Number”。NaN 是 Number 类型的特殊值，表示无效或不可表示的数字。

What if you perform arithmetic operations with a boolean (true or false)? Let's see what happens. JavaScript treats booleans as numbers in mathematical operations: true becomes 1, and false becomes 0.

如果您使用布尔值（ 真或假 ）执行算术运算怎么办？ 让我们看看会发生什么。JavaScript 将布尔值视为数学运算中的数字：true 变为 1，false 变为 0。

const result1 = true + 1;
console.log(result1); // 2
console.log(typeof result1); // number

const result2 = false + 1;
console.log(result2); // 1
console.log(typeof result2); // number

const result3 = 'Hello' + true;
console.log(result3); // "Hellotrue"
console.log(typeof result3); // string

In the first two examples, true + 1 resulted in 2, and false + 1 resulted in 1. In the third example, 'Hello' + true, JavaScript converted true to a string and concatenates it with 'Hello', resulting in 'Hellotrue', which is a string.

在前两个示例中，true + 1 导致 2，false + 1 导致 1。 在第三个示例“Hello”+ true 中，JavaScript 将 true 转换为字符串，并将其与 “Hello” 连接起来，从而生成 “Hellotrue”，这是一个字符串。

For null and undefined, JavaScript treats null as 0 and undefined as NaN in mathematical operations:

对于 null 和 undefined，JavaScript 在数学运算中将 null 视为 0，将 undefined 视为 NaN：

const result1 = null + 5;
console.log(result1); // 5
console.log(typeof result1); // number

const result2 = undefined + 5;
console.log(result2); // NaN
console.log(typeof result2); // number

JavaScript often performs type coercion, automatically converting data types such as numbers, strings, and booleans in sometimes unexpected ways. Understanding these conversions is crucial for avoiding bugs and writing robust code in your projects.

JavaScript 经常执行类型强制，有时以意想不到的方式自动转换数字、字符串和布尔值等数据类型。了解这些转换对于避免错误和在项目中编写强大的代码至关重要。

