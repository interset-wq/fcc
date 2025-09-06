# Build a Greeting Bot, Not started
In this workshop, you will learn JavaScript fundamentals by building a greeting bot.

You will learn about variables, let, const, console.log and basic string usage.

Step 1  步骤1
In this workshop you will learn how to work with JavaScript fundamentals by building a greeting bot.
在本研讨会中，您将学习如何通过构建问候机器人来使用 JavaScript 基础知识。

In this first step, you will want to output a message to the console from the greeting bot.
在第一步中，您需要从问候机器人向控制台输出消息。

Remember that you learned about console.log() and strings in the previous lectures.
请记住，您在之前的讲座中了解了 console.log（） 和字符串。

Here is a reminder of how to use console.log() with strings:
以下是如何将 console.log（） 与字符串一起使用的提醒：

Example Code  示例代码
console.log("Hello, World!");
Add a console.log() statement that outputs the string "Hi there!" to the console. Don't forget your quotes around the message!
向控制台添加一个 console.log（） 语句，该语句将字符串 “Hi there！” 输出。不要忘记您在消息周围的引号！

Step 2  第2步
Now you should see the first message from the bot in the console.
现在，您应该会在控制台中看到来自机器人的第一条消息。

It is time to add a second message from the bot.
是时候添加来自机器人的第二条消息了。

Add another console.log statement to output the message "I am excited to talk to you." to the console.
添加另一个 console.log 语句，将消息 "I am excited to talk to you." 输出到控制台。

Step 3  第 3 步
In the previous lectures, you learned about the let keyword and how to declare variables in JavaScript.
在前面的讲座中，您了解了 let 关键字以及如何在 JavaScript 中声明变量。

Here is a reminder of how to declare a variable using the let keyword:
以下是如何使用 let 关键字声明变量的提醒：

Example Code  示例代码
let greeting;
Use the let keyword to declare a variable called bot.
使用 let 关键字声明一个名为 bot 的变量。

NOTE: You are using let here because later on in the workshop, you will be changing the value of the bot variable.
注意 ：您在这里使用 let 是因为在研讨会的后面，您将更改机器人变量的值。

Step 4  第四步
When you need to declare variables with multiple words, you can use the camelCase naming convention.
当需要声明包含多个单词的变量时，可以使用驼峰命名法。

When using camelCase, the first word is all lowercase and the first letter of each subsequent word is capitalized.
使用驼峰命名法时，第一个单词全部小写，后续每个单词的第一个字母大写。

Here is an example:
这是一个例子：

Example Code  示例代码
let thisIsCamelCase;
Use let to declare a variable named botLocation.
使用 let 声明名为 botLocation 的变量。

Step 5  第 5 步
Now, it is time to assign some values to your bot and botLocation variables.
现在，是时候为机器人和 botLocation 变量分配一些值了。

In the previous lectures, you learned how to assign values to variables like this:
在前面的讲座中，您学习了如何为变量赋值，如下所示：

Example Code  示例代码
variableName = "Here is the value";
Remember that what is on the right side of the assignment operator = is the value that you are assigning to the variable on the left side.
请记住，赋值运算符 = 右侧的值是您分配给左侧变量的值。

Assign the string "teacherBot" to the bot variable and the string "the universe" to the botLocation variable.
将字符串 “teacherBot” 分配给机器人变量，将字符串 “the universe” 分配给 botLocation 变量。


Step 6  第 6 步
Now, it is time to add another message from the bot.
现在，是时候添加来自机器人的另一条消息了。

Add another console statement to the code that logs the message "Allow me to introduce myself.".
将另一个控制台语句添加到记录消息 "Allow me to introduce myself." 的代码中。

Step 7  第 7 步
Earlier, you created the bot and botLocation variables. Now, you will use them to output new messages to the console.
之前，您创建了机器人和 botLocation 变量。现在，您将使用它们将新消息输出到控制台。

In the lectures, you learned how to work with string concatenation using the + operator to concatenate strings together like this:
在讲座中，您学习了如何使用 + 运算符将字符串串联在一起，如下所示：

Example Code  示例代码
let firstName = "John";

console.log("Hello, my name is " + firstName + ".");
// result: "Hello, my name is John."
Remember that you need to be mindful of spaces when concatenating strings with variables.
请记住，在将字符串与变量连接起来时，您需要注意空格。

Create a variable called botIntroduction.
创建一个名为 botIntroduction 的变量。

Then use string concatenation with the + operator to join the string "My name is " followed by the bot variable followed by a period (.).
然后使用字符串串联和 + 运算符来连接字符串 “我的名字是”， 后跟机器人变量，后跟句点 （.）。

Assign this value to the botIntroduction variable.
将此值分配给 botIntroduction 变量。

Then, log the botIntroduction variable to the console.
然后，将 botIntroduction 变量记录到控制台。

Step 8  第 8 步
The next message from the bot will concern the bot's location.
来自机器人的下一条消息将涉及机器人的位置。

Create a variable called botLocationSentence.
创建一个名为 botLocationSentence 的变量。

Then use string concatenation with the + operator to join the string "I live in " with the botLocation variable followed by a period (.).
然后使用字符串串联和 + 运算符，将字符串 “我住在” 与 botLocation 变量后跟句点 （.） 连接起来。

Assign this value to the botLocationSentence variable.
将此值分配给 botLocationSentence 变量。

Then, log the value of botLocationSentence to the console.
然后，将 botLocationSentence 的值记录到控制台。

Step 9  第 9 步
In the previous lectures, you learned how to reassign values to variables like this:
在前面的讲座中，您学习了如何将值重新分配给变量，如下所示：

Example Code  示例代码
let name = "John";
console.log(name); // "John"

name = "Jane";
console.log(name); // "Jane"
Using reassignment, assign the string "professorBot" to the bot variable.
使用重新分配，将字符串 “professorBot” 分配给机器人变量。

Step 10  第 10 步
Now it is time to see the new bot value.
现在是时候看看新的机器人价值了。

Start by creating a new variable called nicknameIntroduction.
首先创建一个名为 nicknameIntroduction 的新变量。

Use string concatenation to join the string "My nickname is " with the bot variable followed by a period (.).
使用字符串串联将字符串 “我的昵称是” 与机器人变量后跟句点 （.） 连接起来。

Assign the resulting string to the nicknameIntroduction variable.
将结果字符串分配给 nicknameIntroduction 变量。

Then, log the value of nicknameIntroduction to the console.
然后，将 nicknameIntroduction 的值记录到控制台。

Step 11  第 11 步
Now it looks like the bot wants to change their nickname.
现在看起来机器人想要更改他们的昵称。

Using reassignment, assign the string "awesomeTeacherBot" to the bot variable.
使用重新赋值，将字符串 “awesomeTeacherBot” 分配给机器人变量。

Step 12  第 12 步
To see the bot's new nickname, you will need to log a new message to the console.
若要查看机器人的新昵称，需要将新消息记录到控制台。

Create a new variable called newNicknameGreeting.
创建一个名为 newNicknameGreeting 的新变量。

Then use string concatenation to join the string "I love my nickname but I wish people would call me " with the bot variable followed by a period.
然后使用字符串串联将字符串 "I love my nickname but I wish people would call me " 与机器人变量后跟句点连接起来。

Assign the result to the newNicknameGreeting variable.
将结果分配给 newNicknameGreeting 变量。

Then, log the value of newNicknameGreeting to the console.
然后，将 newNicknameGreeting 的值记录到控制台。

Step 13  第 13 步
The last few messages from the bot will focus on the bot's favorite subject.
来自机器人的最后几条消息将重点关注机器人最喜欢的主题。

Start by creating a new variable called favoriteSubject and assign it the string "Computer Science".
首先创建一个名为 favoriteSubject 的新变量，并为其分配字符串 “Computer Science”。

Step 14  第 14 步
Next, create a variable called favoriteSubjectSentence.
接下来，创建一个名为 favoriteSubjectSentence 的变量。

Use string concatenation to join the string "My favorite subject is " with the favoriteSubject variable followed by a period.
使用字符串串联将字符串 “我最喜欢的主题是” 与 favoriteSubject 变量后跟句点连接起来。

Assign the result to the favoriteSubjectSentence variable.
将结果分配给 favoriteSubjectSentence 变量。

Then, log the value of favoriteSubjectSentence to the console.
然后，将 favoriteSubjectSentence 的值记录到控制台 。

Step 15  第 15 步
For the final step, you will log the bot's message of "Well, it was nice to talk to you. Have a nice day!" to the console.
对于最后一步，你将机器人的消息记录 "Well, it was nice to talk to you. Have a nice day!" 到控制台。

And with that, your greeting bot is complete!
这样，您的问候机器人就完成了！

