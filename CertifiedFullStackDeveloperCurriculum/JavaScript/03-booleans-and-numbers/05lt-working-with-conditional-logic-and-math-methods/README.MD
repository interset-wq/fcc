# Working with Conditional Logic and Math Methods, Not started
In these lectures you will learn about conditional statements, binary logical operators, and the Math object.

## What Are Conditional Statements, and How Do If/Else If/Else Statements Work?
什么是条件语句，以及 If/Else If/Else 语句是如何工作的？
Conditional statements let you make decisions in your JavaScript code. They allow your program to flow in a particular way based on certain conditions. Let's take a look at how if, else if, else, and the ternary operator work to let you control the flow of your code.
条件语句让你能在 JavaScript 代码中做出决策。它们允许你的程序根据特定条件以特定方式运行。让我们看看 if 、 else if 、 else 以及三元运算符是如何工作的，以让你控制代码的流程。

An if statement takes a condition and runs a block of code if that condition is truthy. Truthy values are any values that result in true when evaluated in a Boolean context like an if statement. Here are examples of truthy values:
一个 if 语句会检查一个条件，如果这个条件为真，就会运行一个代码块。在布尔上下文中（比如一个 if 语句）被评估为 true 的任何值都是真值。以下是一些真值的例子：

non-empty strings, for example, hello
非空字符串，例如 hello

any number other than 0 and -0, for example, 4, -5, and others
任何不是 0 和 -0 的数字，例如 4 、 -5 等

arrays  数组

objects  对象

the boolean true  布尔值 true

On the other hand, falsy values are values that evaluate to false in a boolean context. JavaScript has few falsy values, which makes them easy to remember. Here are a few falsy values:
另一方面，假值是在布尔上下文中求值为 false 的值。JavaScript 中的假值很少，这使得它们容易记忆。以下是一些假值：

boolean false

0 (zero)   0 (零)

"" (empty string)   "" (空字符串)

null

undefined

NaN (Not a Number)   NaN (非数字)

Now, that we have a basic understanding of truthy and falsy values, let's see how it works with if statements. In this first example, we are using a couple of if statements to check against truthy and falsy values:
现在，我们已经对真值和假值有了基本的了解，让我们看看 if 语句是如何工作的。在这个第一个例子中，我们使用了一些 if 语句来检查真值和假值：

if (null) {
  console.log("This will not run.");
}

if ("freeCodeCamp") {
  console.log("This will run.");
}
Since null is a falsy value, the message inside the block will never be logged to the console. But for the second if statement, the string freeCodeCamp is a truthy value, and will be considered true in this boolean context of the if statement. As a result, the message This will run. will be logged to the console.
由于 null 是一个假值，块内的消息永远不会被记录到控制台。但对于第二个 if 语句，字符串 freeCodeCamp 是真值，在这个 if 语句的布尔上下文中将被视为 true 。因此，消息 This will run. 将被记录到控制台。

Let's take a look at a few more examples on how if statements work with different comparison operators. Here is an example of using an if statement to check if the user is eligible to vote:
让我们看看 if 语句如何与不同的比较运算符一起使用的一些更多例子。这里有一个使用 if 语句来检查用户是否有资格投票的例子：

const age = 22;

if (age >= 18) {
 console.log("You're eligible to vote"); // You're eligible to vote
}
In this example, since age is currently 22, this means the condition will evaluate to true because 22 is greater than or equal to 18. So the message You're eligible to vote will be logged to the console. If we change the example so age is now 15, then the condition will evaluate to false and the message will not be logged to the console:
在这个例子中，由于 age 目前是 22 ，这意味着条件将评估为 true ，因为 22 大于或等于 18 。所以消息 You're eligible to vote 将被记录到控制台。如果我们更改示例，使 age 现在是 15 ，那么条件将评估为 false ，消息将不会被记录到控制台：

const age = 15;

if (age >= 18) {
 console.log("You're eligible to vote"); // Code not running because age is less than 18
}
When a condition is false, then you can use an else clause:
当条件是 false 时，你可以使用一个 else 子句：

const age = 15;

if (age >= 18) {
 console.log("You're eligible to vote");
} else {
 console.log("You're not eligible to vote"); // You're not eligible to vote
}
In this example, 15 is not greater than or equal to 18, so the condition would be false. The code inside the else block will run in this case.
在这个例子中， 15 不大于或等于 18 ，所以条件将是 false 。在这种情况下， else 块内的代码将运行。

If you want to check multiple conditions, you can use an else if block. This allows your program to choose between more than two paths.
如果你要检查多个条件，你可以使用一个 else if 块。这允许你的程序在两个以上的路径之间进行选择。

const score = 87;

if (score >= 90) {
 console.log('You got an A'); 
} else if (score >= 80) {
 console.log('You got a B'); // You got a B
} else if (score >= 70) {
 console.log('You got a C');
} else {
 console.log('You failed! You need to study more!');
}
Since the score is currently 87, then the message of You got a B would be logged to the console.
由于当前 score 为 87 ，则 You got a B 的消息将被记录到控制台。

The ternary operator is a compact way to write simple if/else statements. It has three parts: a condition, a result if the condition is true, and a result if it is false. Here's the basic syntax:
三元运算符是一种简洁地编写简单条件语句的方式。它包含三个部分：一个条件、条件为真时的结果以及条件为假时的结果。以下是基本语法：

condition ? expressionIfTrue : expressionIfFalse;
Here's an example dealing with weather temperatures in Celsius:
这里有一个处理摄氏温度的例子：

const weather = temperature > 25 ? 'sunny' : 'cool';

console.log(`It's a ${weather} day!`);
If temperature is greater than 25, the code above logs It's a sunny day!. If temperature is ever less than 25, it logs It's a cool day!.
如果 temperature 大于 25 ，上面的代码会记录 It's a sunny day! 。如果 temperature 任何时候小于 25 ，它会记录 It's a cool day! 。

So, which should you use between an if statement and a ternary? Use a ternary while dealing with a single condition or single expressions, or when you want a compact syntax for simple logic. Use if/else statements when you're dealing with complex conditions and multiple statements, as things become unreadable if you nest ternaries. 
那么，在条件语句和三元运算符之间，你应该选择哪一个？当你处理单个条件或单个表达式，或者当你想要简洁的语法来表示简单逻辑时，使用三元运算符。当你处理复杂条件和多个语句时，使用条件语句，因为嵌套三元运算符会使代码变得难以阅读。

## What Are Binary Logical Operators, and How Do They Work?
什么是二元逻辑运算符，它们是如何工作的？
Binary logical operators help you evaluate two expressions and return a result based on their truthiness. Let's look at the three most common binary logical operators: logical AND, logical OR, and the nullish coalescing operator.
二元逻辑运算符帮助你评估两个表达式，并根据它们的真值返回结果。让我们看看三种最常见的二元逻辑运算符：逻辑与、逻辑或和空合并运算符。

The logical AND operator is represented by a double ampersand (&&). It checks if both operands are true and returns a result. If both operands are truthy, it returns the second value, that is, the one on the right:
逻辑与运算符用两个与号（ && ）表示。它检查两个操作数是否都为真，并返回结果。如果两个操作数都为真值，它返回第二个值，即右边的那个：

const result = true && 'hello';

console.log(result); // hello
In the example above, the text hello is logged to the console because both operands are true. If either operand is falsy, it returns the falsy value:
在上面的示例中，文本 hello 被记录到控制台，因为两个操作数都为 true 。如果任何一个操作数为假值，它返回假值：

const result = 0 && 3;

console.log(result); // 0
Since 0 is a falsy value, the number 0 is logged to the console. And if both operands are falsy, it returns the first falsy value:
由于 0 是一个假值， 0 会被记录到控制台。如果两个操作数都是假值，它会返回第一个假值：

const result = false && 0;

console.log(result); // false
Since false is a falsy value, then false is logged to the console. The logical AND operator is useful when you want to check multiple conditions and ensure that all are true before proceeding. Here is an example:
由于 false 是一个假值， false 会被记录到控制台。逻辑与运算符在你想要检查多个条件并确保所有条件都为真后再继续时非常有用。这里有一个例子：

if (2 < 3 && 3 < 4) {
 console.log('The if block runs'); 
} else {
 console.log('The else block runs');
} 
In the condition, since 2 is less than 3 AND 3 is less than 4, then the sentence The if block runs will be logged to the console.
在条件中，由于 2 小于 3 并且 3 小于 4 ， The if block runs 这句话会被记录到控制台。

The logical OR operator checks if at least one of the operands is truthy. If the first operand is truthy, it returns that value:
逻辑或运算符检查至少有一个操作数为真值。如果第一个操作数为真值，它会返回该值：

const result = 'This is truthy' || false;

console.log(result); // This is truthy
If the first operand is falsy but the second is truthy, the second value will be logged to the console:
如果第一个操作数是假值但第二个是真值，则第二个值将被记录到控制台：

const result = 0 || 'This is truthy';

console.log(result); // This is truthy
It is common to use the logical OR operator in if/else statements like this:
在 if/else 语句中常用逻辑或运算符，如下所示：

let userInput;

if (userInput || 'Guest') {
 console.log('A user is present');
} else {
 console.log('No user detected');
}
Since we didn't assign a value to the userInput variable, it is currently undefined. The condition in the if statement checks if either the userInput variable or the string Guest are truthy. Since the string Guest is true in a boolean context like this, the string A user is present will be logged to the console.
由于我们没有为 userInput 变量赋值，它目前是 undefined 。 if 语句中的条件检查 userInput 变量或字符串 Guest 是否为真值。由于在布尔上下文中字符串 Guest 为真，因此字符串 A user is present 将被记录到控制台。

The nullish coalescing operator is more sophisticated than logical OR and logical AND. Represented by a double question mark (??), it helps in scenarios where you want to return a value only if the first one is null or undefined. Here is an example of working with the nullish coalescing operator:
空值合并运算符比逻辑或和逻辑与更复杂。用双问号（ ?? ）表示，它用于在第一个操作数为 null 或 undefined 时才返回值的场景。以下是使用空值合并运算符的示例：

const result = null ?? 'default';

console.log(result); // default
Since null is a falsy value, the string default would be logged to the console. The nullish coalescing operator is incredibly useful in situations where null or undefined are the only values that should trigger a fallback or default value. Here is an example of dealing with a user's preference settings:
由于 null 是一个假值，字符串 default 将会被记录到控制台。空值合并运算符在 null 或 undefined 是唯一应该触发回退或默认值的场景中非常实用。这里有一个处理用户偏好设置的例子：

const userSettings = {
 theme: null,
 volume: 0,
 notifications: false,
};

let theme = userSettings.theme ?? 'light';
console.log(theme); // light
In the example above, we have an object called userSettings that contains theme, volume and notifications properties. We are accessing the theme using dot notation like userSettings.theme. You will learn more about how to work with objects in a future lecture. Since the user's theme is currently set to null, then the string light will be logged to the console.
在上面的示例中，我们有一个名为 userSettings 的对象，它包含 theme 、 volume 和 notifications 属性。我们使用点表示法访问 theme ，就像 userSettings.theme 一样。你将在未来的讲座中了解更多关于如何操作对象的内容。由于用户的 theme 目前设置为 null ，因此字符串 light 将被记录到控制台。

## What Is the Math Object in JavaScript, and What Are Some Common Methods?
JavaScript 中的 Math 对象是什么，以及有哪些常见方法？
When diving into JavaScript, you'll quickly discover that performing mathematical operations is a common task. While basic arithmetic operators can handle simple calculations, JavaScript offers a built-in Math object to tackle more complex math challenges.
在深入 JavaScript 时，你会发现执行数学运算是一个常见的任务。虽然基本的算术运算符可以处理简单的计算，但 JavaScript 提供了一个内置的 Math 对象来应对更复杂的数学挑战。

This handy tool provides a variety of methods that make it easier to perform advanced calculations and manipulate numbers. Let's explore these methods and see how they can simplify your coding experience.
这个实用的工具提供了多种方法，使执行高级计算和操作数字变得更加容易。让我们探索这些方法，看看它们如何简化你的编码体验。

The Math.random() method generates a random floating-point number between 0 (inclusive) and 1 (exclusive). This means the possible output can be 0, but it will never actually reach 1. Here is an example working with the Math.random() method:
Math 方法生成一个介于 0 （包含）和 1 （不包含）之间的随机浮点数。这意味着可能的输出可以是 0 ，但它永远不会实际达到 1 。以下是使用 Math 方法的一个示例：

const randomNum = Math.random();

console.log(randomNum); 
// any number between 0 and 1 – 0 inclusive and 1 exclusive
Math.min() and Math.max() both take a set of numbers and return the minimum and maximum value, respectively. Here is an example of working both of those methods:
Math.min() 和 Math.max() 都接受一组数字，并分别返回最小值和最大值。以下是使用这两个方法的示例：

const smallest = Math.min(1, 5, 3, 9);
console.log(smallest); // 1

const largest = Math.max(1, 5, 3, 9);
console.log(largest); // 9
The first console.log() will log the number 1, since 1 is the smallest in that list of numbers. And the second console.log() will log the number 9, since 9 is the largest numbers in that list.
第一个 console.log() 将记录数字 1 ，因为 1 是该数字列表中最小的。第二个 console.log() 将记录数字 9 ，因为 9 是该数字列表中最大的。

If you wanted to round numbers up or down to the nearest whole integer, you could use the Math.ceil() and Math.floor() methods. Here is an example of working with Math.ceil():
如果你想将数字向上或向下舍入到最接近的整数，你可以使用 Math.ceil() 和 Math.floor() 方法。以下是使用 Math.ceil() 的示例：

console.log(Math.ceil(4.3)); // 5
Math.ceil() will round 4.3 up to the nearest whole integer, which is 5 in this case. Now, let's take a look at rounding a number down:
Math.ceil() 将 4.3 向上舍入到最接近的整数，在这个例子中是 5 。现在，让我们看看向下舍入一个数字：

console.log(Math.floor(4.7)); // 4
Math.floor() will round 4.7 down to the nearest whole integer, which is 4 in this case. Math.round() is the hybrid of Math.ceil() and Math.floor(). It rounds a number to its nearest integer, taking the decimal point into account:
Math.floor() 将 4.7 向下舍入到最近的整数，在本例中是 4 。 Math.round() 是 Math.ceil() 和 Math.floor() 的结合。它将一个数舍入到最近的整数，同时考虑小数点：

console.log(Math.round(2.3)); // 2
console.log(Math.round(4.5)); // 5
console.log(Math.round(4.8)); // 5
So, if the decimal point is less than 5, the number is rounded down. And if the decimal point is 5 or greater, the number is rounded up. A practical application of Math.floor() and Math.random() is to generate a random number between two whole numbers. Here's the syntax for that:
因此，如果小数点小于 5 ，则该数向下舍入。如果小数点等于或大于 5 ，则该数向上舍入。 Math.floor() 和 Math.random() 的一个实际应用是生成两个整数之间的随机数。以下是该语法：

Math.floor(Math.random() * (max - min)) + min;
Generating a random number between 20 and 1 would look like this:
生成 20 和 1 之间的随机数看起来像这样：

const randomNumBtw1And20 = Math.floor(Math.random() * 20) + 1;
console.log(randomNumBtw1And20); 
Another helpful Math method would be the Math.trunc() method. Math.trunc() removes the decimal part of a number, returning only the integer portion, without rounding:
另一个有用的 Math 方法是 Math.trunc() 方法。 Math.trunc() 去除一个数的小数部分，只返回整数部分，但不进行舍入：

console.log(Math.trunc(2.9)); // 2
console.log(Math.trunc(9.1)); // 9
If you need to get the square root or cube root of a number, you can use the Math.sqrt() and Math.cbrt() methods, respectively:
如果你需要获取一个数的平方根或立方根，你可以分别使用 Math.sqrt() 和 Math.cbrt() 方法：

console.log(Math.sqrt(81)); // 9
console.log(Math.cbrt(27)); // 3
The first log statement, will log 9 because the square root of 81 is 9, while the second log statement will log 3 because the cube root of 27 is 3. If you need to get the absolute value of a number, you can use the Math.abs() method:
第一个日志语句会记录 9 ，因为 81 的平方根是 9 ，而第二个日志语句会记录 3 ，因为 27 的立方根是 3 。如果你需要获取一个数的绝对值，你可以使用 Math.abs() 方法：

console.log(Math.abs(-5)); // 5
console.log(Math.abs(5)); // 5
Math.abs() returns the absolute value of a number, turning negatives into positives. The last method we will look at will be the Math.pow() method:
Math.abs() 返回一个数的绝对值，将负数转换为正数。我们将要看的最后一个方法是 Math.pow() 方法：

console.log(Math.pow(2, 3)); // 8
console.log(Math.pow(8, 2)); // 64
Math.pow() takes two numbers and raise the first to the power of the second. There are many more methods that belong to the Math object, that you can explore on your own. However, these are just a few of the more commonly used ones found in JavaScript codebases.
Math.pow() 接收两个数字，并将第一个数字提升到第二个数字的幂。 Math 对象还有许多其他方法，你可以自行探索。然而，这些只是 JavaScript 代码库中一些更常用的方法。