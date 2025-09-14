# Build a Card Counting Assistant
构建一张卡片计数助手
In the casino game Blackjack, a player can determine whether they have an advantage on the next hand over the house by keeping track of the relative number of high and low cards remaining in the deck. This is called Card Counting.
在赌场游戏二十一点中，玩家可以通过跟踪牌堆中剩余的高牌和低牌的相对数量来确定他们是否在下一局中比赌场有优势。这被称为卡片计数。

Having more high cards remaining in the deck favors the player. When the count is positive, the player should bet high. When the count is zero or negative, the player should bet low.
牌堆中剩余的高牌越多，对玩家越有利。当计数为正时，玩家应该下大注。当计数为零或负时，玩家应该下小注。

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
目标：完成以下用户故事，并让所有测试通过以完成实验。

User Stories:  用户故事：

You should use let to declare a global variable named count and set it to 0.
你应该使用 let 来声明一个名为 count 的全局变量，并将其设置为 0 。
You should have a function called cc.
你应该有一个名为 cc 的函数。
The cc function should receive a card parameter which can either be a number or string.
cc 函数应该接收一个 card 参数，该参数可以是数字或字符串。
For values between 2 to 10, the card parameter will be a number.
对于值在 2 到 10 之间的情况， card 参数将是一个数字。
For all other values, the card parameter will be a string.
对于所有其他值， card 参数将是一个字符串。
The cc function should modify the global count variable based on certain criteria.
cc 函数应根据特定标准修改全局 count 变量。
The global count variable should be increased by 1 for the cards 2, 3,4, 5, or 6
全局 count 变量应对于卡片 2 、 3 、 4 、 5 或 6 增加 1 。
The global count variable should remain unchanged for the cards 7, 8, 9.
全局 count 变量应对于卡片 7 、 8 、 9 保持不变。
The global count variable should be decreased for the cards 10, "J", "Q", "K", "A"
全局变量 count 应为卡片 10 、 "J" 、 "Q" 、 "K" 、 "A" 减少一个值
The cc function should return a string with current count and the string Bet if the count is positive.
函数 cc 应当返回一个包含当前计数和字符串 Bet 的字符串，如果计数为正数。
The cc function should return a string with current count and the string Hold if the count is less than or equal to 0.
函数 cc 应该返回一个包含当前计数和字符串 Hold 的字符串，如果计数小于或等于 0 。
In the function output, the current count and the player's decision (Bet or Hold) should be separated by a space. For example, -3 Hold.
在函数输出中，当前计数和玩家的决定（ Bet 或 Hold ）之间应该用空格隔开。例如， -3 Hold 。
Run the Tests (Ctrl + Enter)
运行测试（Ctrl + Enter）
Reset this lesson  重置本课程
Get Help
  获取帮助
Tests  测试
Waiting:1. You should use let to declare a global variable named count and set it to 0.
1. 你应该使用 let 来声明一个名为 count 的全局变量，并将其设置为 0 。
Waiting:2. You should have a function named cc.
2. 你应该有一个名为 cc 的函数。
Waiting:3. Your function should return the value of count and the text (Bet or Hold) with one space character between them.
3. 你的函数应该返回 count 的值和文本（ Bet 或 Hold ），两者之间用一个空格字符隔开。
Waiting:4. After the cards 2, 3, 4, 5, then calling cc(6) should return the string 5 Bet.
4. 在卡片 2 、 3 、 4 、 5 之后，调用 cc(6) 应该返回字符串 5 Bet 。
Waiting:5. After the cards 7, 8, then calling cc(9) should return the string 0 Hold.
5. 在卡片 7 ， 8 之后，调用 cc(9) 应该返回字符串 0 Hold 。
Waiting:6. After the cards 10, "J", "Q", "K", then calling cc("A") should return the string -5 Hold.
6. 在卡片 10 ， "J" ， "Q" ， "K" 之后，调用 cc("A") 应该返回字符串 -5 Hold 。
Waiting:7. After the cards 3, 7, "Q", 8, then calling cc("A") should return the string -1 Hold.
7. 在卡片 3 ， 7 ， "Q" ， 8 之后，调用 cc("A") 应该返回字符串 -1 Hold 。
Waiting:8. After the cards 2, "J", 9, 2, then calling cc(7) should return the string 1 Bet.
8. 在卡片 2 ， "J" ， 9 ， 2 之后，调用 cc(7) 应该返回字符串 1 Bet 。
Waiting:9. After the cards 2, 2, then calling cc(10) should return the string 1 Bet.
9. 在卡片 2 ， 2 之后，调用 cc(10) 应该返回字符串 1 Bet 。
Waiting:10. After the cards 3, 2, "A", 10, then calling cc("K") should return the string -1 Hold.
10. 在卡片 3 ， 2 ， "A" ， 10 之后，调用 cc("K") 应该返回字符串 -1 Hold 。