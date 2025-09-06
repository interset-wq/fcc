/* 字符串操作 */

// 通过索引获取字符串中的字符
const developer = "Jessica";
console.log(developer[0]); // J

// 转义字符escaping strings
const poem = "Roses are red,\nViolets are blue,\nJavaScript is fun,\nAnd so are you.";
console.log(poem);
// Roses are red,
// Violets are blue,
// JavaScript is fun,
// And so are you.

// 模板字符串
const myName = "Jessica";
const greeting = `Hello, ${myName}!`;
console.log(greeting); // "Hello, Jessica!"

/* 字符和ASCII码相互转换 */

// .charCodeAt(0) 将字符转换为ASCII码
const letter = "A";
console.log(letter.charCodeAt(0));  // 65

// String.fromCharCode() 将ASCII码转换为字符
const char = String.fromCharCode(65);
console.log(char);  // A

/* 字符产方法 */

// .indexOf()方法 获取字符的索引，没找到返回-1
const text = "The quick brown fox jumps over the lazy dog.";
console.log(text.indexOf("fox")); // 16
console.log(text.indexOf("cat")); // -1

// .includes()方法 判断某个子字符串是否包含在某个字符串内
const text2 = "The quick brown fox jumps over the lazy dog.";
console.log(text2.includes("fox")); // true
console.log(text2.includes("cat")); // false

// .slice() 字符串切片，左闭右开区间
const text3 = "freeCodeCamp";
console.log(text3.slice(0, 4));  // "free"
console.log(text3.slice(4, 8));  // "Code"
console.log(text3.slice(8, 12)); // "Camp"
console.log(text3.slice(0)); // "freeCodeCamp"

// .toUpperCase() 大写
const text4 = "Hello, world!";
console.log(text4.toUpperCase()); // "HELLO, WORLD!"

// .toLowerCase() 小写
const text5 = "HELLO, WORLD!"
console.log(text5.toLowerCase()); // "hello, world!"

// .replace() 替换 只替换第一个匹配到的
const text6 = "I like cats. There is a cat.";
console.log(text6.replace("cat", "dog"));  // I like dogs. There is a cat.

// .repeat() 字符串重复
const text7 = "Hello";
console.log(text7.repeat(3)); // "HelloHelloHello"

// .trim() 删除左右空白
const text8 = "  Hello, world!  ";
console.log(text8.trim()); // "Hello, world!"

// .trimStart() 删除左侧空白
console.log(text8.trimStart()); // "Hello, world!  "

// .trimEnd() 删除右侧空白
console.log(text8.trimEnd()); // "  Hello, world!"

// prompt() 浏览器弹窗等待用户输入
// 需要在浏览器环境下才能运行
const answer = window.prompt("What's your favorite animal?", 'dog'); // This will change depending on what the user answers