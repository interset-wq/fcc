/* 数学运算 */


// NaN和Infinity是特殊的数字
console.log(typeof NaN); // number
console.log(typeof Infinity); // number

// JS除数可以为0
console.log(1 / 0); // Infinity
console.log(0 / 0); // NaN

/* 强制类型转换 */

// 加法运算，自动转换为字符串
const result = 5 + '10';
console.log(result); // 510
console.log(typeof result); // string

// 减法，乘除运算，自动转换为数字
const subtractionResult = '10' - 5;
console.log(subtractionResult); // 5
console.log(typeof subtractionResult); // number

const multiplicationResult = '10' * 2;
console.log(multiplicationResult); // 20
console.log(typeof multiplicationResult); // number

const divisionResult = '20' / 2;
console.log(divisionResult); // 10
console.log(typeof divisionResult); // number

// null转换为数字0
const result1 = null + 5;
console.log(result1); // 5
console.log(typeof result1); // number

// undefined转换为数字NaN
const result2 = undefined + 5;
console.log(result2); // NaN
console.log(typeof result2); // number

/* 运算顺序 数学运算顺序 */

const result3 = (2 + 3) * 4;
console.log(result3); // 20

const result4 = 10 - 2 + 3;
console.log(result4); // 11

// 幂运算是从右到左计算
const result5 = 2 ** 3 ** 2;
console.log(result5); // 512

/* 自增自减运算 */

let x = 5;
// 前置自增，先自增再返回变量
console.log(++x); // 6
console.log(x); // 6


let y = 5;
// 后置自增，先返回变量再自增
console.log(y++); // 5
console.log(y); // 6

let num = 5;
console.log(--num); // 4
console.log(num--); // 4
console.log(num); // 3


/* 比较运算符 */

// 相等运算符比较时会自动进行类型转换
console.log(5 == '5'); // true
// 严格相等运算符比较时不会自动进行类型转换，即同时要数值和类型相等才返回true
console.log(5 === '5'); // false

/* 一元运算符 */

// 一元加号运算符可以将字符串转换为数字
const str = '42';
const num1 = +str;
console.log(num1); // 42
console.log(typeof num1); // number

// 负号
const num3 = 4;
console.log(-num3); // -4

// 逻辑非
console.log(!true) // false

/* if语句 */
const score = 87;

if (score >= 90) {
    console.log('You got an A');
} else if (score >= 80) {
    console.log('You got a B'); // You got an B
} else if (score >= 70) {
    console.log('You got a C');
} else {
    console.log('You failed! You need to study more!');
}

/* if-else 和 三目运算符 */

const temperature = 30;

// if-else
let weather1;
if (temperature > 25) {
    weather1 = 'sunny';
} else {
    weather1 = 'cool';
}
console.log(`It's a ${weather1} day!`); // It's a sunny day!

// 三目运算符
const weather2 = temperature > 25 ? 'sunny' : 'cool';
console.log(`It's a ${weather2} day!`); // It's a sunny day!


/* 逻辑运算符 */

// 且，都为true返回后面的值，
// 如果有false，返回false对应的值
const result10 = true && 'hello';
console.log(result10); // hello

// 空值合并运算符
// 左边为null或undefined时，返回右边的值
const userSettings = {
    theme: null,
    volume: 0,
    notifications: false,
};

let theme = userSettings.theme ?? 'light';
console.log(theme); // light

/* 数学运算 Math对象 */
