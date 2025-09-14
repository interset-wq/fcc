# Build a Boolean Check Function
构建一个布尔检查函数
In this lab you will build a function that check if a value is classified as a boolean primitive.
在这个实验中，你将构建一个函数来检查一个值是否被分类为布尔原始类型。

Boolean primitives are true and false.
布尔原始类型是 true 和 false 。

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
目标：完成以下用户故事，并让所有测试通过以完成实验。

User Stories:  用户故事：

You should have a function called booWho that receives one argument.
你应该有一个名为 booWho 的函数，它接收一个参数。
If the argument received is a boolean primitive, the function should return true.
如果接收到的参数是布尔原始类型，函数应该返回 true 。
If the argument is any other value, the function should return false.
如果参数是其他任何值，函数应该返回 false 。
Run the Tests (Ctrl + Enter)
运行测试（Ctrl + Enter）
Reset this lesson  重置本课程
Get Help
  获取帮助
Tests  测试
Waiting:1. You should have a booWho function.
1. 你应该有一个 booWho 函数。
Waiting:2. booWho(true) should return true.
2. booWho(true) 应该返回 true 。
Waiting:3. booWho(false) should return true.
3. booWho(false) 应该返回 true 。
Waiting:4. booWho([1, 2, 3]) should return false.
4. booWho([1, 2, 3]) 应返回 false .
Waiting:5. booWho([].slice) should return false.
5. booWho([].slice) 应返回 false .
Waiting:6. booWho({ "a": 1 }) should return false.
6. booWho({ "a": 1 }) 应返回 false .
Waiting:7. booWho(1) should return false.
7. booWho(1) 应返回 false .
Waiting:8. booWho(NaN) should return false.
8. booWho(NaN) 应返回 false .
Waiting:9. booWho("a") should return false.
9. booWho("a") 应返回 false .
Waiting:10. booWho("true") should return false.
10. booWho("true") 应返回 false .
Waiting:11. booWho("false") should return false.
11. booWho("false") 应返回 false .