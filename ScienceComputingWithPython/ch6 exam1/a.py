def arithmetic_arranger(problems: list[str], show_answers: bool=False) -> str:
    """将加减法运算转化为列竖式的格式"""

    """抛出异常"""
    # 最多5个问题
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    slices_list = []

    for problem in problems:
        slices = problem.split()
        # print(slices, slices[0].isnumeric(), slices[-1].isnumeric())

        # 运算符号必须是加减
        if slices[1] not in '+-':
            raise ValueError("Error: Operator must be '+' or '-'.")
        # 操作数最多是四位数
        elif max([len(slice) for slice in slices]) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        # 操作数只能是数字
        elif not slices[0].isnumeric() and not slices[-1].isnumeric():
            raise ValueError('Error: Numbers must only contain digits.')
        slices_list.append(slices)
    # print(slices_list)
        # break
        # if '+' not in problem and '-' not in problem:
        #     raise ValueError("Error: Operator must be '+' or '-'.")
        # else:
        #     if '+' in problem:
        #         two_num = [i.strip(' ') for i in problem.split('+')]
        #         for num in two_num:
        #             if not num.isdigit():
        #                 raise ValueError('Error: Numbers must only contain digits.')
        #             if len(num) > 4:
        #                 raise ValueError('Error: Numbers cannot be more than four digits.')
        #         two_num.append('+')
        #         questions.append(two_num)
        #     elif '-' in problem:
        #         two_num = [i.strip(' ') for i in problem.split('-')]
        #         for num in two_num:
        #             if not num.isdigit():
        #                 raise ValueError('Error: Numbers must only contain digits.')
        #             if len(num) > 4:
        #                 raise ValueError('Error: Numbers cannot be more than four digits.')
        #         # two_num_list.append(two_num)
        #         two_num.append('-')
        #         questions.append(two_num)
    
    """将问题转换为竖式"""
    top_str_aligns = []
    bottom_str_aligns = []
    lines = []
    ans_str_aligns = []
    for slices in slices_list:
        top_str = slices[0]
        operator = slices[1]
        bottom_str = slices[-1]

        # 计算结果
        if operator == '+':
            ans = int(top_str) + int(bottom_str)
        elif operator == '-':
            ans = int(top_str) - int(bottom_str)
        ans_str = str(ans)

        # 每个问题右对齐
        length = max(len(top_str), len(bottom_str)) + 2
        line = '-'*length
        top_str_align = ' '*(length - len(top_str)) + top_str
        bottom_str_align = operator + ' '*(length-1-len(bottom_str)) + bottom_str
        ans_str_align = ' '*(length - len(ans_str)) + ans_str
        lines.append(line)
        top_str_aligns.append(top_str_align)
        bottom_str_aligns.append(bottom_str_align)
        ans_str_aligns.append(ans_str_align)
    
    space = ' '*4
    top_str_return = space.join(top_str_aligns)
    bottom_str_return = space.join(bottom_str_aligns)
    line_return = space.join(lines)
    ans_str_return = space.join(ans_str_aligns)

    if show_answers:
        problems = f'{top_str_return}\n{bottom_str_return}\n{line_return}\n{ans_str_return}'
    else:
        problems = f'{top_str_return}\n{bottom_str_return}\n{line_return}'
    return problems

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) 
# should return 'Error: Too many problems.'.
# arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) 
# should return "Error: Operator must be '+' or '-'.".
# arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) 
# should return 'Error: Numbers cannot be more than four digits.'.
# arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) 
# should return 'Error: Numbers must only contain digits.'.

# arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
print('3g5'.isnumeric())