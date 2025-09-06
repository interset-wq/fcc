## Build a Mathbot, Not started
In this workshop, you will review how to work with the different Math object methods by building a Mathbot.

Step 1  第一步
In this workshop, you will review working with the different Math object methods by building a Mathbot. This Mathbot will log some math operations and messages to the console in efforts to teach you about JavaScript's Math object.
在这个工作坊中，你将通过构建一个 Mathbot 来复习使用不同的 Math 对象方法。这个 Mathbot 将记录一些数学运算和消息到控制台，目的是教你关于 JavaScript 的 Math 对象。

For this first step, start by creating a variable called botName and assign it the string value of "MathBot".
对于第一步，首先创建一个名为 botName 的变量，并将其赋值为 "MathBot" 的字符串值。

Then, create another variable called greeting and assign it the sentence "Hi there! My name is [botName goes here] and I am here to teach you about the Math object!". In place of the [botName goes here] placeholder, use the botName variable.
然后，创建另一个名为 greeting 的变量，并将其赋值为句子 "Hi there! My name is [botName goes here] and I am here to teach you about the Math object!" 。在 [botName goes here] 占位符处，使用 botName 变量。

You are free to use template literals or string concatenation with the + operator to achieve this.
你可以自由使用模板字面量或字符串拼接（使用 + 运算符）来实现这一点。

Finally, log the greeting variable to the console.
最后，将 greeting 变量记录到控制台。

Step 2  第二步
The next part of the workshop will review how the Math.random() method works.
工作坊的下一部分将回顾 Math.random() 方法的工作原理。

Start by adding another console.log() that logs the string "The Math.random() method returns a pseudo random number between 0 and less than 1." to the console.
首先，添加另一个 console.log() ，它将字符串 "The Math.random() method returns a pseudo random number between 0 and less than 1." 记录到控制台。

Step 3  步骤 3
Now, it is time to generate a random number using the Math.random() method.
现在，是时候使用 Math.random() 方法生成一个随机数了。

Create a variable called randomNum and assign it the value of the result of calling the Math.random() method.
创建一个名为 randomNum 的变量，并将其赋值为调用 Math.random() 方法的结果。

Then, log the randomNum variable to the console.
然后，将 randomNum 变量记录到控制台。

Try adding a space in the code to re-run the bot and see different random numbers that are generated.
尝试在代码中添加一个空格来重新运行机器人，并查看生成的不同随机数。

Step 4  步骤 4
The next portion of the workshop is to review how to generate a random number between two values.
工作坊的下一部分是复习如何在两个值之间生成随机数。

Start by adding another console.log() that logs the message "Now, generate a random number between two values." to the console.
首先，添加另一个 console.log() 来将消息 "Now, generate a random number between two values." 输出到控制台。

Then, create a variable called min and assign it the value of 1 and create a variable called max and assign it the value of 100.
然后，创建一个名为 min 的变量并赋值为 1 ，创建一个名为 max 的变量并赋值为 100 。

In the next step, you will generate a random number between these two values.
在下一步中，你将在这两个值之间生成一个随机数。

Step 5  步骤 5
The formula to generate a random number between two values is the following:
生成两个值之间随机数的公式如下：

Example Code  示例代码
Math.random() * (maximum - minimum) + minimum;
This will produce a result that is a floating point number between two values.
这将产生一个在两个值之间的浮点数结果。

Create a variable called randomNum2 and assign it the result of generating a value between the min and max values.
创建一个名为 randomNum2 的变量，并将其赋值为在 min 和 max 值之间生成的结果。

Then, log the randomNum2 variable to see the result. Try refreshing the page to see different results.
然后，记录 randomNum2 变量以查看结果。尝试刷新页面以查看不同的结果。

Step 6  第六步
Up until this point, you have only been dealing with floating point numbers and the number 0.
到目前为止，你只处理过浮点数和数字 0 。

For the next part of the workshop, you will review how to work with the Math.floor() method.
在研讨会接下来的部分，你将复习如何使用 Math.floor() 方法。

Start by adding a console.log() that logs the message "The Math.floor() method rounds the value down to the nearest whole integer."
首先，添加一个 console.log() 来记录消息 "The Math.floor() method rounds the value down to the nearest whole integer."

Step 7  步骤 7
As you learned in the previous lectures, the Math.floor() method rounds the value down to the nearest whole integer.
如前几节课所述， Math.floor() 方法会将数值舍入到最近的整数。

Example Code  示例代码
const price = 10.99;
Math.floor(price); // 10
Create a variable called numRoundedDown and assign it the result of rounding the floating point number 6.7 down to the nearest whole integer.
创建一个名为 numRoundedDown 的变量，并将其赋值为将浮点数 6.7 舍入到最近的整数的结果。

Then, log the numRoundedDown variable to the console to see the result.
然后，将 numRoundedDown 变量输出到控制台以查看结果。

Step 8  第 8 步
Now, it is time to review how the Math.ceil() method works.
现在，是时候回顾 Math.ceil() 方法的工作原理了。

Start by logging the string "The Math.ceil() method rounds the value up to the nearest whole integer." to the console.
首先，将字符串 "The Math.ceil() method rounds the value up to the nearest whole integer." 记录到控制台。

Step 9  步骤 9
In the previous lectures, you learned how to work with the Math.ceil() method like this:
在之前的课程中，你学习了如何使用 Math.ceil() 方法，如下所示：

Example Code  示例代码
const price = 10.01;
Math.ceil(price); // 11
The Math.ceil() method rounds the value up to the nearest whole integer.
Math.ceil() 方法会将数值向上舍入到最近的整数。

Create a variable called numRoundedUp and assign it the result of rounding the floating point number 3.2 up to the nearest whole integer.
创建一个名为 numRoundedUp 的变量，并将其赋值为将浮点数 3.2 向上舍入到最近的整数的计算结果。

Then, log the numRoundedUp variable to the console to see the result.
然后，将 numRoundedUp 变量输出到控制台以查看结果。

Step 10  第 10 步
The next portion of the workshop will review how to round numbers to the nearest whole integer.
接下来的工作坊部分将回顾如何将数字四舍五入到最接近的整数。

Start by adding a console.log() that logs the message "The Math.round() method rounds the value to the nearest whole integer." to the console.
首先，添加一个 console.log() ，它将消息 "The Math.round() method rounds the value to the nearest whole integer." 记录到控制台。

Step 11  第 11 步
In the lectures, you learned that the Math.round() method rounds the value to the nearest whole integer.
在讲座中，你学到 Math.round() 方法会将数值四舍五入到最近的整数。

Here are some examples:
这里有一些例子：

Example Code  示例代码
Math.round(6.7); // 7
Math.round(3.2); // 3
This differs from the Math.floor() and Math.ceil() methods, which round down and up to the nearest whole integer, respectively.
这与 Math.floor() 和 Math.ceil() 方法不同，分别表示向下和向上四舍五入到最近的整数。

Create a new variable called numRounded and assign the result of rounding the number 2.7. Then, log the value of numRounded to the console.
创建一个名为 numRounded 的新变量，并将数值 2.7 四舍五入的结果赋给它。然后，将 numRounded 的值输出到控制台。

Below that, create another new variable called numRounded2 and assign the result of rounding the number 11.2. Then, log the value of numRounded2 to the console.
在下面，创建另一个新的变量 numRounded2 并将 11.2 的结果四舍五入后赋值给它。然后，将 numRounded2 的值记录到控制台。

Step 12  第 12 步
For the last portion of the workshop, you will review how to get the minimum and maximum values of a set of numbers.
在研讨会的最后部分，你将复习如何获取一组数字的最小值和最大值。

Start by adding a console.log() that logs the message "The Math.max() and Math.min() methods are used to get the maximum and minimum number from a range." to the console.
首先，向代码中添加一个 console.log() ，用于在控制台输出消息 "The Math.max() and Math.min() methods are used to get the maximum and minimum number from a range." 。

Step 13  第 13 步
In the previous lectures, you learned how to get the maximum and minimum values from a range of numbers like this:
在之前的课程中，你学习了如何从一个数字范围内获取最大值和最小值，例如：

Example Code  示例代码
Math.max(1, 2, 3, 4, 5); // 5
Math.min(1, 2, 3, 4, 5); // 1
Create a variable called maxNum and assign it the result of finding the maximum number between the numbers 3, 125, 55, 24. Then, log the value of maxNum to the console.
创建一个名为 maxNum 的变量，并将其赋值为在数字 3, 125, 55, 24 之间找到的最大数。然后，将 maxNum 的值记录到控制台。

Below that, create a variable called minNum and assign it the result of finding the minimum number between the numbers 6, 90, 14, 90, 2. Then, log the value of minNum to the console.
在其下方，创建一个名为 minNum 的变量，并将其赋值为在数字 6, 90, 14, 90, 2 之间找到的最小数。然后，将 minNum 的值记录到控制台。

Step 14  第 14 步
For the last step of the workshop, you will log the message "It was fun learning about the different Math methods with you!" to the console.
在研讨会最后一步，你将消息 "It was fun learning about the different Math methods with you!" 记录到控制台。

And with that last change, you have completed the MathBot workshop!
就这样，你完成了 MathBot 研讨会！