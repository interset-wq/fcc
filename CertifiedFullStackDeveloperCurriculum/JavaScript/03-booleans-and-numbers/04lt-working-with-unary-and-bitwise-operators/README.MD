# Working with Unary and Bitwise Operators 一元运算符和位运算

In these lectures you will learn about unary and bitwise operators.

## What Are Unary Operators, and How Do They Work? 一元运算符

Unary operators act on a single operand to perform operations like type conversion, value manipulation, or checking certain conditions. Let's look at some common unary operators and how they work.

一元运算符作用于单个操作数，执行类型转换、值操作或检查某些条件等操作。让我们看看一些常见的一元运算符及其工作原理。

The unary plus operator converts its operand into a number. If the operand is already a number, it remains unchanged.

一元加号运算符将其操作数转换为数字。如果操作数已经是数字，则保持不变。

const str = '42';
const strToNum = +str;

console.log(strToNum); // 42
console.log(typeof str); // string
console.log(typeof strToNum); // number

Unary plus is handy when you want to make sure you're working with a numeric value. As you might guess, there's a unary negation operator. It negates the value of the operand. It works similarly to the unary plus, except it flips the sign.

当你想确保自己正在处理数值时，一元加号运算符会很有用。正如你可能猜到的，还有一个一元否定运算符。它否定操作数的值。它的工作方式与一元加号类似，只是它会改变符号。

const str = '42';
const strToNegativeNum = -str;

console.log(strToNegativeNum); // -42
console.log(typeof str); // string
console.log(typeof strToNegativeNum); // number

The logical NOT operator, represented by an exclamation mark (!), is another unary operator. It flips the boolean value of its operand. So, if the operand is true, it becomes false, and if it's false, it becomes true. 

逻辑非运算符，用感叹号（!）表示，是另一个一元运算符。它翻转其操作数的布尔值。所以，如果操作数是 true，它就变成 false，如果操作数是 false，它就变成 true。

let isOnline = true;
console.log(!isOnline); // false

let isOffline = false;
console.log(!isOffline); // true

The bitwise NOT operator is a less commonly used unary operator. Represented by a tilde, ~, it inverts the binary representation of a number. Computers store numbers in binary format (1s and 0s). The ~ operator flips every bit, meaning it changes all 1s to 0s and all 0s to 1s. You will learn more about binary and bits in a future lecture.

位非运算符是一种不太常用的单目运算符。它用波浪号~表示，用于反转一个数的二进制表示。计算机以二进制格式（1 和 0）存储数字。~运算符翻转每一位，意味着将所有的 1 变为 0，所有的 0 变为 1。你将在未来的课程中了解更多关于二进制和位的内容。

const num = 5; // The binary for 5 is 00000101

console.log(~num); // -6

In this example, 5 became -6 because by applying the ~ operator to 5, you get - (5 + 1), which equals -6 due to two's complement representation. Two's complement is a way computers represent negative numbers in binary. You probably won't use the bitwise NOT often unless you're working with low-level programming tasks like manipulating bits directly.

在这个例子中，~将 0 变成了 1，因为将~运算符应用于 3，得到 4，由于二进制补码表示，4 等于 5。二进制补码是计算机在二进制中表示负数的一种方式。除非你正在处理像直接操作位这样的底层编程任务，否则你可能不会经常使用位非运算符。

The void keyword is a unary operator that evaluates an expression and returns undefined.

void关键字是一个单目运算符，用于计算表达式并返回其结果。

const result = void (2 + 2);

console.log(result); // undefined
void is also commonly used in hyperlinks to prevent navigation:

void也常用于超链接中，以防止导航：

<a href="javascript:void(0);">Click Me</a>

Finally, there is the typeof operator which you learned about in previous lectures. This returns the type of its operand as a string.

最后，还有你在之前的讲座中学到的 typeof 运算符，它返回其操作数的类型作为字符串。

const value = 'Hello world';

console.log(typeof value); // string

## What Are Bitwise Operators, and How Do They Work? 位运算符

Bitwise operators in JavaScript are special operators that work on the binary representations of numbers. To understand bitwise operators, we first need to grasp the concept of bits and binary numbers. In computing, a bit is the most basic unit of information. It can have only two values: 0 or 1. Binary is a number system that uses only these two digits to represent all numbers.
JavaScript 中的位运算符是作用于数字二进制表示的特殊运算符。要理解位运算符，我们首先需要掌握位和二进制数的概念。在计算机中，位是最基本的信息单位。它只有两个值： 0 或 1 。二进制是一种仅使用这两个数字来表示所有数字的数制。

For example, the binary representation of the decimal number 10 is 1010. In this system, each digit represents a power of 2, starting from the rightmost digit and increasing as we move left.
例如，十进制数 10 的二进制表示是 1010 。在这个系统中，每个数字代表 2 的幂，从最右边的数字开始，向左移动时幂次逐渐增加。

1	0	1	0
1 · 23	0 · 22	1 · 21	0 · 20
8	0	2	0
In the table above, the first row shows the binary number 1010, the second row shows the power of 2 represented by each binary position, and the third row shows the result of each multiplication. If you add all the values in the third row, they total 10.
在上述表格中，第一行显示了二进制数 1010 ，第二行显示了每个二进制位的幂，第三行显示了每次乘法的结果。如果你将第三行的所有值相加，它们总共是 10 。

Now, let's dive into bitwise operators. These operators perform operations on the binary representations of numbers. JavaScript provides several bitwise operators, including AND (&), OR (|), XOR (^), NOT (~), left shift (<<), and right shift (>>).
现在，让我们深入了解位运算符。这些运算符对数字的二进制表示进行操作。JavaScript 提供了多种位运算符，包括与（ & ）、或（ | ）、异或（ ^ ）、非（ ~ ）、左移（ << ）和右移（ >> ）。

The bitwise AND (&) operator returns a 1 in each bit position for which the corresponding bits of both operands are 1. Here's an example:
位与（ & ）运算符在两个操作数的对应位都为 1 时，在每一位返回 1 。这里有一个例子：

let a = 5;  // Binary: 101
let b = 3;  // Binary: 011
console.log(a & b);  // Output: 1 (Binary: 001)
In this example, we perform a bitwise AND operation on 5 (101 in binary) and 3 (011 in binary). The result is 1 (001 in binary) because only the rightmost bit is 1 in both numbers.
在这个例子中，我们对 5 （二进制为 101 ）和 3 （二进制为 011 ）进行位与运算。结果是 1 （二进制为 001 ），因为只有最右边的位在两个数中都是 1 。

The bitwise OR (|) operator returns a 1 in each bit position for which the corresponding bits of either or both operands are 1. For example:
位或（ | ）运算符在任意一个或两个操作数的对应位为 1 时，在每一位返回 1 。例如：

let a = 5;  // Binary: 101
let b = 3;  // Binary: 011
console.log(a | b);  // Output: 7 (Binary: 111)
Here, the result is 7 (111 in binary) because at least one of the bits is 1 in each position.
这里，结果是 7 （二进制为 111 ），因为在每一位中至少有一个位是 1 。

The bitwise XOR (^) operator returns a 1 in each bit position for which the corresponding bits of either, but not both, operands are 1. For instance:
位运算符 XOR（ ^ ）在任一操作数的对应位不同但非同时为 1 时，在每一位位置返回 1 。例如：

let a = 5;  // Binary: 101
let b = 3;  // Binary: 011
console.log(a ^ b);  // Output: 6 (Binary: 110)
The result is 6 (110 in binary) because the first and second bits from the right are different in the two numbers.
结果是 6 （二进制为 110 ），因为两个数从右往左的第一位和第二位不同。

The bitwise NOT (~) operator inverts all the bits of its operand. For example:
位运算符 NOT（ ~ ）会反转其操作数的所有位。例如：

let a = 5;  // Binary: 101
console.log(~a);  // Output: -6
This might seem surprising, but it's because of how negative numbers are represented in binary using two's complement.
这可能看起来很奇怪，但这是因为负数在二进制中使用二进制补码表示。

The left shift (<<) operator shifts all bits to the left by a specified number of positions. For example:
左移（ << ）运算符将所有位向左移动指定的位数。例如：

let a = 5;  // Binary: 101
console.log(a << 1);  // Output: 10 (Binary: 1010)
Here, all bits are shifted one position to the left, effectively multiplying the number by 2.
这里，所有位向左移动一位，相当于将数字乘以 2 。

The right shift (>>) operator shifts all bits to the right. For example:
右移（ >> ）运算符将所有位向右移动。例如：

let a = 5;  // Binary: 101
console.log(a >> 1);  // Output: 2 (Binary: 10)
Here, all bits are shifted one position to the right, effectively dividing the number by 2 and rounding down.
这里，所有位向右移动一位，相当于将数字除以 2 并向下取整。

Bitwise operators are often used in low-level programming and cryptography. While they may not be as commonly used in everyday JavaScript programming, understanding them can be beneficial for certain specialized tasks and can deepen your understanding of how computers work at a fundamental level.
位运算符通常用于低级编程和密码学。虽然它们在日常 JavaScript 编程中可能不如其他运算符常用，但理解它们对于某些特定任务是有益的，并且可以加深你对计算机基本工作原理的理解。

