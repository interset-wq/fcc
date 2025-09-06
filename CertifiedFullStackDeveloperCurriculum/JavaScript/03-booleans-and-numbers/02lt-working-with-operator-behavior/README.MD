# Working with Operator Behavior, Not started
In these lectures you will learn about operator precedence, the increment and decrement operators, and compound assignment operators.

## How Does Operator Precedence Work?
运算符优先级是如何工作的？
If you write an expression with several operators in JavaScript, how does JavaScript decide which one to evaluate first? This is where operator precedence comes in. Let's explore operator precedence in detail with code examples, and also what happens when operators have the same precedence.
如果你在 JavaScript 中写了一个包含多个操作符的表达式，JavaScript 是如何决定先求值哪一个呢？这就是操作符优先级发挥作用的地方。让我们通过代码示例详细探讨操作符优先级，以及当操作符具有相同优先级时会发生什么。

Operator precedence determines the order in which operations are evaluated in an expression. Operators with higher precedence are evaluated before those with lower precedence. Think of operator precedence like in math, where division and multiplication happen before addition and subtraction.
操作符优先级决定了表达式中操作的求值顺序。优先级高的操作符会先于优先级低的操作符被求值。可以像在数学中那样理解操作符优先级，其中除法和乘法会先于加法和减法进行。

Without following this rule, basic equations would give you the wrong answer. JavaScript works the same way. It has its own rules for which operators come first, second, and so on. For example, take a look at the expression below:
如果不遵循这个规则，基本的方程式会给你错误的答案。JavaScript 也是这样工作的。它有自己的规则来决定哪些运算符优先级更高、其次等等。例如，看看下面的表达式：

const result = 2 + 3 * 4;

console.log(result); // 14
If JavaScript evaluated this expression from left to right, you'd expect 2 + 3 = 5, then 5 * 4 = 20. But because multiplication has a higher precedence than addition, JavaScript evaluates the 3 * 4 part first, resulting in 2 + 12 = 14.
如果 JavaScript 从左到右计算这个表达式，你期望得到 2 + 3 = 5 ，然后是 5 * 4 = 20 。但由于乘法比加法有更高的优先级，JavaScript 会先计算 3 * 4 部分，结果得到 2 + 12 = 14 。

Sometimes, you may want certain parts of your expression to run first, regardless of precedence rules. You can use parentheses, (), to do this. Anything inside parentheses is evaluated first, no matter what. Let's make the 2 + 3 part of the previous example evaluate first:
有时，你可能希望某些部分的表达式先执行，而不管优先级规则如何。你可以使用括号， () ，来实现这一点。括号内的任何内容都会首先被评估，无论什么情况。让我们让之前的示例中的 2 + 3 部分先执行：

const result = (2 + 3) * 4;

console.log(result); // 20
In the example above, the parentheses force JavaScript to evaluate 2 + 3 first, and then multiply the result by 4. This gives you 20 instead of 14.
在上面的例子中，括号迫使 JavaScript 先计算 2 + 3 ，然后再将结果乘以 4 。这会给你 20 而不是 14 。

The division operator has more precedence than addition or subtraction too:
除法运算符的优先级也比加法或减法高：

const result = 2 + 6 / 3;

console.log(result); // 4
If JavaScript evaluated this expression from left to right, you might expect 2 + 6 = 8, then 8 / 3 = 2.67. But since division has a higher precedence than addition, JavaScript evaluates the division first: 6 / 3 = 2, and then adds 2 + 2, giving the result 4.
如果 JavaScript 从左到右计算这个表达式，你可能会期望 2 + 6 = 8 ，然后是 8 / 3 = 2.67 。但由于除法的优先级比加法高，JavaScript 会先计算除法： 6 / 3 = 2 ，然后加上 2 + 2 ，得到结果 4 。

So, in both multiplication and division, those operations will always take place before addition and subtraction unless you use parentheses to change the order. So what happens if the operators have the same precedence? JavaScript uses associativity to figure out the order to evaluate them.
所以，在乘法和除法中，这些运算总是会在加法和减法之前进行，除非你使用括号来改变运算顺序。那么如果运算符具有相同的优先级呢？JavaScript 使用关联性来确定它们的计算顺序。

Associativity is what tells JavaScript whether to evaluate operators from left to right or right to left. For most operators like addition and multiplication, associativity is left to right. So, JavaScript processes these from the leftmost side of the expression to the right:
关联性告诉 JavaScript 是从左到右还是从右到左来计算运算符。对于大多数运算符，如加法和乘法，关联性是从左到右。所以，JavaScript 会从表达式的最左侧开始向右处理：

const result = 10 - 2 + 3;

console.log(result); // 11
First, 10 - 2 = 8, then 8 + 3 = 11. JavaScript moves left to right in this case. Some operators, like assignment (=), are right-to-left associative. This means the right side of the expression gets evaluated first:
首先处理 10 - 2 = 8 ，然后处理 8 + 3 = 11 。在这种情况下，JavaScript 会从左到右移动。有些运算符，如赋值（ = ），是从右到左关联的。这意味着表达式的右侧会先被计算：

let a, b;
a = b = 5;

console.log(a); // 5
console.log(b); // 5
console.log(a + b); // 10
In the example above, JavaScript assigns 5 to b first, then assigns b (which is now 5) to a.
在上述示例中，JavaScript 首先将 5 赋值给 b ，然后将 b （现在是 5 ）赋值给 a 。

The exponent operator is also right-to-left associative:
指数运算符也是从右到左结合的：

const result = 2 ** 3 ** 2;

console.log(result); // 512
First, JavaScript evaluates 3 ** 2, which equals 9, then, it evaluates 2 ** 9, which equals 512. If the exponent operator had left-to-right associativity, JavaScript would have calculated 2 ** 3 first to get 8, then 8 ** 2 to get 64. 
首先，JavaScript 计算 3 ** 2 ，等于 9 ，然后计算 2 ** 9 ，等于 512 。如果指数运算符是从左到右结合的，JavaScript 会先计算 2 ** 3 得到 8 ，然后计算 8 ** 2 得到 64 。

## How Do the Increment and Decrement Operators Work?
增量与减量运算符是如何工作的？
If you're working with numbers and need to increase or decrease a value by one, the increment and decrement operators make the job easier. Let's break it down in a simple way.
如果你在处理数字并需要将值增加或减少 1，增量与减量运算符可以让这项工作更简单。让我们用简单的方式解释一下。

The increment and decrement operators are represented by ++ and --, respectively. They both allow you to adjust the value of a variable by 1.
增量与减量运算符分别用 ++ 和 -- 表示。它们都允许你通过 1 调整变量的值。

Instead of writing something like x = x + 1 or x = x - 1, you can simply use x++ to add 1, or x-- to subtract 1. It's faster, cleaner, and easier to read.
你不必写 x = x + 1 或 x = x - 1 ，只需使用 x++ 来增加 1 ，或使用 x-- 来减少 1 。这样更快速、更简洁、更易读。

There's a twist to how the increment and decrement operators work: they come in two forms, prefix and postfix, with the difference being when the value gets updated. For the increment operator, prefix is ++x and postfix is x++.
增量运算符和减量运算符的工作方式有一个特点：它们有两种形式，前缀和后缀，区别在于何时更新值。对于增量运算符，前缀是 ++x ，后缀是 x++ 。

Prefix (++x) increases the value of the variable first, then returns a new value. Postfix (x++) returns the current value of the variable first, then increases it:
前缀（ ++x ）先增加变量的值，然后返回新值。后缀（ x++ ）先返回变量的当前值，然后增加它：

let x = 5;

console.log(++x); // 6
console.log(x); // 6
In the code above, ++x means "increment x first, then use it". So when you log ++x, you immediately get the incremented value, which is 6.
在上述代码中， ++x 表示“先增量 x ，然后使用它”。所以当你记录 ++x 时，你会立即得到增量后的值，即 6 。

Now, let's take a look at an example using the postfix:
现在，让我们来看一个使用后缀的例子：

let y = 5;

console.log(y++); // 5
console.log(y); // 6
In this example, y++ means "use y first, then increment it". When you log y++, you get 5, but y becomes 6 after that line of code.
在这个例子中， y++ 表示“先使用 y ，然后递增它”。当你记录 y++ 时，你会得到 5 ，但在那行代码之后 y 会变成 6 。

The decrement operator does the same thing as increment, except it decreases the value by 1. Again, there are two forms: prefix (--x) decreases the value of the variable first, then returns the new value. And postfix (x--) returns the current value first, then decreases it:
递减运算符与递增运算符做相同的事情，只是它会减少 1 的值。同样，有两种形式：前缀（ --x ）先减少变量的值，然后返回新值。后缀（ x-- ）先返回当前值，然后减少它：

let x = 5;
console.log(--x); // 4
console.log(x); // 4

let y = 5;
console.log(y--); // 5
console.log(y); // 4
So, which should you use: prefix or postfix? In many cases, it doesn't matter which one you use. Both get the job done. However, if you're using the value immediately in an expression, the difference becomes important. Let's take a look at this example:
那么，你应该使用前缀还是后缀呢？在许多情况下，使用哪一个并不重要。两者都能完成任务。然而，如果你在表达式中立即使用该值，那么差异就变得重要了。让我们来看这个例子：

let a = 5;
let b = ++a;
console.log(b); // 6 (a was incremented before assignment)

let c = 5;
let d = c++;
console.log(d); // 5 (c was incremented after assignment)
So, if you need the updated value right away, use prefix. If you want the current value first and you don’t care about the increment until later, go with postfix.
所以，如果你需要立即获取更新后的值，使用前缀。如果你先想获取当前值，并且不关心直到稍后才需要递增，那么选择后缀。

## What Are Compound Assignment Operators in JavaScript, and How Do They Work?
JavaScript 中的复合赋值运算符是什么，它们是如何工作的？
In JavaScript, all arithmetic operators have a compound assignment form. Compound assignment operators allow you to perform a mathematical operation and reassign the result back to the variable in one line of code. Instead of writing something like this:
在 JavaScript 中，所有算术运算符都有复合赋值形式。复合赋值运算符允许你在一行代码中执行数学运算并将结果重新赋值给变量。你不必像这样编写：

let num = 5;
num = num + 2;

console.log(num); // 7
You can write something like this:
你可以像这样编写：

let num = 5;
num += 2;

console.log(num); // 7
Notice how num += 2 combines both the addition and assignment steps into one. This saves time and reduces clutter in your code. Let's dive deeper into the most common compound assignment operators in JavaScript.
注意 num += 2 如何将加法和赋值步骤合并为一步。这节省了时间并减少了代码中的杂乱。让我们深入探讨 JavaScript 中最常见的复合赋值运算符。

As you've already seen, the += operator lets you add a value to an existing variable. It is known as the addition assignment operator. The addition assignment operator takes the current value of the variable, adds the specified number to it, and then assigns the result back to the variable:
如你所见， += 运算符允许你将一个值加到一个已存在的变量上。它被称为加法赋值运算符。加法赋值运算符获取变量的当前值，将其与指定的数相加，然后将结果重新赋值给该变量：

let total = 10;
total += 5;

console.log(total); // 15
As you might guess, there's a subtraction assignment operator denoted by -=. The subtraction assignment operator subtracts the specified value from the current value of the variable and assigns the new value back to the variable:
正如你所猜到的，有一个减法赋值运算符，用 -= 表示。减法赋值运算符从变量的当前值中减去指定的值，并将新值重新赋值给该变量：

let score = 20;
score -= 7;

console.log(score); // 13
If you didn't use the subtraction assignment, you'd have done something like this:
如果你没有使用减法赋值运算符，你可能需要这样做：

let score = 20;
score = score - 7;

console.log(score); // 13
The multiplication assignment operator is represented by *=. It multiplies the current value of the variable by the specified number and reassigns it back to the variable:
乘法赋值运算符用 *= 表示。它将变量的当前值乘以指定的数，然后将结果重新赋值给该变量：

let points = 5;
points *= 3;

console.log(points); // 15
Lastly, there's a division assignment operator denoted by /=. Just like others before it, it lets you divide the current value of a variable by a number you specify, then assign the result back to the variable:
最后，还有一个除法赋值运算符，用 /= 表示。和之前的运算符一样，它允许你将变量的当前值除以一个指定的数字，然后将结果重新赋值给该变量：

let balance = 100;
balance /= 4;

console.log(balance); // 25
Remember there's a compound assignment operator for every operator in JavaScript. So, apart from the four already mentioned, we also have:
记住，JavaScript 中每个运算符都有一个复合赋值运算符。所以，除了前面提到的四个之外，我们还有：

Remainder assignment operator (%=), which divides a variable by the specified number and assigns the remainder to the variable.
余数赋值运算符（ %= ），它将变量除以指定的数字，并将余数赋值给该变量。

Exponent assignment operator (**=), which raises a variable to the power of the specified number and reassigns the result to the variable.
指数赋值运算符（ **= ），它将变量提升到指定数字的幂，并将结果重新赋值给该变量。

Bitwise AND assignment operator (&=), which performs a bitwise AND operation with the specified number and reassigns the result to the variable.
按位与赋值运算符（ &= ），它将指定的数字进行按位与操作，并将结果重新赋值给变量。

Bitwise OR assignment operator (|=), which performs a bitwise OR operation with the specified number and reassigns the result to the variable.
按位或赋值运算符（ |= ），它将指定的数字进行按位或操作，并将结果重新赋值给变量。

