# JavaScript Comparisons and Conditionals Review

## Comparisons and the null and undefined Data Types 比较和 null 和 undefined 数据类型

Comparisons and undefined: A variable is undefined when it has been declared but hasn't been assigned a value. It's the default value of uninitialized variables and function parameters that weren't provided an argument. undefined converts to NaN in numeric contexts, which makes all numeric comparisons with undefined return false.
比较和 undefined : 当变量被声明但未分配值时，它是 undefined 。它是未初始化变量和未提供参数的函数参数的默认值。 undefined 在数值上下文中转换为 NaN ，这使得所有与 undefined 的数值比较都返回 false 。

console.log(undefined > 0);  // false
console.log(undefined < 0);  // false
console.log(undefined == 0); // false

Comparisons and null: The null type represents the intentional absence of a value. When using the equality operator, null and undefined are considered equal. However, when using the strict equality operator (===), which checks both value and type without performing type coercion, null and undefined are not equal:
比较和 null : null 类型表示有意不存在的值。在使用相等运算符时， null 和 undefined 被视为相等。然而，在使用严格相等运算符（ === ）时，它检查值和类型而不执行类型转换， null 和 undefined 不相等：

console.log(null == undefined); // true
console.log(null === undefined); // false

### switch Statements   switch 语句

Definition: A switch statement evaluates an expression and matches its value against a series of case clauses. When a match is found, the code block associated with that case is executed. A break statement should be placed at the end of each case, to terminate its execution and continue with the next. The default case is an optional case and only executes if none of the other cases match. The default case is placed at the end of a switch statement.
定义： switch 语句评估一个表达式，并将其值与一系列 case 子句进行匹配。当找到匹配项时，与该情况相关的代码块将被执行。每个 break 语句应放置在每个子句的末尾，以终止其执行并继续下一个子句。 default 子句是一个可选子句，只有当其他子句都不匹配时才会执行。 default 子句放置在 switch 语句的末尾。

const dayOfWeek = 3; 

switch (dayOfWeek) {
  case 1:
    console.log("It's Monday! Time to start the week strong.");
    break;
  case 2:
    console.log("It's Tuesday! Keep the momentum going.");
    break;
  case 3:
    console.log("It's Wednesday! We're halfway there.");
    break;
  case 4:
    console.log("It's Thursday! Almost the weekend.");
    break;
  case 5:
    console.log("It's Friday! The weekend is near.");
    break;
  case 6:
    console.log("It's Saturday! Enjoy your weekend.");
    break;
  case 7:
    console.log("It's Sunday! Rest and recharge.");
    break;
  default:
    console.log("Invalid day! Please enter a number between 1 and 7.");
}