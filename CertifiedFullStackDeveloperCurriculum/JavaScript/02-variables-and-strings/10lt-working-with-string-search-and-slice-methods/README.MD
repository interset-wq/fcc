# Working with String Search and Slice Methods 切片和字符串的包含关系

In this lecture you will learn how to search for substrings using the includes() method and how to extract portions of strings using the slice() method.

## How Can You Test if a String Contains a Substring? 字符串是否包含

When working with strings in JavaScript, there are many cases where you might need to check whether a string contains a specific substring, which is a smaller part of that string.

在 JavaScript 中使用字符串时，在许多情况下，您可能需要检查字符串是否包含特定的子字符串，该子字符串是该字符串的较小部分。

For example, you might want to check if a user's input includes a specific word or character before performing some action. One way to achieve this is by using the includes() method.

例如，您可能希望在执行某些作之前检查用户的输入是否包含特定单词或字符。实现此目的的一种方法是使用 includes（） 方法。

The includes() method is used to check if a string contains a specific substring. If the substring is found within the string, the method returns true otherwise, it returns false.

includes（） 方法用于检查字符串是否包含特定的子字符串。如果在字符串中找到子字符串，则该方法返回 true，否则返回 false。

Here's the basic syntax:

以下是基本语法：

Example Code  示例代码

string.includes(searchValue);

For the syntax, the searchValue is the substring you want to look for within the string. And here's an example:

对于语法，searchValue 是您要在字符串中查找的子字符串。这里有一个例子：

Example Code  示例代码

let phrase = "JavaScript is awesome!";
let result = phrase.includes("awesome");

console.log(result);  // true

In this example, the word awesome is found within the string JavaScript is awesome!, so the includes() method returns true.

在此示例中，在字符串 JavaScript is awesome！ 中找到了 awesome 一词，因此 includes（） 方法返回 true。

It's important to note that the includes() method is case-sensitive. This means that the exact match of the characters is required, including their case.

重要的是要注意 includes（） 方法区分大小写。这意味着需要字符的完全匹配，包括它们的大小写。

For example:  例如：

Example Code  示例代码

let phrase = "JavaScript is awesome!";
let result = phrase.includes("Awesome");

console.log(result);  // Output: false

Since Awesome (with an uppercase A) does not match awesome (with a lowercase a), the result is false.

由于 Awesome（大写 A）与 awesome（小写 a）不匹配，因此结果为 false。

You can also use the includes() method to check for a substring starting at a specific index in the string by providing a second parameter:

您还可以使用 includes（） 方法通过提供第二个参数来检查从字符串中特定索引开始的子字符串：

Example Code  示例代码

let text = "Hello, JavaScript world!";
let result = text.includes("JavaScript", 7);

console.log(result);  // true

Here, the search for the substring JavaScript starts from the 7th position in the string, ensuring it skips any characters before this position.

在这里，对子字符串 JavaScript 的搜索从字符串中的第 7 个位置开始，确保它跳过该位置之前的任何字符。

The includes() method only returns a true or false result. It does not provide information on where the substring is located in the string or how many times it occurs. If you need that level of detail, other methods, such as the indexOf() method might be more suitable.

includes（） 方法仅返回 true 或 false 结果。它不提供有关子字符串在字符串中的位置或出现次数的信息。如果您需要这种详细程度，其他方法（例如 indexOf（） 方法）可能更合适。

## How Can You Extract a Substring from a String? 字符串切片

When working with strings in JavaScript, you often need to extract a portion or substring from a larger string.

在 JavaScript 中使用字符串时，您通常需要从较大的字符串中提取部分或子字符串。

For example, you may want to extract part of a word, a specific character sequence, or just a fragment of a sentence.
例如，您可能想要提取单词的一部分、特定字符序列或仅提取句子的片段。

JavaScript provides several methods for this task, one of the most commonly used being the slice() method.
JavaScript 为此任务提供了多种方法，其中最常用的方法之一是 slice（） 方法。

The slice() method allows you to extract a portion of a string and returns a new string, without modifying the original string. It takes two parameters: the starting index and the optional ending index.
slice（） 方法允许您提取字符串的一部分并返回一个新字符串，而无需修改原始字符串。它需要两个参数：起始索引和可选的结束索引。

Here's the basic syntax:
以下是基本语法：

Example Code  示例代码
string.slice(startIndex, endIndex);
startIndex is the position where the extraction starts. endIndex is where the extraction ends. If not provided, slice() extracts until the end of the string.
startIndex 是提取开始的位置。endIndex 是提取结束的地方。如果未提供，则 slice（） 提取直到字符串末尾。

Let's look at a simple example of extracting part of a string:
让我们看一个提取字符串部分的简单示例：

Example Code  示例代码
let message = "Hello, world!";
let greeting = message.slice(0, 5);

console.log(greeting);  // Output: Hello
In this example, slice(0, 5) extracts characters starting from index 0 up to but not including index 5. As a result, the word Hello is extracted.
在此示例中， slice（0， 5） 提取从索引 0 开始但不包括索引 5 的字符。结果，提取了单词 Hello。

If you omit the second parameter, slice() will extract everything from the start index to the end of the string:
如果省略第二个参数，slice（） 将提取从字符串开始索引到结尾的所有内容：

Example Code  示例代码
let message = "Hello, world!";
let world = message.slice(7);

console.log(world);  // Output: world!
Here, slice(7) extracts the string from index 7 to the end of the string, resulting in world!.
在这里，slice（7） 从索引 7 提取字符串到字符串末尾，从而产生 world！。

You can also use negative numbers as indexes. When you use a negative number, it counts backward from the end of the string:
您还可以使用负数作为索引。当您使用负数时，它从字符串末尾向后计数：

Example Code  示例代码
let message = "JavaScript is fun!";
let lastWord = message.slice(-4);

console.log(lastWord);  // Output: fun!
In this case, slice(-4) extracts the last four characters from the string, giving us fun!.
在这种情况下，slice（-4） 从字符串中提取最后四个字符，给我们带来乐趣！

Let's say you want to extract a section from the middle of a string. You can provide both the starting and ending indexes to precisely control which part of the string you want:
假设你想从字符串中间提取一个部分。您可以同时提供开始索引和结束索引，以精确控制您想要的字符串部分：

Example Code  示例代码
let message = "I love JavaScript!";
let language = message.slice(7, 17);

console.log(language);  // Output: JavaScript
Here, slice(7, 17) extracts the substring starting at index 7 and ending right before index 17, which is the word JavaScript.
在这里，slice（7， 17） 提取从索引 7 开始到索引 17 之前结束的子字符串，即单词 JavaScript。

The slice() method is a powerful tool for extracting parts of a string in JavaScript.
slice（） 方法是在 JavaScript 中提取字符串部分的强大工具。

You specify the start and end indexes, and the method returns a new string that contains the extracted portion.
指定开始索引和结束索引，该方法将返回包含提取部分的新字符串。

With options for positive, negative, and omitted indexes, you can adapt it to various situations without altering the original string.
通过正索引、负索引和省略索引选项，您可以在不更改原始字符串的情况下使其适应各种情况。

