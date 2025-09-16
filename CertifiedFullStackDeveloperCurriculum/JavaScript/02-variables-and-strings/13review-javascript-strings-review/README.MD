# JavaScript Strings Review 字符串

## String Basics  字符串基础知识

Definition: A string is a sequence of characters wrapped in either single quotes, double quotes or backticks. Strings are primitive data types and they are immutable. Immutability means that once a string is created, is cannot be changed.

定义 ：字符串是用单引号、双引号或反引号括起来的字符序列。字符串是原始数据类型，它们是不可变的。不变性意味着一旦创建了字符串，就无法更改。

Accessing Characters from a String: To access a character from a string you can use bracket notation and pass in the index number. An index is the position of a character within a string, and it is zero-based.

从字符串中访问字符 ：要从字符串中访问字符，您可以使用括号表示法并传入索引号。索引是字符串中字符的位置，它从零开始。

    const developer = "Jessica";
    developer[0] // J

`\n` (Newline Character): You can create a newline in a string by using the \n newline character.

\n（换行符）： 您可以使用 \n 换行符在字符串中创建换行符。

const poem = "Roses are red,\nViolets are blue,\nJavaScript is fun,\nAnd so are you.";
console.log(poem);

Escaping Strings: You can escape characters in a string by placing backlashes (\) in front of the quotes.

转义字符串 ：您可以通过在引号前面放置反衬 （\） 来转义字符串中的字符。

const statement = "She said, \"Hello!\"";
console.log(statement); // She said, "Hello!"

## Template Literals (Template Strings) and String Interpolation 模板文字（模板字符串）和字符串插值

Definition: Template literals are defined with backticks (`). They allow for easier string manipulation, including embedding variables directly inside a string, a feature known as string interpolation.

定义 ：模板文字使用反引号 （'） 定义。它们允许更轻松地进行字符串作，包括直接在字符串中嵌入变量，这一功能称为字符串插值。

const name = "Jessica";
const greeting = `Hello, ${name}!`; // "Hello, Jessica!"

## ASCII, the charCodeAt() Method and the fromCharCode() Method 字符和ASCII相互转换

ASCII: ASCII, short for American Standard Code for Information Interchange, is a character encoding standard used in computers to represent text. It assigns a numeric value to each character, which is universally recognized by machines.

ASCII：ASCII 是美国信息交换标准代码的缩写，是计算机中用于表示文本的字符编码标准。它为每个字符分配一个数值，该值被机器普遍识别。

The `charCodeAt()` Method: This method is called on a string and returns the ASCII code of the character at a specified index.

charCodeAt（） 方法 ：此方法在字符串上调用，并在指定索引处返回字符的 ASCII 代码。

const letter = "A";
console.log(letter.charCodeAt(0));  // 65

The `fromCharCode()` Method: This method converts an ASCII code into its corresponding character.

fromCharCode（） 方法 ：此方法将 ASCII 代码转换为其相应的字符。

const char = String.fromCharCode(65);
console.log(char);  // A

## Other Common String Methods 其他常见字符串方法

The `indexOf` Method: This method is used to search for a substring within a string. If the substring is found, indexOf returns the index (or position) of the first occurrence of that substring. If the substring is not found, indexOf returns -1, which indicates that the search was unsuccessful.

indexOf 方法 ：此方法用于搜索字符串中的子字符串。如果找到子字符串，则 indexOf 返回该子字符串第一次出现的索引（或位置）。如果未找到子字符串，则 indexOf 返回 -1，这表示搜索不成功。

const text = "The quick brown fox jumps over the lazy dog.";
console.log(text.indexOf("fox")); // 16
console.log(text.indexOf("cat")); // -1

The `includes()` Method: This method is used to check if a string contains a specific substring. If the substring is found within the string, the method returns true. Otherwise, it returns false.

includes（） 方法 ：此方法用于检查字符串是否包含特定的子字符串。如果在字符串中找到子字符串，则该方法返回 true。否则，它返回 false。

const text = "The quick brown fox jumps over the lazy dog.";
console.log(text.includes("fox")); // true
console.log(text.includes("cat")); // false

The `slice()` Method: This method extracts a portion of a string and returns a new string, without modifying the original string. It takes two parameters: the starting index and the optional ending index.

slice（） 方法 ：此方法提取字符串的一部分并返回新字符串，而不修改原始字符串。它需要两个参数：起始索引和可选的结束索引。

const text = "freeCodeCamp";
console.log(text.slice(0, 4));  // "free"
console.log(text.slice(4, 8));  // "Code"
console.log(text.slice(8, 12)); // "Camp"

The `toUpperCase()` Method: This method converts all the characters to uppercase letters and returns a new string with all uppercase characters.

toUpperCase（） 方法 ：此方法将所有字符转换为大写字母，并返回包含所有大写字符的新字符串。

const text = "Hello, world!";
console.log(text.toUpperCase()); // "HELLO, WORLD!"

The `toLowerCase()` Method: This method converts all characters in a string to lowercase.

toLowerCase（） 方法 ：此方法将字符串中的所有字符转换为小写。

const text = "HELLO, WORLD!"
console.log(text.toLowerCase()); // "hello, world!"

The `replace()` Method: This method is used to find a specified value (like a word or character) in a string and replace it with another value.

replace（） 方法 ：此方法用于在字符串中查找指定值（如单词或字符）并将其替换为另一个值。

const text = "I like cats";
console.log(text.replace("cats", "dogs")); // "I like dogs"

The `repeat()` Method: This method is used to repeat a string a specified number of times.

repeat（） 方法 ：此方法用于重复字符串指定次数。

const text = "Hello";
console.log(text.repeat(3)); // "HelloHelloHello"

The `trim()` Method: This method is used to remove whitespaces from both the beginning and the end of a string.

trim（） 方法 ：此方法用于删除字符串开头和结尾的空格。

const text = "  Hello, world!  ";
console.log(text.trim()); // "Hello, world!"

The `trimStart()` Method: This method removes whitespaces from the beginning (or "start") of the string.

trimStart（） 方法 ：此方法从字符串的开头（或“开始”）中删除空格。

const text = "  Hello, world!  ";
console.log(text.trimStart()); // "Hello, world!  "

The `trimEnd()` Method: This method removes whitespaces from the end of the string.

trimEnd（） 方法 ：此方法从字符串末尾删除空格。

const text = " Hello, world! ";
console.log(text.trimEnd()); // "  Hello, world!"

The prompt() Method: This method of the window is used to get information from a user through the form of a dialog box. This method takes two arguments. The first argument is the message which will appear inside the dialog box, typically prompting the user to enter information. The second one is a default value which is optional and will fill the input field initially.

prompt（） 方法 ： 窗口的这种方法用于通过对话框的形式从用户那里获取信息。此方法采用两个参数。第一个参数是将出现在对话框中的消息，通常提示用户输入信息。第二个是可选的默认值，最初将填充输入字段。

const answer = window.prompt("What's your favorite animal?"); // This will change depending on what the user answers