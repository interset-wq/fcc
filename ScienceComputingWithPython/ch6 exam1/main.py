def arithmetic_arranger(problems: list[str], show_answers: bool=False) -> str:
    """将加减法运算转化为列竖式的格式"""

    # 最多5个问题
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    # two_num_list = []
    questions = []
    # 只能能是加减法
    for problem in problems:
        if '+' not in problem and '-' not in problem:
            raise ValueError("Error: Operator must be '+' or '-'.")
        else:
            if '+' in problem:
                two_num = [i.strip(' ') for i in problem.split('+')]
                for num in two_num:
                    if not num.isdigit():
                        raise ValueError('Error: Numbers must only contain digits.')
                    if len(num) > 4:
                        raise ValueError('Error: Numbers cannot be more than four digits.')
                two_num.append('+')
                questions.append(two_num)
            elif '-' in problem:
                two_num = [i.strip(' ') for i in problem.split('-')]
                for num in two_num:
                    if not num.isdigit():
                        raise ValueError('Error: Numbers must only contain digits.')
                    if len(num) > 4:
                        raise ValueError('Error: Numbers cannot be more than four digits.')
                # two_num_list.append(two_num)
                two_num.append('-')
                questions.append(two_num)
    
    top_strs = []
    bottom_strs = []
    lines = []
    ans_strs = []
    for question in questions:
        top = question[0]
        bottom = question[1]
        sign = question[2]
        if sign == '+':
            ans = int(top) + int(bottom)
        elif sign == '-':
            ans = int(top) - int(bottom)
        ans = str(ans)
        length = max(len(top), len(bottom)) + 2
        line = '-'*length
        top_str = ' '*(length - len(top)) + top
        bottom_str = sign + ' '*(length-1-len(bottom)) + bottom
        ans_str = ' '*(length - len(ans)) + ans
        lines.append(line)
        top_strs.append(top_str)
        bottom_strs.append(bottom_str)
        ans_strs.append(ans_str)
    print(top_strs)
    space = ' '*4
    top_str_long = space.join(top_strs)
    bottom_str_long = space.join(bottom_strs)
    line_long = space.join(lines)
    ans_str_long = space.join(ans_strs)

    if show_answers:
        problems = f'{top_str_long}\n{bottom_str_long}\n{line_long}\n{ans_str_long}'
    else:
        problems = f'{top_str_long}\n{bottom_str_long}\n{line_long}'
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) 