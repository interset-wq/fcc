# Build a Loan Qualification Checker, Not started
In this workshop, you will continue to learn how to work with conditionals by building a loan qualification checker app.

You will learn more about if statements, and how to use comparison operators and multiple conditions in an if statement.

Step 1  第一步
In this workshop, you'll review JavaScript conditionals by building a loan qualification checker app.
在这个工作坊中，你将通过构建一个贷款资格检查器应用程序来复习 JavaScript 条件语句。

The app will check whether the user is eligible for a duplex, car, and condo loan based on their annual income and credit score. A credit score is a number that represents how good you are at managing borrowed money.
该应用程序将根据用户的年收入和信用评分检查用户是否有资格获得联排别墅、汽车和公寓贷款。信用评分是一个数字，代表你管理借入资金的能力。

To get started, create the following variables and values.
开始之前，创建以下变量和值。

Variable Name  变量名	Value  价值
minIncomeForDuplex	60000
minCreditScoreForDuplex	700
minIncomeForCondo	45000
minCreditScoreForCondo	680
minIncomeForCar	30000
minCreditScoreForCar	650

Step 2  第二步
When the user is eligible for a loan, you'll want to display a message to them in the console.
当用户符合贷款资格时，你需要在控制台中向他们显示一条消息。

For that, you'll build out a function inside which you'll have some checks that'll return what loan the applicant is eligible for.
为此，你将构建一个函数，该函数中包含一些检查，用于返回申请人符合的贷款类型。

Create an empty getLoanMessage function with an annualIncome and creditScore parameters.
创建一个空的函数，带有参数 annualIncome 和 creditScore 。

Step 3  步骤 3
To check which loan a user is qualified for based on the annualIncome and creditScore, you have to use if/else if statement or a ternary right inside the getLoanMessage function. You'll then return the appropriate message in the block of each condition.
要根据 annualIncome 和 creditScore 检查用户符合哪种贷款，你必须使用 if/else if 语句或直接在 getLoanMessage 函数内使用三元运算符。然后，在每个条件块中返回适当的消息。

Starting with the duplex loan, check if annualIncome is greater than or equal to minIncomeForDuplex AND if creditScore is greater than or equal to minCreditScoreForDuplex.
首先检查双拼贷款，检查 annualIncome 是否大于或等于 minIncomeForDuplex 并且 creditScore 是否大于或等于 minCreditScoreForDuplex 。

If that condition is true, then the applicant is eligible for a duplex loan and the other loans. So, inside the check, return the string "You qualify for a duplex, condo, and car loan."
如果这个条件为真，那么申请人符合双拼贷款和其他贷款的资格。所以，在检查内部，返回字符串 "You qualify for a duplex, condo, and car loan."

Step 4  步骤 4
If the applicant's annual income is greater than or equal to minIncomeForCondo, AND if their credit score is greater than or equal to minCreditScoreForCondo, then they qualify for a condo and car loan.
如果申请人的年收入大于或等于 minIncomeForCondo ，并且他们的信用评分大于或等于 minCreditScoreForCondo ，那么他们有资格获得公寓和汽车贷款。

Check if that's true in the getLoanMessage function. If it is, return the string "You qualify for a condo and car loan."
在 getLoanMessage 函数中检查这是否属实。如果是，返回字符串 "You qualify for a condo and car loan."

Step 5  步骤 5
Now, you should check if the applicant is qualified for a car loan only. If they are, return the string "You qualify for a car loan.".
现在，你应该检查申请人是否合格获得汽车贷款。如果是，返回字符串 "You qualify for a car loan." 。

Step 6  第六步
If the applicant's annual income and credit score fall below minIncomeForCar and minCreditScoreForCar, then they don't qualify for any loan. So, return the string "You don't qualify for any loans."
如果申请人的年收入和信用评分低于 minIncomeForCar 和 minCreditScoreForCar ，那么他们不符合任何贷款资格。所以，返回字符串 "You don't qualify for any loans."

Step 7  步骤 7
Now, it is time to test out your getLoanMessage function.
现在，是时候测试你的 getLoanMessage 函数了。

Use the table below to create 4 variables and their values:
使用下表创建 4 变量及其值：

Variable Name  变量名	Value  值
duplexLoanMsg	getLoanMessage(85000, 850)
condoLoanMsg	getLoanMessage(65000, 690)
carLoanMsg	getLoanMessage(45000, 660)
noLoanMsg	getLoanMessage(25000, 550)
After that, log each variable to the console to see the messages.
之后，将每个变量记录到控制台以查看消息。

With that, your loan qualification checker project is complete!
至此，你的贷款资格检查器项目就完成了！

