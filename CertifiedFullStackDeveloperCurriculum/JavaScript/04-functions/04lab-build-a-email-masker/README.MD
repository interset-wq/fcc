# Build an Email Masker  构建一个邮箱掩码器
In this lab, you will mask the username part of an email address with asterisks. Masking is a term used to hide or replace sensitive information with asterisks or other characters.
在本实验中，你将用星号掩码邮箱地址的用户名部分。掩码是一个用来隐藏或用星号或其他字符替换敏感信息的术语。

For example, if the email address was myEmail@email.com, then the masked email address will be m*****l@email.com.
例如，如果邮箱地址是 myEmail@email.com ，那么掩码后的邮箱地址将是 m*****l@email.com 。

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
目标：完成以下用户故事，并让所有测试通过以完成实验。

User Stories:  用户故事：

Create a function named maskEmail that takes email as an argument.
创建一个名为 maskEmail 的函数，该函数接受 email 作为参数。
Inside the function, you should mask the email and append the domain name to it. Remember that you can use methods like slice, repeat, indexOf or even replace to help you.
在函数内部，你应该掩码 email 并追加域名到它。记住你可以使用 slice 、 repeat 、 indexOf 甚至 replace 等方法来帮助你。
Outside the function, declare a variable named email to store the email address you want to mask.
在函数外部，声明一个名为 email 的变量来存储你想掩码的电子邮件地址。
Call the maskEmail function with the email variable and output the result to the console.
调用 maskEmail 函数，使用 email 变量，并将结果输出到控制台。
maskEmail("apple.pie@example.com") should return "a*******e@example.com".
maskEmail("apple.pie@example.com") 应返回 "a*******e@example.com" 。
maskEmail("freecodecamp@example.com") should return "f**********p@example.com".
maskEmail("freecodecamp@example.com") 应返回 "f**********p@example.com" 。
maskEmail("info@test.dev") should return "i**o@test.dev".
maskEmail("info@test.dev") 应返回 "i**o@test.dev" 。
maskEmail("user@domain.org") should return "u**r@domain.org".
maskEmail("user@domain.org") 应返回 "u**r@domain.org" 。
Run the Tests (Ctrl + Enter)
运行测试（Ctrl + Enter）
Reset this lesson  重置本课程
Get Help
  获取帮助
Tests  测试
Waiting:1. You should define a function named maskEmail.
1. 你应该定义一个名为 maskEmail 的函数。
Waiting:2. The maskEmail function should take a string, email as an argument.
2. maskEmail 函数应该接受一个字符串 email 作为参数。
Waiting:3. Outside the function, you should have an email variable.
3. 在函数外部，你应该有一个 email 变量。
Waiting:4. You should assign a valid email address to your email variable.
4. 你应该为你的 email 变量分配一个有效的电子邮件地址。
Waiting:5. maskEmail("apple.pie@example.com") should return "a*******e@example.com".
5. maskEmail("apple.pie@example.com") 应返回 "a*******e@example.com" .
Waiting:6. maskEmail("freecodecamp@example.com") should return "f**********p@example.com".
6. maskEmail("freecodecamp@example.com") 应返回 "f**********p@example.com" .
Waiting:7. maskEmail("info@test.dev") should return "i**o@test.dev".
7. maskEmail("info@test.dev") 应返回 "i**o@test.dev" .
Waiting:8. maskEmail("user@domain.org") should return "u**r@domain.org".
8. maskEmail("user@domain.org") 应返回 "u**r@domain.org" .
Waiting:9. Your maskEmail should produce the correct result.
9. 你的 maskEmail 应该产生正确的结果。
Waiting:10. You should log the output of calling maskEmail with email as argument.
10. 你应该记录调用 maskEmail 并以 email 作为参数的输出。