/* 数据类型 */


// 在js中整数和浮点数统称为 number 类型
let integer = 1;
let floatPoint = 1.5;
console.log(typeof integer); // number
console.log(typeof floatPoint); // number

// 字符串 string 类型
// 使用单引号，双引号，反引号包裹
let str = 'hello world';
console.log(typeof str); // string

// true和false是布尔值 boolean 类型
let isOk = true;
let isRight = false;
console.log(typeof isOk); // boolean
console.log(typeof isRight); // boolean

// 未初始化的变量值和类型都是 undefined
let hello;
console.log(hello); // undefined
console.log(typeof hello); // undefined

// null是一种特殊的对象 object 类型
let obj = null;
console.log(obj); // null
console.log(typeof obj); // object

// 属性名值对是对象 object 类型
let pet = {
    name: "Fluffy",
    age: 3,
    type: "dog"
};
console.log(typeof pet); // object

// 标识符 symbol 类型
// 每个标识符都是唯一的，Symbol传入的参数只是这个标识符的描述信息
const crypticKey1 = Symbol("saltNpepper");
const crypticKey2 = Symbol("saltNpepper");
console.log(typeof crypticKey1) // symbol
console.log(crypticKey1 === crypticKey2); // false

// 后缀n表示很大的整数 bigint 类型
const veryBigNumber = 1234567890123456789012345678901234567890n;
console.log(veryBigNumber); // 1234567890123456789012345678901234567890n
console.log(typeof veryBigNumber); // bigint

/* 连接字符串 */

// 字符串加法
let studentName = "Asad";
let studentAge = 25;
let studentInfo = studentName + " is " + studentAge + " years old.";
console.log(studentInfo); // Asad is 25 years old.

let message = "Welcome to programming, ";
message += "Asad!";
console.log(message); // Welcome to programming, Asad!

// .concat()方法
let firstName = "John";
let lastName = "Doe";
let fullName = firstName.concat(" ", lastName);
console.log(fullName); // John Doe

/* js是动态类型 */
let error = 404; // JavaScript treats error as a number
console.log(typeof error); // number
error = "Not Found"; // JavaScript now treats error as a string
console.log(typeof error); // string