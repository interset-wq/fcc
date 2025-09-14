# Build a Calculator, Not started
In this workshop, you will review your knowledge of functions by building a calculator.

Step 1  第一步
In this workshop, you will review how to work with functions by building a calculator app.
在这个工作坊中，你将通过构建一个计算器应用程序来复习如何使用函数。

In the previous lectures, you learned how to declare functions like this:
在前面的课程中，你学习了如何这样声明函数：

Example Code  示例代码
// regular function
function myFunction() {

}

// arrow function
const myArrowFunction = () => {

}
Start by creating a function called addTwoAndSeven.
首先创建一个名为 addTwoAndSeven 的函数。

You can choose to use the regular function syntax or the arrow function syntax.
你可以选择使用普通函数语法或箭头函数语法。

Step 2  第二步
One of concepts you learned in the previous lectures was how to return values from a function.
你在之前的讲座中学习的一个概念是如何从函数中返回值。

Here is a reminder of how to return a value from a function:
这里是如何从函数中返回值的提醒：

Example Code  示例代码
function myFunction() {
  return "Hello World";
}
Inside your addTwoAndSeven function, return the sum of 2 and 7.
在你的 addTwoAndSeven 函数内部，返回 2 和 7 的和。

Step 3  步骤 3
In the previous lectures, you learned how to call (invoke) a function. Calling a function means to execute the code inside the function.
在之前的课程中，你学习了如何调用（执行）一个函数。调用函数意味着执行函数内部的代码。

Here is a reminder of how to call a function:
以下是调用函数的方法：

Example Code  示例代码
function myFunction() {
  return "Hello World";
}

// function call
myFunction();
Add a console.log statement, and inside it, call the addTwoAndSeven function.
添加一个 console.log 语句，并在其中调用 addTwoAndSeven 函数。

You should now see the sum of 2 and 7 logged to the console.
现在你应该看到 2 和 7 的和被打印到控制台。

Step 4  步骤 4
Now, it is time to add another function.
现在，是时候添加另一个函数了。

Declare a function called addThreeAndFour that returns the sum of 3 and 4.
声明一个名为 addThreeAndFour 的函数，该函数返回 3 和 4 的和。

Then call the addThreeAndFour function inside a console.log to see the result.
然后在 console.log 内部调用 addThreeAndFour 函数以查看结果。

Step 5  步骤 5
Even though the functions work as expected, there is a lot of repetition in your code.
尽管函数按预期工作，但你的代码中有很多重复。

Since you are building a calculator, you don't want to have to create a function for every possible combination of numbers you want to add together.
既然你在构建计算器，就不想为所有可能的数字组合创建一个函数来相加。

It would be better to create a single reusable function that can add any two numbers together.
最好创建一个单一的、可重用的函数，它可以将任意两个数字相加。

Remove all of the code you have written so far.
删除你到目前为止编写的所有代码。

In the next step, you will review how to work with parameters and arguments in functions.
在下一步中，你将学习如何在函数中处理参数和实参。

Step 6  第六步
In the previous lectures, you learned how to work with function parameters.
在前面的课程中，你学习了如何使用函数参数。

A function parameter is a variable that is defined in the function's declaration and acts as a placeholder.
函数参数是在函数声明中定义的变量，用作占位符。

Here is an example of a function that has a parameter:
这是一个具有参数的函数示例：

Example Code  示例代码
// The parameter is `name`
function greetUser(name) {
  return `Hello, ${name}!`;
}
Declare a function called calculateSum that takes two parameters, num1 and num2.
声明一个名为 calculateSum 的函数，该函数接受两个参数， num1 和 num2 。

Step 7  步骤 7
Inside your calculateSum function, you will need to return the sum of the two parameters.
在你的 calculateSum 函数中，你需要返回两个参数的和。

Step 8  第 8 步
The advantage of functions is that they can be called with different arguments, allowing you to reuse the same code with various values.
函数的优点在于它们可以用不同的参数被调用，这使你能够用各种值重用相同的代码。

Here are some example function calls with different string arguments:
这里有一些使用不同字符串参数的函数调用示例：

Example Code  示例代码
// function definition
function greetUser(name) {
  console.log(`Hello ${name}!`);
}

// function calls
greetUser("John"); // "Hello John!"
greetUser("Jane"); // "Hello Jane!"
Add a console.log that calls the calculateSum function with the arguments 2 and 5.
添加一个 console.log 调用 calculateSum 函数，参数为 2 和 5 。

Step 9  步骤 9
To further test out your calculateSum function, you will need to call it with different arguments.
为了进一步测试你的 calculateSum 函数，你需要用不同的参数调用它。

Add another console.log that calls the calculateSum function with the arguments 10 and 10.
添加另一个 console.log ，它调用 calculateSum 函数，参数为 10 和 10 。

Below that console.log, add another console.log that calls the calculateSum function with the arguments 5 and 5.
在那个 console.log 下面，添加另一个 console.log ，它调用 calculateSum 函数，参数为 5 和 5 。

Step 10  第 10 步
Now that your calculator can add two numbers together, it is time to create a function that will subtract two numbers.
现在你的计算器已经可以加两个数了，是时候创建一个函数来减两个数了。

Declare a function called calculateDifference that takes two parameters, num1 and num2.
声明一个名为 calculateDifference 的函数，该函数接受两个参数， num1 和 num2 。

Inside the function, return the difference between the two parameters.
在函数内部，返回两个参数的差值。

Step 11  第 11 步
Now it is time to test your calculateDifference function.
现在该测试你的 calculateDifference 函数了。

Start by adding a console.log that calls the calculateDifference function with the arguments 22 and 5.
首先，添加一个 console.log 调用 calculateDifference 函数，参数为 22 和 5 。

Then, add a second console.log that calls the calculateDifference function with the arguments 12 and 1.
然后，添加第二个 console.log 调用 calculateDifference 函数，参数为 12 和 1 。

Finally, add a third console.log that calls the calculateDifference function with the arguments 17 and 9.
最后，添加第三个 console.log 调用 calculateDifference 函数，参数为 17 和 9 。

Step 12  第 12 步
Now it is time to add the multiplication functionality to your calculator.
现在，是时候给你的计算器添加乘法功能了。

Declare a function called calculateProduct that takes two parameters, num1 and num2.
声明一个名为 calculateProduct 的函数，该函数接受两个参数， num1 和 num2 。

Inside the function, return the product of the two parameters.
在函数内部，返回两个参数的乘积。

Then, add a console.log that calls the calculateProduct function with the arguments 13 and 5.
然后，添加一个 console.log 调用 calculateProduct 函数，参数为 13 和 5 。

Step 13  第 13 步
The next step is to add the division functionality to your calculator.
下一步是为你的计算器添加除法功能。

Declare a function called calculateQuotient that takes two parameters, num1 and num2.
声明一个名为 calculateQuotient 的函数，该函数接受两个参数， num1 和 num2 。

Inside the function, return the quotient of the two parameters.
在函数内部，返回两个参数的商。

Then, add a console.log that calls the calculateQuotient function with the arguments 7 and 11.
然后，添加一个 console.log 调用 calculateQuotient 函数，参数为 7 和 11 。

Step 14  第 14 步
Your calculateQuotient appears to be working correctly but there is one case that you have not tested yet.
你的 calculateQuotient 看起来工作正常，但有一个情况你还没有测试过。

Add a console.log that calls the calculateQuotient function with the arguments 3 and 0.
添加一个 console.log 调用 calculateQuotient 函数，参数为 3 和 0 。

Make sure to take a close look at the output of this call.
确保仔细查看这个调用的输出

Step 15  第 15 步
If you look in the console, you will see the Infinity value. Infinity is a special value in JavaScript that represents a number that is greater than any other number.
如果你查看控制台，你会看到 Infinity 值。 Infinity 是 JavaScript 中的一个特殊值，表示一个比任何其他数都大的数。

The division by zero is not a valid operation in mathematics.
除以零在数学上不是有效的运算。

To account for this edge case, you should update your calculateQuotient function to instead check if num2 is zero.
为了考虑这种边界情况，你应该更新你的 calculateQuotient 函数，改为检查 num2 是否为零。

If it is, the function should return the string "Error: Division by zero". Otherwise, it should return the result of dividing num1 by num2.
如果是，函数应该返回字符串 "Error: Division by zero" 。否则，它应该返回 num1 除以 num2 的结果。

Step 16  第 16 步
It would be nice to have your calculator calculate the square of a number. The square of a number is the number multiplied by itself.
很棒的是能让你的计算器计算一个数的平方。一个数的平方是它自己乘以自己。

To calculate the square of a number in JavaScript, you can use the Math.pow() method. The Math.pow() method takes two arguments: the base number and the exponent.
在 JavaScript 中计算一个数的平方，你可以使用 Math.pow()方法。该方法接受两个参数：基数和指数。

You can also use the exponentiation operator (**) to calculate the square of a number.
你也可以使用指数运算符（**）来计算一个数的平方。

Here is an example:
这里是一个例子：

Example Code  示例代码
// base number is 5 
// the exponent is 2
Math.pow(5, 2); // 25

// using the exponentiation operator
5 ** 2; // 25
Declare a function called calculateSquare that takes a num parameter and returns the square of num.
声明一个名为 calculateSquare 的函数，该函数接受一个 num 参数并返回 num 的平方。

Step 17  第 17 步
To test your calculateSquare function, you will need to call the function a couple of times.
要测试你的 calculateSquare 函数，你需要调用这个函数几次。

Add a console.log that calls the calculateSquare function with the argument of 2.
添加一个 console.log ，它用参数 2 调用 calculateSquare 函数。

Then, add another console.log that calls the calculateSquare function with the argument of 9.
然后，再添加另一个 console.log ，它用参数 9 调用 calculateSquare 函数。

Step 18  第 18 步
The last piece of functionality for your calculator will be the square root functionality.
你计算器的最后一项功能将是平方根功能。

A square is a number multiplied by itself. So, the square root would be the number that when multiplied by itself gives the original number.
一个平方是一个数乘以它本身。所以，平方根就是那个乘以自己能得到原数的数。

For example, the square root of 9 is 3 because 3 * 3 = 9.
例如， 9 的平方根是 3 因为 3 * 3 = 9 。

To get the square root of a number in JavaScript, you can use the Math.sqrt() method.
在 JavaScript 中获取一个数的平方根，你可以使用 Math.sqrt() 方法。

Here is an example:
这里是一个例子：

Example Code  示例代码
// result: 3
Math.sqrt(9);
Declare a function called calculateSquareRoot that takes a num parameter and returns the square root of num.
声明一个名为 calculateSquareRoot 的函数，该函数接受一个 num 参数，并返回 num 的平方根。

Step 19  第 19 步
In the final step of the workshop, you will need to test out your calculateSquareRoot function.
在研讨会的最后一步，你需要测试你的 calculateSquareRoot 函数。

Add a second console.log that calls the calculateSquareRoot function with the argument of 25.
添加一个第二个 console.log ，它调用 calculateSquareRoot 函数，参数为 25 。

Then, add a third console.log that calls the calculateSquareRoot function with the argument of 100.
然后，添加一个第三个 console.log ，它调用 calculateSquareRoot 函数，参数为 100 。

And with those changes, your calculator app is complete!
有了这些更改，你的计算器应用就完成了！
