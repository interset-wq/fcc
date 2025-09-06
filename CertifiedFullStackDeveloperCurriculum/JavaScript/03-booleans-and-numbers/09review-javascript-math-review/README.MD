# JavaScript Math Review

## Working with the Number Data Type 使用数字数据类型

Definition: JavaScript's Number type includes integers, floating-point numbers, Infinity and NaN. Floating-point numbers are numbers with a decimal point. Positive Infinity is a number greater than any other number while -Infinity is a number smaller than any other number. NaN (Not a Number) represents an invalid numeric value like the string "Jessica".
定义：JavaScript 的 Number 类型包括整数、浮点数、 Infinity 和 NaN 。浮点数是带有小数点的数字。正 Infinity 是一个大于任何其他数字的数，而 -Infinity 是一个小于任何其他数字的数。 NaN （ Not a Number ）表示无效的数值，例如字符串 "Jessica" 。

## Common Arithmetic Operations 常见算术运算

Addition Operator: This operator (`+`) is used to calculate the sum of two or more numbers.
加法运算符：该运算符（ + ）用于计算两个或多个数字的总和。
Subtraction Operator: This operator (`-`) is used to calculate the difference between two numbers.
减法运算符：该运算符（ - ）用于计算两个数之间的差值。
Multiplication Operator: This operator (`*`) is used to calculate the product of two or more numbers.
乘法运算符：该运算符（ * ）用于计算两个或多个数的乘积。
Division Operator: This operator (`/`) is used to calculate the quotient between two numbers
除法运算符：该运算符（ / ）用于计算两个数之间的商。
Division By Zero: If you try to divide by zero, JavaScript will return Infinity.
除以零：如果你尝试除以零，JavaScript 将返回 Infinity 。
Remainder Operator: This operator(`%`) returns the remainder of a division.
取余运算符：该运算符（ % ）返回除法的余数。
Exponentiation Operator: This operator (`**`) raises one number to the power of another.
指数运算符：该运算符（ ** ）将一个数提升为另一个数的幂。

## Calculations with Numbers and Strings 数字和字符串的计算

Explanation: When you use the `+` operator with a number and a string, JavaScript will coerce the number into a string and concatenate the two values. When you use the `-`, `*` or `/` operators with a string and number, JavaScript will coerce the string into a number and the result will be a number. For `null` and `undefined`, JavaScript treats `null` as `0` and `undefined` as `NaN` in mathematical operations.
说明：当使用 + 运算符与数字和字符串一起时，JavaScript 会将数字转换为字符串，并将两个值连接起来。当使用 - 、 * 或 / 运算符与字符串和数字一起时，JavaScript 会将字符串转换为数字，结果将是数字。对于 null 和 undefined ，JavaScript 在数学运算中将 null 视为 0，将 undefined 视为 NaN 。

const result = 5 + '10';

console.log(result); // 510
console.log(typeof result); // string

const subtractionResult = '10' - 5;
console.log(subtractionResult); // 5
console.log(typeof subtractionResult); // number

const multiplicationResult = '10' * 2;
console.log(multiplicationResult); // 20
console.log(typeof multiplicationResult); // number

const divisionResult = '20' / 2;
console.log(divisionResult); // 10
console.log(typeof divisionResult); // number

const result1 = null + 5;
console.log(result1); // 5
console.log(typeof result1); // number

const result2 = undefined + 5;
console.log(result2); // NaN
console.log(typeof result2); // number

## Operator Precedence  操作符优先级

Definition: Operator precedence determines the order in which operations are evaluated in an expression. Operators with higher precedence are evaluated before those with lower precedence. Values inside the parenthesis will be evaluated first and multiplication/division will have higher precedence than addition/subtraction. If the operators have the same precedence, then JavaScript will use associativity.
定义：操作符优先级决定了表达式中操作的求值顺序。优先级高的操作符会先于优先级低的操作符被求值。括号内的值会首先被求值，乘除的优先级高于加减。如果操作符具有相同的优先级，那么 JavaScript 将使用结合性。

const result = (2 + 3) * 4;

console.log(result); // 20

const result2 = 10 - 2 + 3;

console.log(result2); // 11

const result3 = 2 ** 3 ** 2;

console.log(result3); // 512

Definition: Associativity informs us the direction in which an expression is evaluated when multiple operators of the same type exist. It defines whether the expression should be evaluated from left-to-right (left-associative) or right-to-left (right-associative). For example, the exponent operator is also right to left associative:
定义：结合性告诉我们当存在多个相同类型的操作符时，表达式将按什么方向被求值。它定义了表达式应该从左到右（ left-associative ）还是从右到左（ right-associative ）被求值。例如，指数操作符也是从右到左结合的：

const result4 = 5 ** 4 ** 1; // 625

console.log(result4);

## Increment and Decrement Operators 自增和自减操作符

Increment Operator: This operator is used to increase the value by one. The prefix notation ++num increases the value of the variable first, then returns a new value. The postfix notation num++ returns the current value of the variable first, then increases it.
自增运算符：这个运算符用于将值增加一。前缀表示法 ++num 先增加变量的值，然后返回新值。后缀表示法 num++ 先返回变量的当前值，然后增加它。

let x = 5;

console.log(++x); // 6
console.log(x); // 6


let y = 5;

console.log(y++); // 5
console.log(y); // 6

Decrement Operator: This operator is used to decrease the value by one. The prefix notation and postfix notation work the same way as earlier with the increment operator.
自减运算符：这个运算符用于将值减少一。它的前置表示法和后置表示法与自增运算符的工作方式相同。

let num = 5;

console.log(--num); // 4
console.log(num--); // 4
console.log(num); // 3

## Compound Assignment Operators 复合赋值运算符

Addition Assignment (+=) Operator: This operator performs addition on the values and assigns the result to the variable.
加法赋值运算符 ( += )：该运算符对值进行加法运算，并将结果赋值给变量。
Subtraction Assignment (-=) Operator: This operator performs subtraction on the values and assigns the result to the variable.
减法赋值运算符 ( -= )：该运算符对值进行减法运算，并将结果赋值给变量。
Multiplication Assignment (*=) Operator: This operator performs multiplication on the values and assigns the result to the variable.
乘法赋值运算符 ( *= )：该运算符对值进行乘法运算，并将结果赋值给变量。
Division Assignment (/=) Operator: This operator performs division on the values and assigns the result to the variable.
除法赋值（ /= ）运算符：该运算符对值进行除法运算，并将结果赋值给变量。
Remainder Assignment (%=) Operator: This operator divides a variable by the specified number and assigns the remainder to the variable.
取余赋值运算符（ %= ）：该运算符将一个变量除以指定的数，并将余数赋值给该变量。
Exponentiation Assignment (**=) Operator: This operator raises a variable to the power of the specified number and reassigns the result to the variable.
指数赋值运算符（ **= ）：该运算符将一个变量提升到指定的数次幂，并将结果重新赋值给该变量。

## Booleans and Equality  布尔值与相等性

Boolean Definition: A boolean is a data type that can only have two values: `true` or `false`.
布尔值定义：布尔值是一种数据类型，它只能有两个值： true 或 false 。
Equality (==) Operator: This operator uses type coercion before checking if the values are equal.
相等（ == ）运算符：该运算符在检查值是否相等之前会进行类型转换。

console.log(5 == '5'); // true

Strict Equality (===) Operator: This operator does not perform type coercion and checks if both the types and values are equal.
严格相等（ === ）运算符：该运算符不会进行类型转换，而是检查类型和值是否都相等。

console.log(5 === '5'); // false

Inequality (!=) Operator: This operator uses type coercion before checking if the values are not equal.
不等式（ != ）运算符：这个运算符在检查值是否不相等之前会进行类型转换。
Strict Inequality (!==) Operator: This operator does not perform type coercion and checks if both the types and values are not equal.
严格不等式（ !== ）运算符：该运算符不执行类型转换，并检查类型和值都不相等。

## Comparison Operators  比较运算符

Greater Than (>) Operator: This operator checks if the value on the left is greater than the one on the right.
大于（ > ）运算符：该运算符检查左边的值是否大于右边的值。
Greater Than (>=) or Equal Operator: This operator checks if the value on the left is greater than or equal to the one on the right.
大于（ >= ）或等于运算符：该运算符检查左边的值是否大于或等于右边的值。
Less Than (<) Operator: This operator checks if the value on the left is less than the one on the right.
小于（ < ）运算符：该运算符检查左边的值是否小于右边的值。
Less Than (<=) or Equal Operator: This operator checks if the value on the left is less than or equal to the one on the right.
小于（ <= ）或等于运算符：该运算符检查左边的值是否小于或等于右边的值。

# Unary Operators  一元运算符

Unary Plus Operator: This operator converts its operand into a number. If the operand is already a number, it remains unchanged.
一元加号运算符：该运算符将其操作数转换为数字。如果操作数已经是数字，则保持不变。

const str = '42';
const num = +str;

console.log(num); // 42
console.log(typeof num); // number

Unary Negation (-) Operator: This operator negates the operand.
一元否定（ - ）运算符：该运算符对操作数进行否定。

const num = 4;
console.log(-num); // -4

Logical NOT (!) Operator: This operator flips the boolean value of its operand. So, if the operand is true, it becomes false, and if it's false, it becomes true. 
逻辑非（ ! ）运算符：这个运算符会翻转其操作数的布尔值。所以，如果操作数是 true ，它会变成 false ，如果它是 false ，它会变成 true 。

## Bitwise Operators  按位运算符

Bitwise AND (&) Operator: This operator returns a 1 in each bit position for which the corresponding bits of both operands are 1.
按位与（ & ）运算符：这个运算符对于两个操作数的对应位都为 1 的位位置返回 1。
Bitwise AND Assignment (&=) Operator: This operator performs a bitwise AND operation with the specified number and reassigns the result to the variable.
按位与赋值运算符 ( &= )：该运算符对指定的数字执行 bitwise AND 操作，并将结果重新赋值给变量。
Bitwise OR (|) Operator: This operator returns a 1 in each bit position for which the corresponding bits of either or both operands are 1.
按位或（ | ）运算符：该运算符对于操作数中任意一个或两个对应位为 1 的位位置，返回 1。
Bitwise OR Assignment (|=) Operator: This operator performs a bitwise OR operation with the specified number and reassigns the result to the variable.
按位或赋值（ |= ）运算符：该运算符将指定的数值与 bitwise OR 运算，并将结果重新赋值给变量。
Bitwise XOR (^) Operator: This operator returns a 1 in each bit position for which the corresponding bits of either, but not both, operands are 1.
按位异或（ ^ ）运算符：该运算符对于操作数中只有一个对应位为 1 的位位置，返回 1。
Bitwise NOT (~) Operator: This operator inverts the binary representation of a number.
按位非（ ~ ）运算符：这个运算符反转数字的二进制表示。
Left Shift (<<) Operator: This operator shifts all bits to the left by a specified number of positions.
左移运算符 ( << )：该运算符将所有位向左移动指定的位数。
Right Shift (>>) Operator: This operator shifts all bits to the right.
右移运算符 ( >> )：该运算符将所有位向右移动。

## Conditional Statements, Truthy Values, Falsy Values and the Ternary Operator 条件语句、真值、假值和三元运算符

if/else if/else: An if statement takes a condition and runs a block of code if that condition is truthy. If the condition is false, then it moves to the else if block. If none of those conditions are true, then it will execute the else clause. Truthy values are any values that result in true when evaluated in a Boolean context like an if statement. Falsy values are values that evaluate to false in a Boolean context.
if/else if/else ：一个 if 语句接受一个条件，如果该条件为 truthy ，则执行代码块。如果条件为 false ，则跳转到 else if 块。如果这些条件都不为 true ，则执行 else 子句。 Truthy 值是在布尔上下文（如 if 语句）中求值为 true 的任何值。 Falsy 值是在布尔上下文中求值为 false 的值。

const score = 87;

if (score >= 90) {
 console.log('You got an A'); 
} else if (score >= 80) {
 console.log('You got a B'); // You got an B
} else if (score >= 70) {
 console.log('You got a C');
} else {
 console.log('You failed! You need to study more!');
}

Ternary Operator: This operator is often used as a shorter way to write if else statements.
三元运算符：这个运算符通常被用作一种更简洁的方式来编写条件语句。

const temperature = 30;
const weather = temperature > 25 ? 'sunny' : 'cool';

console.log(`It's a ${weather} day!`); // It's a sunny day!

## Binary Logical Operators 二进制逻辑运算符

Logical AND (&&) Operator: This operator checks if both operands are true. If both are true, then it will return the second value. If either operand is falsy, then it will return the falsy value. If both operands are falsy, it will return the first falsy value.
逻辑与（ && ）运算符：该运算符检查两个操作数是否都为 true 。如果两个操作数都是 true ，则返回第二个值。如果任一操作数为 falsy ，则返回 falsy 值。如果两个操作数都是 falsy ，则返回第一个 falsy 值。

const result = true && 'hello';
console.log(result); // hello

Logical OR (||) Operator: This operator checks if at least one of the operands is truthy. 
逻辑或（ || ）运算符：该运算符检查至少有一个操作数为真值。
Nullish Coalescing (??) Operator: This operator will return a value only if the first one is null or undefined.
空值合并（ ?? ）运算符：这个运算符只有在第一个值为 null 或 undefined 时才会返回值。

const userSettings = {
 theme: null,
 volume: 0,
 notifications: false,
};

let theme = userSettings.theme ?? 'light';
console.log(theme); // light

## The Math Object   Math 对象

The Math.random() Method: This method generates a random floating-point number between 0 (inclusive) and 1 (exclusive). This means the possible output can be 0, but it will never actually reach 1.
Math.random() 方法：这个方法生成一个在 0（包含）和 1（不包含）之间的随机浮点数。这意味着可能的输出可以是 0，但它实际上永远不会达到 1。
The Math.max() Method: This method takes a set of numbers and returns the maximum value.
Math.max() 方法：这个方法接收一组数字并返回最大值。
The Math.min() Method: This method takes a set of numbers and returns the minimum value.
Math.min() 方法：这个方法接收一组数字并返回最小值。
The Math.ceil() Method: This method rounds a value up to the nearest whole integer.
Math.ceil() 方法：这个方法将一个值向上舍入到最近的整数。
The Math.floor() Method: This method rounds a value down to the nearest whole integer.
Math.floor() 方法：此方法将值向下舍入到最近的整数。
The Math.round() Method: This method rounds a value to the nearest whole integer.
Math.round() 方法：此方法将值四舍五入到最接近的整数。

console.log(Math.round(2.3)); // 2
console.log(Math.round(4.5)); // 5
console.log(Math.round(4.8)); // 5

The Math.trunc() Method: This method removes the decimal part of a number, returning only the integer portion, without rounding.
Math.trunc() 方法：此方法移除数字的小数部分，只返回整数部分，不进行四舍五入。
The Math.sqrt() Method: This method will return the square root of a number.
Math.sqrt() 方法：此方法将返回一个数的平方根。
The Math.cbrt() Method: This method will return the cube root of a number.
Math.cbrt() 方法：这个方法将返回一个数的立方根。
The Math.abs() Method: This method will return the absolute value of a number.
Math.abs() 方法：这个方法将返回一个数的绝对值。
The Math.pow() Method: This method takes two numbers and raises the first to the power of the second.
Math.pow() 方法：这个方法接受两个数，并将第一个数提升到第二个数的幂。

## Common Number Methods  常见的数字方法

isNaN(): NaN stands for "Not-a-Number". It's a special value that represents an unrepresentable or undefined numerical result. The isNaN() function property is used to determine whether a value is NaN or not. Number.isNaN() provides a more reliable way to check for NaN values, especially in cases where type coercion might lead to unexpected results with the global isNaN() function.
isNaN() : NaN 代表 "非数字"。它是一个特殊值，表示无法表示或未定义的数值结果。 isNaN() 函数属性用于判断一个值是否为 NaN 。 Number.isNaN() 提供了一种更可靠的方法来检查 NaN 值，特别是在全局 isNaN() 函数可能导致类型转换产生意外结果的情况下。

console.log(isNaN(NaN));       // true
console.log(isNaN(undefined)); // true
console.log(isNaN({}));        // true

console.log(isNaN(true));      // false
console.log(isNaN(null));      // false
console.log(isNaN(37));        // false


console.log(Number.isNaN(NaN));        // true
console.log(Number.isNaN(Number.NaN)); // true
console.log(Number.isNaN(0 / 0));      // true

console.log(Number.isNaN("NaN"));      // false
console.log(Number.isNaN(undefined));  // false

The parseFloat() Method: This method parses a string argument and returns a floating-point number. It's designed to extract a number from the beginning of a string, even if the string contains non-numeric characters later on.
parseFloat() 方法：这个方法解析一个字符串参数并返回一个浮点数。它被设计用来从字符串的开头提取一个数字，即使字符串后面包含非数字字符。
The parseInt() Method: This method parses a string argument and returns an integer. parseInt() stops parsing at the first non-digit it encounters. For floating-point numbers, it returns only the integer part. If it can't find a valid integer at the start of the string, it returns NaN.
parseInt() 方法：这个方法解析一个字符串参数并返回一个整数。 parseInt() 在遇到第一个非数字时停止解析。对于浮点数，它只返回整数部分。如果它在字符串开头找不到有效的整数，则返回 NaN 。
The toFixed() Method: This method is called on a number and takes one optional argument, which is the number of digits to appear after the decimal point. It returns a string representation of the number with the specified number of decimal places.
toFixed() 方法：这个方法作用于一个数字，并可以接受一个可选参数，即小数点后要显示的位数。它返回一个具有指定小数位数的数字的字符串表示。