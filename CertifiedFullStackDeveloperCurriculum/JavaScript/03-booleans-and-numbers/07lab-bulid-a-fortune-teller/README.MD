# Build a Fortune Teller  构建一个占卜师
In this lab, you will define five fortunes and randomly select one of them to display the fortune to the user.
在这个实验中，你需要定义五个命运，并随机选择其中一个来向用户展示命运。

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
目标：完成以下用户故事，并让所有测试通过以完成实验。

User Stories:  用户故事：

You should initialize the five variables fortune1, fortune2, fortune3, fortune4, and fortune5 with a string value of your choice. You can use the below options if you like:
你应该将五个变量 fortune1 、 fortune2 、 fortune3 、 fortune4 和 fortune5 初始化为你选择的字符串值。如果你喜欢，可以使用下面的选项：

"Your cat will look very cuddly today."
"The weather will be nice tomorrow."
"Be cautious of your new neighbors."
"You will find a new hobby soon."
"It would be wise to avoid the color red today."
You should select a random number between 1 and 5, inclusive, and assign it to the variable randomNumber.
你应该在 1 到 5 之间（包括 1 和 5）选择一个随机数，并将其赋值给变量 randomNumber 。

You should create a selectedFortune variable and assign the appropriate fortune based on these rules:
你应该创建一个 selectedFortune 变量，并根据这些规则分配相应的运势：

If randomNumber is 1, assign the value of fortune1 to selectedFortune.
如果 randomNumber 是 1，将 fortune1 的值赋给 selectedFortune 。
If randomNumber is 2, assign the value of fortune2 to selectedFortune.
如果 randomNumber 是 2，将 fortune2 的值赋给 selectedFortune 。
If randomNumber is 3, assign the value of fortune3 to selectedFortune.
如果 randomNumber 是 3，将 fortune3 的值赋给 selectedFortune 。
If randomNumber is 4, assign the value of fortune4 to selectedFortune.
如果 randomNumber 是 4，将 fortune4 的值赋给 selectedFortune 。
If randomNumber is 5, assign the value of fortune5 to selectedFortune.
如果 randomNumber 是 5，将 fortune5 的值赋给 selectedFortune 。
You should log the selectedFortune to the console.
你应该将 selectedFortune 记录到控制台。

Run the Tests (Ctrl + Enter)
运行测试 (Ctrl + Enter)
Reset this lesson  重置本课程
Get Help
  获取帮助
Tests  测试
Waiting:1. You should initialize fortune1 with a string value.
1. 你应该用字符串值初始化 fortune1 。
Waiting:2. You should initialize fortune2 with a string value.
2. 你应该用字符串值初始化 fortune2 。
Waiting:3. You should initialize fortune3 with a string value.
3. 你应该用字符串值初始化 fortune3 。
Waiting:4. You should initialize fortune4 with a string value.
4. 你应该用字符串值初始化 fortune4 。
Waiting:5. You should initialize fortune5 with a string value.
5. 你应该用字符串值初始化 fortune5 。
Waiting:6. You should use the Math.random() method to generate a random number.
6. 你应该使用 Math.random() 方法来生成一个随机数。
Waiting:7. You should generate a random number between 1 and 5, inclusive, and assign it to the variable randomNumber.
7. 你应该生成一个在 1 到 5 之间（包括 1 和 5）的随机数，并将其赋值给变量 randomNumber 。
Waiting:8. You should have a selectedFortune variable that is assigned a value based on the value of randomNumber.
8. 你应该有一个 selectedFortune 变量，它的值根据 randomNumber 的值来赋值。
Waiting:9. The randomNumber should correspond to its fortune. For example, if randomNumber is 1, the selectedFortune should be equal to fortune1 and so on.
9. randomNumber 应与其命运相对应。例如，如果 randomNumber 是 1，那么 selectedFortune 应该等于 fortune1 ，以此类推。
Waiting:10. You should output the selectedFortune to the console.
10. 你应该将 selectedFortune 输出到控制台。