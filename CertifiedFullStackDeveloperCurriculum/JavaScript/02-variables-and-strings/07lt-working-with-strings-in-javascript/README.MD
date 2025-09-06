# Working with Strings in JavaScript, Not started
In these lectures, you will learn how to work with strings in JavaScript. You will learn how to access characters from a string, how to use template literals and interpolation, how to create a new line in strings, and much more.

## What Is Bracket Notation, and How Do You Access Characters from a String?
什么是括号表示法，如何从字符串中访问字符？
In JavaScript, strings are treated as sequences of characters, and each character in a string can be accessed using bracket notation. This allows you to retrieve a specific character from a string based on its position, which is called its index.
在 JavaScript 中，字符串被视为字符序列，并且可以使用括号表示法访问字符串中的每个字符。这允许您根据字符串的位置从字符串中检索特定字符，这称为其索引。

An index is the position of a character within a string, and it is zero-based. This means that the first character of a string has an index of 0, the second character has an index of 1, and so on.
索引是字符串中字符的位置，它从零开始。这意味着字符串的第一个字符的索引为 0，第二个字符的索引为 1，依此类推。

For example, in the string hello, the character h is at index 0, e is at index 1, l is at index 2, and so on.
例如，在字符串 hello 中，字符 h 位于索引 0，e 位于索引 1，l 位于索引 2，依此类推。

Bracket notation uses square brackets ([]) and the index of the character you want to access. Let’s look at an example:
括号表示法使用方括号 （[]） 和要访问的字符的索引。让我们看一个例子：

let greeting = "hello";
console.log(greeting[1]); // Output: "e"
In this example, we can access the character at index 1, which is e.
在这个例子中，我们可以访问索引 1 处的字符，即 e。

To get the last character of a string, you can use the length of the string minus one. The length property of a string tells you how many characters it contains, so to access the last character, you would subtract one from the length:
要获取字符串的最后一个字符，您可以使用字符串的长度减去 1。字符串的 length 属性告诉您它包含多少个字符，因此要访问最后一个字符，您需要从长度中减去一个：

let greeting = "hello";
console.log(greeting[greeting.length - 1]); // Output: "o"
In this case, the length of hello is 5, and the last character (o) is at index 4 which is 5 - 1.
在这种情况下，hello 的长度为 5，最后一个字符 （o） 位于索引 4，即 5 - 1。

If you want to get multiple characters, you can use bracket notation like this:
如果你想得到多个字符，你可以使用像这样的括号表示法：

let greeting = "hello";
let firstTwo = greeting[0] + greeting[1]; // Output: "he"
console.log(firstTwo);
In this example, we are concatenating the first and second characters using bracket notation to form the string he.
在此示例中，我们使用括号表示法连接第一个和第二个字符以形成字符串 he。

Bracket notation is useful when you need to access specific characters in a string, such as extracting initials from a name or checking a specific letter for validation.
当您需要访问字符串中的特定字符时，例如从名称中提取首字母或检查特定字母进行验证，括号表示法非常有用。

## How Do You Create a Newline in Strings and Escape Strings?
如何在字符串和转义字符串中创建换行符？
When working with strings in JavaScript, there are times when you need to include special characters that the JavaScript engine might otherwise misinterpret.
在 JavaScript 中使用字符串时，有时您需要包含 JavaScript 引擎可能会误解的特殊字符。

Two common tasks involve creating a newline within a string and escaping certain characters (like quotes) to make sure they appear correctly.
两个常见任务涉及在字符串中创建换行符并转义某些字符（如引号）以确保它们正确显示。

In many programming languages, including JavaScript, you can create a newline in a string using a special character called an escape sequence. The most common escape sequence for newlines is \n.
在许多编程语言（包括 JavaScript）中，您可以使用称为转义序列的特殊字符在字符串中创建换行符。换行符最常见的转义序列是 \n。

For example, if you want to break a string into multiple lines, you would use \n where you want the new line to begin:
例如，如果你想将一个字符串分成多行，你可以在你希望新行开始的地方使用 \n：

let poem = "Roses are red,\nViolets are blue,\nJavaScript is fun,\nAnd so are you.";
console.log(poem);
The output will be:
输出将是：

Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.
The \n escape sequence tells JavaScript to insert a line break at that point, which results in the string being displayed across multiple lines.
\n 转义序列告诉 JavaScript 在该点插入换行符，这会导致字符串跨多行显示。

Another important concept when working with strings is escaping characters. Sometimes, you need to include characters in your string that JavaScript normally uses for something else, such as quotes.
使用字符串时的另一个重要概念是转义字符。有时，您需要在字符串中包含 JavaScript 通常用于其他内容的字符，例如引号。

If you simply use quotes inside a string without escaping them, it can cause an error because JavaScript will think you're trying to end the string.
如果您只是在字符串内使用引号而不转义它们，则可能会导致错误，因为 JavaScript 会认为您正在尝试结束字符串。

For example, this will cause an error:
例如，这将导致错误：

let statement = "She said, "Hello!"";
JavaScript gets confused because it thinks the string ends after the word "said," but, you want the quotes around "Hello!" to be part of the string.
JavaScript 会感到困惑，因为它认为字符串在单词“said” 之后结尾，但是，您希望 “Hello！” 周围的引号成为字符串的一部分。

To fix this, you can escape the inner quotes by placing a backslash (\) before them:
要解决此问题，您可以通过在内引号前放置反斜杠 （\） 来转义内引号：

let statement = "She said, \"Hello!\"";
console.log(statement); // Output: She said, "Hello!"
The backslash tells JavaScript to treat the quotes as literal characters, so they appear correctly in the output.
反斜杠告诉 JavaScript 将引号视为文字字符，以便它们正确显示在输出中。

You can also escape other special characters, such as the backslash itself (\\), or single quotes within a string surrounded by single quotes (\').
您还可以转义其他特殊字符，例如反斜杠本身 （\\），或用单引号 （\'） 括起来的字符串中的单引号。

Here's another example using single quotes:
这是另一个使用单引号的示例：

let quote = 'It\'s a beautiful day!';
console.log(quote); // Output: It's a beautiful day!
By escaping the single quote with \', JavaScript knows to include it as part of the string rather than ending the string early.
通过用 \' 转义单引号，JavaScript 知道将其作为字符串的一部分包含在内，而不是提前结束字符串。

Escaping and creating newlines are essential when you’re formatting output or handling special characters in strings. These techniques help you prevent errors and ensure your text appears exactly as intended.
当您格式化输出或处理字符串中的特殊字符时，转义和创建换行符至关重要。这些技术可帮助您防止错误并确保您的文本完全按预期显示。

## What Are Template Literals, and What Is String Interpolation?
什么是模板文字，什么是字符串插值？
In JavaScript, template literals are a powerful and flexible way to work with strings. Unlike regular strings, which use single (') or double (") quotes, template literals are defined with backticks (`).
在 JavaScript 中，模板文字是一种强大而灵活的字符串处理方式。与使用单引号 （'） 或双引号 （“） 的常规字符串不同，模板文字是用反引号 （'） 定义的。

They allow for easier string manipulation, including embedding variables directly inside a string, a feature known as string interpolation.
它们允许更轻松地进行字符串作，包括直接在字符串中嵌入变量，这一功能称为字符串插值。

Template literals make it easier to create strings that span multiple lines or include expressions (like variables or even JavaScript code) directly within the string.
模板文字可以更轻松地创建跨多行的字符串或直接在字符串中包含表达式（如变量甚至 JavaScript 代码）。

Here's a basic example of a template literal:
下面是模板文字的基本示例：

let name = "Alice";
let greeting = `Hello, ${name}!`; // Output: "Hello, Alice!"
Notice the use of backticks instead of single or double quotes. The ${name} syntax is an example of string interpolation, where the value of the variable name is directly inserted into the string.
请注意使用反引号而不是单引号或双引号。${name} 语法是字符串插值的一个示例，其中变量名称的值直接插入到字符串中。

String interpolation allows you to embed variables and expressions inside a string. This is a significant improvement over the older method, where you would concatenate strings and variables using the + operator.
字符串插值允许您在字符串中嵌入变量和表达式。与旧方法相比，这是一个重大改进，在旧方法中，您可以使用 + 运算符连接字符串和变量。

Here is an example using string concatenation and the plus (+) operator:
下面是使用字符串串联和加号 （+） 运算符的示例：

let name = "Alice";
let age = 25;
let message = "My name is " + name + " and I am " + age + " years old.";
console.log(message); // Output: "My name is Alice and I am 25 years old."
And here is an example using template literals and string interpolation:
这是一个使用模板文字和字符串插值的示例：

let message = `My name is ${name} and I am ${age} years old.`;
console.log(message); // Output: "My name is Alice and I am 25 years old."
As you can see, string interpolation with template literals is much cleaner and easier to read, especially when you're working with multiple variables.
如您所见，使用模板文字的字符串插值更干净、更易于阅读，尤其是在处理多个变量时。

Another great feature of template literals is that they support multiline strings. With regular strings, you would need to use escape characters (\n) to create new lines. With template literals, you can simply write the string across multiple lines, and the formatting is preserved:
模板文字的另一个重要功能是它们支持多行字符串。对于常规字符串，您需要使用转义字符 （\n） 来创建新行。使用模板文字，您可以简单地跨多行编写字符串，并保留格式：

let poem = `Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.`;

console.log(poem);
The output will retain the line breaks as written:
输出将保留所写的换行符：

Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.
Template literals are particularly useful when you need to include variables or expressions in strings, format complex strings, or work with multiline text. They are more concise and readable compared to traditional string concatenation.
当需要在字符串中包含变量或表达式、设置复杂字符串格式或处理多行文本时，模板文字特别有用。与传统的字符串串联相比，它们更加简洁和可读。

## How Can You Find the Position of a Substring in a String?
如何找到子字符串在字符串中的位置？
When working with strings in JavaScript, there may be times when you need to locate the position of a specific substring within a larger string.
在 JavaScript 中处理字符串时，有时您可能需要在较大的字符串中找到特定子字符串的位置。

A substring is a sequence of characters that appears within a larger string. For example, in the string hello world, hello and world are substrings.
子字符串是出现在较大字符串中的字符序列。例如，在字符串 hello world 中，hello 和 world 是子字符串。

To locate the position of a substring inside of a string, you can use the indexOf() method. The indexOf() method in JavaScript allows you to search for a substring within a string.
要在字符串中定位子字符串的位置，可以使用 indexOf（） 方法。JavaScript 中的 indexOf（） 方法允许您在字符串中搜索子字符串。

If the substring is found, indexOf() returns the index (or position) of the first occurrence of that substring. If the substring is not found, indexOf() returns -1, which indicates that the search was unsuccessful.
如果找到子字符串，indexOf（） 将返回该子字符串第一次出现的索引（或位置）。如果未找到子字符串，则 indexOf（） 返回 -1，这表示搜索不成功。

The indexOf() method takes two arguments: the first is the substring you want to find within the larger string, and the second is an option starting position for the search. If you don’t provide a starting position, the search will begin at the start of the string.
indexOf（） 方法接受两个参数：第一个是要在较大字符串中查找的子字符串，第二个是搜索的选项起始位置。如果未提供起始位置，则搜索将从字符串的开头开始。

In this context, an argument is a value you give to a function or method when you call it, enabling that function or method to perform its task using the specific information you provide. You will learn more about arguments in future lectures.
在这种情况下， 参数是您在调用函数或方法时赋予它的值，使该函数或方法能够使用您提供的特定信息执行其任务。您将在以后的讲座中了解更多关于论点的信息。

Here is an example of using the indexOf() method to find the position for the string awesome:
以下是使用 indexOf（） 方法查找字符串 awesome 位置的示例：

let sentence = "JavaScript is awesome!";
let position = sentence.indexOf("awesome!");
console.log(position); // 14
In this example, the word awesome starts at index 14 in the string JavaScript is awesome!, so the indexOf() method returns 14.
在此示例中，单词 awesome 从字符串 JavaScript is awesome！ 中的索引 14 开始，因此 indexOf（） 方法返回 14。

Now, let's see what happens when the substring isn't found:
现在，让我们看看当找不到子字符串时会发生什么：

let sentence = "JavaScript is awesome!";
let position = sentence.indexOf("fantastic");
console.log(position); // -1
Since the word fantastic does not appear in the string, the method returns -1.
由于单词 fantastic 未出现在字符串中，因此该方法返回 -1。

You can also specify where to begin searching within the string by providing a second argument to indexOf(). Here’s an example:
您还可以通过向 indexOf（） 提供第二个参数来指定在字符串中开始搜索的位置。这是一个例子：

let sentence = "JavaScript is awesome, and JavaScript is powerful!";
let position = sentence.indexOf("JavaScript", 10);
console.log(position); // 27
In this case, the search for JavaScript begins after the 10th character, and so the second occurrence of JavaScript is found at index 27.
在这种情况下，对 JavaScript 的搜索在第 10 个字符之后开始，因此第二次出现的 JavaScript 位于索引 27 处。

It is important to note that the indexOf() method is case sensitive.
重要的是要注意 indexOf（） 方法区分大小写。

In this example, the following would return -1 because the capital letter F is not found in the string freeCodeCamp.
在此示例中，以下内容将返回 -1，因为在字符串 freeCodeCamp 中找不到大写字母 F。

console.log("freeCodeCamp".indexOf("F")) // -1
Using indexOf() can be very useful when you need to check if a substring is present in a string and to determine its position for further operations.
当您需要检查字符串中是否存在子字符串并确定其位置以进行进一步作时，使用 indexOf（） 非常有用。

## What Is the prompt() Method, and How Does It Work?
什么是 prompt（） 方法，它是如何工作的？
The prompt() method is an important part of JavaScript's interaction with the user. It’s one of the simplest ways to get input from a user through a small pop-up dialog box.
prompt（） 方法是 JavaScript 与用户交互的重要组成部分。这是通过小型弹出对话框获取用户输入的最简单方法之一。

You'll often see it used in cases where the webpage needs a piece of information from the user, such as a name or some other form of text input.
您经常会看到它在网页需要用户提供的信息（例如姓名或其他形式的文本输入）的情况下使用。

So, what exactly does the prompt() method do? It opens a dialog box that asks the user for some input, and then it returns the text entered by the user as a string.
那么，prompt（） 方法到底有什么作用呢？它打开一个对话框，要求用户输入一些输入，然后将用户输入的文本作为字符串返回。

The prompt() method takes two arguments: The first one is the message which will appear inside the dialog box, typically prompting the user to enter information. And the second one is a default value which is optional and will fill the input field initially.
prompt（） 方法接受两个参数：第一个是将出现在对话框中的消息，通常提示用户输入信息。第二个是可选的默认值，最初将填充输入字段。

Here's an example of how it works:
以下是其工作原理的示例：

let userName = prompt("What is your name?", "Guest");
In this example, the prompt() method displays a dialog box with the message What is your name? and an input field that initially contains the value Guest.
在此示例中，prompt（） 方法显示一个对话框，其中包含消息“What is your name？”，以及一个最初包含值 Guest 的输入字段。

If the user types their name and presses "OK", the userName variable will store the entered value. If the user presses "Cancel," the userName variable will be set to null. null signifies that the user did not provide any input.
如果用户输入其名称并按“确定”，则 userName 变量将存储输入的值。如果用户按“取消”，则 userName 变量将设置为 null。null 表示用户未提供任何输入。

When the page first loads, you'll see the prompt dialog box appear with the message What is your name? and the input field pre-filled with Guest.
首次加载页面时，您将看到提示对话框出现，其中包含消息“ 你的名字是什么？”，以及预填充“ 访客 ”的输入字段。

Keep in mind that the prompt() method will halt the execution of the script until the user interacts with the dialog box.
请记住，prompt（） 方法将停止脚本的执行，直到用户与对话框交互。

This means the rest of your JavaScript code won’t run until the user either provides input and clicks "OK", or cancels the prompt.
这意味着在用户提供输入并单击“确定”或取消提示之前，其余的 JavaScript 代码不会运行。

One other point to consider is that while prompt() is useful for quick testing or small applications, it's generally avoided in modern, complex web applications due to its disruptive nature and inconsistent behavior across different browsers.
另一点需要考虑的是，虽然 prompt（） 对于快速测试或小型应用程序很有用，但由于其破坏性和不同浏览器之间的不一致行为，在现代、复杂的 Web 应用程序中通常会避免使用它。

Here's an example:  这是一个例子：

let age = prompt("How old are you?");
if (age !== null) {
  console.log("You are " + age + " years old.");
} else {
  console.log("User canceled the prompt.");
}
In this example, if the user provides input, it will be displayed in the console. If they cancel, the console will log that the user canceled the prompt.
在此示例中，如果用户提供输入，则该输入将显示在控制台中。如果他们取消，控制台将记录用户取消了提示。

By understanding the prompt() method, you gain a simple way to interact with users and retrieve information directly through the browser, even though it may not be widely used in modern web applications.
通过了解 prompt（） 方法，您可以获得一种与用户交互并直接通过浏览器检索信息的简单方法，即使它可能不会在现代 Web 应用程序中广泛使用。
