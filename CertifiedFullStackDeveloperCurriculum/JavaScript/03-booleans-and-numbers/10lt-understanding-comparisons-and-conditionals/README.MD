# Understanding Comparisons and Conditionals, Not started
In these lectures, you will learn about comparison operators and conditionals. You will learn how the various conditionals differ from one another, and how comparisons work with null and undefined.

## How Do Comparisons Work with Null and Undefined Data Types?
比较操作符如何处理 null 和 undefined 数据类型？
In JavaScript, null and undefined are two distinct data types that represent the absence of a value, but they behave differently in comparisons. Understanding how these types interact in various comparison scenarios is crucial for writing robust and bug-free code.
在 JavaScript 中， null 和 undefined 是两种不同的数据类型，它们都表示没有值，但在比较时的行为不同。理解这些类型在各种比较场景中的交互对于编写健壮且无 bug 的代码至关重要。

Let's start with the undefined type. A variable is undefined when it has been declared but hasn't been assigned a value. It's the default value of uninitialized variables and function parameters that weren't provided an argument.
让我们先从 undefined 类型开始。当变量被声明但未分配值时，它就是 undefined 。它是未初始化变量的默认值，以及未提供参数的函数参数的默认值。

The null type, on the other hand, is an assignment value that represents a deliberate non-value. It's often used to indicate that a variable intentionally has no value.
另一方面， null 类型是一个赋值值，表示有意不赋值。它通常用于表示变量有意没有值。

When comparing null and undefined using the equality operator (==), JavaScript performs type coercion. This means it tries to convert the operands to the same type before making the comparison. In this case, null and undefined are considered equal:
当使用相等运算符（==）比较 null 和 undefined 时，JavaScript 会进行类型转换。这意味着它会在进行比较之前尝试将操作数转换为相同类型。在这种情况下， null 和 undefined 被视为相等：

console.log(null == undefined); // true
However, when using the strict equality operator (===), which checks both value and type without performing type coercion, null and undefined are not equal:
然而，当使用严格相等运算符（===），它检查值和类型而不进行类型转换时， null 和 undefined 不相等：

console.log(null === undefined); // false
This difference is important to keep in mind when writing conditional statements or performing equality checks in your code. When comparing null or undefined with other values using the equality operator (==), the behavior can be unexpected. For example:
在编写条件语句或在代码中进行相等检查时，需要注意这个差异。当使用相等运算符（==）将 null 或 undefined 与其他值进行比较时，行为可能出乎意料。例如：

console.log(null == 0);  // false
console.log(null == ''); // false
console.log(undefined == 0); // false
console.log(undefined == ''); // false
These comparisons return false because null and undefined are only equal to each other (and themselves) when using the equality operator. The behavior of null in other comparisons is particularly tricky:
这些比较返回 false ，因为 null 和 undefined 只有在使用相等运算符时才彼此相等（以及对自己相等）。 null 在其他比较中的行为尤其难以理解：

console.log(null > 0);  // false
console.log(null == 0); // false
console.log(null >= 0); // true
undefined, on the other hand, always converts to NaN in numeric contexts, which makes all numeric comparisons with undefined return false:
undefined ，另一方面，在数值上下文中始终转换为 NaN ，这使得所有与 undefined 的数值比较都返回 false :

console.log(undefined > 0);  // false
console.log(undefined < 0);  // false
console.log(undefined == 0); // false
Given these nuances, it's generally recommended to use the strict equality operator when comparing values, especially when dealing with null and undefined. This approach helps avoid unexpected type coercion and makes your code's behavior more predictable.
考虑到这些细微差别，通常建议在比较值时使用严格相等运算符，尤其是在处理 null 和 undefined 时。这种方法有助于避免意外的类型强制转换，并使代码的行为更加可预测。

In summary, while null and undefined are both used to represent the absence of a value, they behave differently in comparisons. Understanding these differences is key to writing clear and error-free JavaScript code.
总之，虽然 null 和 undefined 都用于表示空值，但在比较中的行为不同。理解这些差异是编写清晰且无错误的 JavaScript 代码的关键。

## What Are Switch Statements and How Do They Differ from If/Else Chains?
什么是 switch 语句以及它与 if/else 链有何不同？
switch statements and if/else if/else chains are both control flow structures in programming that allow us to execute different code blocks based on certain conditions. However, they have distinct characteristics and use cases.
switch 语句和 if/else if/else 链都是编程中的控制流结构，它们允许我们根据特定条件执行不同的代码块。然而，它们具有不同的特点和用途。

A switch statement evaluates an expression and matches its value against a series of case clauses. When a match is found, the code block associated with that case is executed. Here's a basic structure of a switch statement:
switch 语句评估一个表达式，并将其值与一系列 case 子句进行匹配。当找到匹配项时，与该 case 关联的代码块将被执行。以下是 switch 语句的基本结构：

switch (expression) {
  case value1:
    // code to be executed if expression === value1
    break;
  case value2:
    // code to be executed if expression === value2
    break;
  default:
    // code to be executed if expression doesn't match any case
}
The break statement at the end of each case is crucial. It tells the program to exit the switch block once a matching case has been executed. Without it, the program would continue executing subsequent cases, a behavior known as "fall-through".
每个 case 末尾的 break 语句至关重要。它告诉程序在执行匹配的 case 后退出 switch 块。没有它，程序将继续执行后续的 case，这种行为被称为"穿透"（fall-through）。

switch statements are typically used when you're comparing a single variable against multiple possible values. They're especially useful when you have many potential conditions to check against a single variable. Here is an example using a switch statement for the days of the week:
switch 语句通常用于将单个变量与多个可能值进行比较。当需要对单个变量进行多个潜在条件的检查时，它们尤其有用。这里是一个使用 switch 语句来表示一周中各天的示例：

let dayOfWeek = 3; 

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
switch statements can be more readable and concise when dealing with many possible values for a single variable.
当单个变量有多个可能值时， switch 语句可以更易读和简洁。

if/else if statements on the other hand are more flexible. They can evaluate complex conditions and different variables in each clause. This makes them suitable for a wider range of scenarios. Here is an example of when you might use an if/else statement over a switch statement:
另一方面， if/else if 语句更灵活。它们可以在每个子句中评估复杂的条件和不同的变量。这使得它们适用于更广泛的场景。这里是一个你可能使用 if/else 语句而不是 switch 语句的示例：

let creditScore = 720; 
let annualIncome = 60000; 
let loanAmount = 200000; 

let eligibilityStatus;

if (creditScore >= 750 && annualIncome >= 80000) {
    eligibilityStatus = "Eligible for premium loan rates.";
} else if (creditScore >= 700 && annualIncome >= 50000) {
    eligibilityStatus = "Eligible for standard loan rates.";
} else if (creditScore >= 650 && annualIncome >= 40000) {
    eligibilityStatus = "Eligible for subprime loan rates.";
} else if (creditScore < 650) {
    eligibilityStatus = "Not eligible due to low credit score.";
} else {
    eligibilityStatus = "Not eligible due to insufficient income.";
}

console.log(eligibilityStatus);
In this example, we have a person’s annual income and credit score and checking what types of loan they would qualify for. Since we are dealing with more complex logical evaluations and multiple variables, it is better to use an if/else statement here versus a switch statement.
在这个示例中，我们有一个人的年收入和信用评分，并检查他们可以申请哪种类型的贷款。由于我们这里涉及更复杂的逻辑评估和多个变量，因此使用 if/else 语句比使用 switch 语句更好。

It's worth noting that switch statements in JavaScript use strict comparison (===), which means they don't perform type coercion. This can be an advantage in terms of predictability and avoiding subtle bugs.
值得注意的是，JavaScript 中的 switch 语句使用严格比较（ === ），这意味着它们不会执行类型转换。这在可预测性和避免微妙错误方面可能是一个优势。

In summary, while both switch statements and if/else if chains allow for multiple-branch logic in your code, they have different strengths. switch statements excel at handling multiple possible values for a single variable, while if/else if chains offer more flexibility for complex conditions. The choice between them often comes down to the specific requirements of your code and personal or team coding style preferences.
总而言之，虽然 switch 语句和 if/else if 链都允许在代码中进行多分支逻辑，但它们各有优势。 switch 语句擅长处理单个变量多种可能值的情况，而 if/else if 链则提供了更灵活的复杂条件处理方式。选择它们通常取决于代码的具体需求以及个人或团队的编码风格偏好。