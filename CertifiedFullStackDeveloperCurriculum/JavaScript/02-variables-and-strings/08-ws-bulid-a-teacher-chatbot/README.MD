# Build a Teacher Chatbot, Not started
In this workshop, you will continue to learn more about JavaScript strings by building a chatbot.

You will learn how to work with template literals, and the indexOf method.

Step 1  步骤1
In this workshop, you are going to continue learning about strings by building a Teacher Chatbot.
在本次研讨会中，您将通过构建教师聊天机器人来继续学习字符串。

To begin, add a console statement, with the message of "Hi there!".
首先，添加控制台语句，并附上 “嗨！

Step 2  第2步
Now it is time to set the bot's name.
现在是时候设置机器人的名称了。

Create a variable called botName and assign it the string value of "teacherBot".
创建一个名为 botName 的变量，并为其分配字符串值 “teacherBot”。

Step 3  第 3 步
Now it is time to create a greeting using the botName variable.
现在是时候使用 botName 变量创建问候语了。

In the previous lectures, you learned how to concatenate strings using template literals like this:
在前面的讲座中，您学习了如何使用模板文字连接字符串，如下所示：

Example Code  示例代码
const name = "John";

// "Hello, John!"
`Hello, ${name}!`;
Start by creating a variable called greeting.
首先创建一个名为 greeting 的变量。

Next, using template literal syntax, assign a string that says My name is, followed by the botName variable, and ending with a period (.).
接下来，使用模板文字语法，分配一个字符串，其中显示 My name is，后跟 botName 变量，并以句点 （.） 结尾。

Finally, log the greeting variable to the console.
最后，将 greeting 变量记录到控制台。

Step 4  第四步
The next step is to create a few more variables that will be used in future bot messages.
下一步是创建更多变量，这些变量将在将来的机器人消息中使用。

Create a variable called subject and assign it the string value "JavaScript".
创建一个名为 subject 的变量，并为其分配字符串值 “JavaScript”。

Then create a variable called topic and assign it the string value "strings".
然后创建一个名为 topic 的变量并为其分配字符串值 “strings”。

Step 5  第 5 步
Now, it's time to use the variables you created in the previous step.
现在，是时候使用您在上一步中创建的变量了。

In the lectures, you learned how to work with template literals like this:
在讲座中，您学习了如何使用模板文字，如下所示：

Example Code  示例代码
const name = "John";
const age = 30;

// My name is John and I am 30 years old.
`My name is ${name} and I am ${age} years old.`;
Start by creating a sentence variable.
首先创建一个句子变量。

Using template literal syntax, assign the string Today, you will learn about [topic variable goes here] in [subject variable goes here]. to the sentence variable.
使用模板文字语法，将字符串赋值 Today, you will learn about [topic variable goes here] in [subject variable goes here]. 给句子变量。

You will replace the [topic variable goes here] and [subject variable goes here] placeholders with the topic and subject variables and ${} syntax.
您将用主题变量和主题变量以及 ${} 语法替换 [主题变量转到此处] 和 [主题变量转到此处] 占位符。

Finally, log the sentence variable to the console.
最后，将句子变量记录到控制台。

Step 6  第 6 步
For this next portion of the project, the bot will teach working with the string length property.
对于项目的下一部分，机器人将教授如何使用字符串长度属性。

Start by creating a new variable called strLengthIntro.
首先创建一个名为 strLengthIntro 的新变量。

Then using template literal syntax, assign the string Here is an example of using the length property on the word [subject]. to the strLengthIntro variable.
然后使用模板文字语法，将字符串 Here is an example of using the length property on the word [subject]. 分配给 strLengthIntro 变量。

Replace [subject] with the subject variable like you did earlier.
像之前一样将 [subject] 替换为 subject 变量。

Finally, log the strLengthIntro variable to the console.
最后，将 strLengthIntro 变量记录到控制台。

Step 7  第 7 步
To get the length of a string, you can use the length property. This property returns the number of characters in a string.
要获取字符串的长度，您可以使用 length 属性。此属性返回字符串中的字符数。

Here is an example:
这是一个例子：

Example Code  示例代码
const greeting = "Hello, world!";

// Output: 13
console.log(greeting.length);
Start by using the length property to get the length of the subject string and log that value to the console.
首先使用 length 属性获取主题字符串的长度，并将该值记录到控制台。

Step 8  第 8 步
Now it is time to get the length of the topic string.
现在是时候获取主题字符串的长度了。

You can use template literals inside console statements like this:
您可以在控制台语句中使用模板文字，如下所示：

Example Code  示例代码
const developer = "Jessica";
console.log(`Hello, my name is ${developer}.`);
Start by outputting the message Here is an example of using the length property on the word [topic]. to the console.
首先将消息 Here is an example of using the length property on the word [topic]. 输出到控制台。

Remember to replace [topic] with the topic variable, and use proper template literal syntax as you did in the previous steps.
请记住将 [topic] 替换为 topic 变量，并像前面的步骤一样使用正确的模板文字语法。

Then, add a second console.log statement that outputs the length of the topic string to the console.
然后，添加第二个 console.log 语句，将主题字符串的长度输出到控制台。

Step 9  第 9 步
The next part of this workshop is to review accessing characters from a string.
本研讨会的下一部分是回顾如何从字符串中访问字符。

Start by outputting the message Here is an example of accessing the first letter in the word [subject]. to the console.
首先将消息 Here is an example of accessing the first letter in the word [subject]. 输出到控制台。

Remember to replace [subject] with the subject variable and use proper template literal syntax like you did in the previous steps.
请记住将 [subject] 替换为 subject 变量，并像在前面的步骤中一样使用正确的模板文字语法。

Step 10  第 10 步
In the previous lectures, you learned how to access characters in a string like this:
在前面的讲座中，您学习了如何访问字符串中的字符，如下所示：

Example Code  示例代码
const firstName = "Jessica";
// returns "J"
firstName[0];
Remember that index numbers start at 0, so the first letter in a string will always be at index 0.
请记住，索引号从 0 开始，因此字符串中的第一个字母将始终位于索引 0。

Start by adding another console statement.
首先添加另一个控制台语句。

Inside the console statement, output the first letter of the subject variable using bracket notation and the correct index number.
在控制台语句中，使用括号表示法和正确的索引号输出主题变量的第一个字母。

Step 11  第 11 步
Now it is time to access the second letter of the subject variable.
现在是时候访问主题变量的第二个字母了。

Start by adding a console statement that outputs the message Here is an example of accessing the second letter in the word [subject]. Remember to replace [subject] with the actual value of the subject variable and use correct template literal syntax.
首先添加一个控制台语句，该语句输出消息 Here is an example of accessing the second letter in the word [subject]. 记住将 [subject] 替换为 subject 变量的实际值，并使用正确的模板文字语法。

Then add another console statement that outputs the second letter of the subject variable using bracket notation and the correct index number.
然后添加另一个控制台语句，该语句使用括号表示法和正确的索引号输出主题变量的第二个字母。

Step 12  第 12 步
Now it is time to access the last character of a string.
现在是时候访问字符串的最后一个字符了。

Start by adding another console statement that outputs the message Here is an example of accessing the last letter in the word [subject].
首先添加另一个输出消息 Here is an example of accessing the last letter in the word [subject]. 的控制台语句

Remember to replace [subject] with the actual value of the subject variable and use correct template literal syntax.
请记住将 [subject] 替换为 subject 变量的实际值，并使用正确的模板文字语法。

Step 13  第 13 步
In the lectures, you learned how to access the last character in a string like this:
在讲座中，您学习了如何访问字符串中的最后一个字符，如下所示：

Example Code  示例代码
const firstName = "Jessica";

// returns "a"
firstName[firstName.length - 1];
string.length - 1 will always give you the last index number for a string.
string.length - 1 将始终为您提供字符串的最后一个索引号。

Create a new variable called lastCharacter and assign it the value of the last character in the subject variable.
创建一个名为 lastCharacter 的新变量，并为其赋值主题变量中最后一个字符的值。

Then, log the value of the lastCharacter variable to the console.
然后，将 lastCharacter 变量的值记录到控制台。

Step 14  第 14 步
For the last part of the workshop, you will review how to find the index position of substring in a string. Remember that a substring is a part of a string.
在研讨会的最后一部分，您将回顾如何在字符串中找到子字符串的索引位置。请记住，子字符串是字符串的一部分。

Start by creating a variable called learningIsFunSentence and assign it the string value of "Learning is fun.".
首先创建一个名为 learningIsFunSentence 的变量，并为其分配字符串值 “Learning is fun.”。

Step 15  第 15 步
The next step is to add another console statement that outputs the string "Here are examples of finding the positions of substrings in the sentence.".
下一步是添加另一个输出字符串的控制台语句 "Here are examples of finding the positions of substrings in the sentence." 。

Step 16  第 16 步
In the previous lectures, you learned how to work with the indexOf method like this:
在前面的讲座中，您学习了如何使用 indexOf 方法，如下所示：

Example Code  示例代码
const sentence = "I love to learn.";

// returns index 2
console.log(sentence.indexOf("love"));

// returns -1
console.log(sentence.indexOf("hate"));
Remember that the indexOf method returns the index position of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
请记住，indexOf 方法返回字符串中第一次出现子字符串的索引位置。如果未找到子字符串，则返回 -1。

Add a new console statement that outputs the result of using the indexOf method on the learningIsFunSentence variable to find the index position of the substring "Learning".
添加一个新的控制台语句，输出在 learningIsFunSentence 变量上使用 indexOf 方法查找子字符串 “Learning” 的索引位置的结果。

Step 17  第 17 步
Next, you will add a new console statement that outputs the result of using the indexOf method on the learningIsFunSentence variable to find the position of the substring "fun".
接下来，您将添加一个新的控制台语句，该语句输出在 learningIsFunSentence 变量上使用 indexOf 方法查找子字符串 “fun” 的位置的结果。

Below that console statement, add a new console statement that outputs the result of using the indexOf method to find the position of the substring "learning".
在该控制台语句下方，添加一个新的控制台语句，该语句输出使用 indexOf 方法查找子字符串 “learning” 位置的结果。

Take note of what the last console statement outputs.
记下最后一个控制台语句输出的内容。

Step 18  第 18 步
The last console statement outputs -1 because the substring "learning" is not found in the "Learning is fun. sentence.
最后一个控制台语句输出 -1，因为在 “Learning is fun. 句。

The indexOf method is case-sensitive. So the substring "learning" is not the same as the substring "Learning".
indexOf 方法区分大小写。因此，子字符串 “learning” 与子字符串 “Learning” 不同。

Now that you understand how some common string methods work, you can complete the workshop by logging one last message to the console.
现在，您已经了解了一些常见字符串方法的工作原理，您可以通过将最后一条消息记录到控制台来完成研讨会。

Add a console statement that outputs the message "I hope you enjoyed learning today." to the console.
添加一个控制台语句，将消息 "I hope you enjoyed learning today." 输出到控制台 。

And with that final message, you have completed the workshop!
有了最后一条信息，您就完成了研讨会！

