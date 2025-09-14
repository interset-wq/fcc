/* 函数 */


/* 无返回值函数 */

// 函数声明
function greet() {
    console.log("Hello, Jessica!");
}
// 函数调用
greet(); // Hello, Jessica!


function greet1(name) {
    console.log("Hello, " + name + "!");
}

greet1("Alice"); // Hello, Alice!
greet1("Nick"); // Hello, Nick!

// 无返回值函数，默认返回undefined
let greetAlice = greet1("Alice"); // Hello, Alice!
console.log(greetAlice); // undefined


/* 有返回值的函数 */
function calculateSum(num1, num2) {
    return num1 + num2;
}

console.log(calculateSum(3, 4)); // 7



/* 匿名函数 */
const sum = function (num1, num2) {
    return num1 + num2;
};

console.log(sum(3, 4)); // 7


/* 参数默认值 */
function greetings(name = "Guest") {
    console.log(`Hello, ${name}!`);
}

greetings(); // Hello, Guest!
greetings("Anna"); // Hello, Anna!