# Working with Comparison and Boolean Operators, Not started
In these lectures you will learn about booleans, and equality and inequality operators, and other comparison operators.

## What Are Booleans, and How Do They Work with Equality and Inequality Operators?
什么是布尔值，以及它们如何与相等和不等运算符一起工作？
In an earlier lecture, you were first introduced to the concept of booleans, but in this lecture, we will dive deeper into how booleans work and how the equality and inequality operators work.
在之前的讲座中，你已经首次接触到了布尔值的概念，但在本次讲座中，我们将深入探讨布尔值的工作原理以及相等和不等运算符的工作方式。

Booleans are a data type with only true and false values. They're useful because they allow you to do something based on some conditions. Booleans are essential when you want to evaluate whether something should happen or not, like deciding if someone can access a certain feature in your app. Here is an example of setting the value true to a variable called isOldEnoughToDrive:
布尔值是一种只有 true 和 false 值的数据类型。它们很有用，因为它们允许你根据某些条件执行操作。当你想要评估某事是否应该发生时，布尔值是必不可少的，比如决定是否允许用户访问你的应用中的某个功能。这里是一个将值 true 赋给名为 isOldEnoughToDrive 的变量的示例：

let isOldEnoughToDrive = true;

console.log(isOldEnoughToDrive); // true
You can use this variable inside a conditional like this:
你可以在条件语句中使用这个变量，如下所示：

let isOldEnoughToDrive = true;

if (isOldEnoughToDrive) {
 console.log("You're old enough to drive"); // You're old enough to drive
} else {
 console.log("Sorry, you are not old enough to drive");
}
A conditional helps you make decisions in your code based on a condition. This example uses what is called an if/else statement.
一个条件语句能帮助你在代码中根据条件做出决策。这个例子使用了所谓的 if/else 语句。

If isOldEnoughToDrive is true, then the sentence You're old enough to drive will be logged to the console. Otherwise, if the isOldEnoughToDrive is false, then the sentence Sorry, you are not old enough to drive will be logged to the console. Since the isOldEnoughToDrive variable is set to true, the first sentence will be logged to the console. You will learn more about if/else statements in a future lecture.
如果 isOldEnoughToDrive 是 true ，那么句子 You're old enough to drive 将被记录到控制台。否则，如果 isOldEnoughToDrive 是 false ，那么句子 Sorry, you are not old enough to drive 将被记录到控制台。由于 isOldEnoughToDrive 变量被设置为 true ，第一句话将被记录到控制台。你将在未来的讲座中了解更多关于 if/else 语句的内容。

To compare two values, you can use either the equality or strict equality operator. The result of the comparison will be a boolean of either true or false. Here is an example of using the equality operator to compare a string and a number. The equality operator is represented by a double equals sign (==).
要比较两个值，你可以使用相等运算符或严格相等运算符。比较的结果将是一个 true 或 false 的布尔值。这里是一个使用相等运算符比较字符串和数字的例子。相等运算符用两个等号（ == ）表示。

console.log(5 == "5"); // true
In this example, JavaScript converts the string "5" into the number 5 and then checks if they are equal. Since both values are now the same, the result is true. The equality operator uses type coercion before checking if each value is equal.
在这个例子中，JavaScript 将字符串 "5" 转换为数字 5 ，然后检查它们是否相等。由于这两个值现在相同，结果是 true。相等运算符在检查每个值是否相等之前会进行类型转换。

This differs from the strict equality operator, which does not perform type coercion. The strict equality operator will check if the types are the same and if the values are the same. Here is an example using the strict equality operator to compare a number and string. This operator is represented by a triple equals sign (===).
这与严格相等运算符不同，后者不会执行类型转换。严格相等运算符会检查类型是否相同以及值是否相同。这里是一个使用严格相等运算符比较数字和字符串的例子。该运算符用三个等号（ === ）表示。

console.log(5 === '5'); // false
The following comparison will be false, because a string data type is not the same as a number data type. If you need to check if something is not equal to another value, then you can use the inequality or strict inequality operators. Here is an example of using the inequality operator (!=) to compare a number with a string.
接下来的比较将是 false ，因为字符串数据类型与数字数据类型不相同。如果你需要检查某个值是否不等于另一个值，那么你可以使用不等运算符或严格不等运算符。这里是一个使用不等运算符（ != ）比较数字和字符串的例子。

console.log(5 != "5"); // false
In this example, the result would be false because the inequality operator first converts the string value to a number and then compares the values. Since the values would be the same it will return false. If you tried to use the strict inequality operator, then you would get a different result. The strict inequality operator is represented by an exclamation mark followed by two equal signs (!==).
在这个例子中，结果将是 false ，因为不等运算符首先将字符串值转换为数字，然后比较值。由于值相同，它将返回 false 。如果你尝试使用严格不等运算符，那么你会得到不同的结果。严格不等运算符用感叹号后跟两个等号（ !== ）表示。

console.log(5 !== "5"); // true
The result would be true because the strict inequality operator does not perform any type coercion. Since the number 5 is not equal to the string "5", then the result is true.
结果将是 true ，因为严格不等式运算符不会执行任何类型转换。由于数字 5 不等于字符串 "5" ，因此结果是 true 。

It is considered best practice to use strict inequality and equality operators whenever possible, as they do not perform type coercion. Most of the time in professional projects, you will see codebases that usually prefer these two operators over the inequality and equality operators.
在可能的情况下，使用严格不等式和等式运算符被认为是最佳实践，因为它们不会执行类型转换。在大多数专业项目中，你通常会看到代码库更倾向于使用这两个运算符而不是不等式和等式运算符。

## What Are Comparison Operators, and How Do They Work?
比较运算符是什么，它们是如何工作的？
Comparison operators allow you to compare two values and return a true or false result. You can then use the result to make a decision or control the flow of your program. You use comparisons in if statements, loops, and many other situations where you need to make decisions based on certain conditions. Let's dive into the most common comparison operators and see how they work.
比较运算符允许你比较两个值并返回 true 或 false 的结果。你可以使用这个结果来做出决策或控制程序的流程。你在 if 语句、循环以及其他需要根据特定条件做出决策的情况下使用比较运算符。让我们深入了解最常见的比较运算符以及它们的工作原理。

The greater than operator, represented by a right-angle bracket (>), checks if the value on the left is greater than the one on the right:
大于运算符，用右尖括号（ > ）表示，检查左边的值是否大于右边的值：

let a = 6;
let b = 9;

console.log(a > b); // false
console.log(b > a); // true
The greater than or equal operator, represented by a right-angle bracket and the equals sign (>=), checks if the value on the left is either greater than or equal to the one on the right:
大于等于运算符，用右尖括号和等号（ >= ）表示，检查左边的值是否大于或等于右边的值：

let a = 6;
let b = 9;
let c = 6;

console.log(a >= b); // false
console.log(b >= a); // true
console.log(a >= c); // true
The lesser than operator, represented by a left-angle bracket (<) works similarly to >, but in reverse. It checks if the value on the left is smaller than the one on the right:
小于运算符，用左尖括号（ < ）表示，与 > 类似但方向相反。它检查左边的值是否小于右边的值：

let a = 6;
let b = 9;

console.log(a < b); // true
console.log(b < a); // false
The less than or equal operator, represented by a left-angle bracket and the equals sign (<=) checks if the value on the left is smaller than or equal to the one on the right:
小于或等于运算符，用左尖括号和等号（ <= ）表示，用于检查左边的值是否小于或等于右边的值：

let a = 6;
let b = 9;
let c = 6;

console.log(a <= b); // true
console.log(b <= a); // false
console.log(a <= c); // true
