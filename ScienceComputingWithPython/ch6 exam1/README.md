# Build an Arithmetic Formatter Project 构建一个算术格式化器项目

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

小学生经常列竖式计算加减法：

      235
    +  52
    -----

Finish the `arithmetic_arranger` function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.

函数 `arithmetic_arranger()` 接受一个字符串列表，每个字符串都是一个数学加减法问题，将这些问题返回成列竖式的形式。函数还有一个可选参数，如果这个参数设置为True，那么也要列出计算结果

## Example

Function Call:

    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:

       32      3801      45      123
    + 698    -    2    + 43    +  49
    -----    ------    ----    -----

Function Call:

    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:

      32         1      9999      523
    +  8    - 3801    + 9999    -  49
    ----    ------    ------    -----
      40     -3800     19998      474

## Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

如果传参正确，这个函数会返回正确的结果，如果不正确将抛出异常

- Situations that will return an error:
    - If there are too many problems supplied to the function. The limit is five, anything more will return: `'Error: Too many problems.'` 
    - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: `"Error: Operator must be '+' or '-'."`
    - Each number (operand) should only contain digits. Otherwise, the function will return: `'Error: Numbers must only contain digits.'`
    - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: `'Error: Numbers cannot be more than four digits.'`
- If the user supplied the correct format of problems, the conversion you return will follow these rules:
    - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    - Numbers should be right-aligned.
    - There should be four spaces between each problem.
    - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

Note: open the browser console with F12 to see a more verbose output of the tests.

- 抛出异常的情形：
    - 最多5个加减法计算
    - 运算符号只能是加减
    - 每个数字中只能包含数字
    - 每个操作数最多是四位数字
- 正常运行的情形：
    - 运算符号跟最长的数字之间有一个空格，按照列竖式的格式
    - 数字要右对齐
    - 每个问题之间要有四个空格分隔
    - 用虚线，虚线的长度应该与前面平齐


5. arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) should return 'Error: Too many problems.'.
6. arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) should return "Error: Operator must be '+' or '-'.".
7. arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers cannot be more than four digits.'.
8. arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers must only contain digits.'.