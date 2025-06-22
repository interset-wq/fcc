from random import randint

# convert input str to float
def string_frac(in_string: str) -> float:
    """convert input str to float"""
    if '/' in in_string:
        # numerator(分子), denominator(分母)
        nd = in_string.split('/')
        n = float(nd[0])
        d = float(nd[1])
        ans = n / d
    else:
        ans = float(in_string)
    
    return ans


def one_step_add() -> None:
    """Random question and you should try to answer it"""
    # display problem
    a = randint(-4, 10)
    b = randint(2, 24)
    print('x + ', a, ' =', b)
    ans = float(input('x = '))
    answer = b - a

    # test input ans
    if ans == answer:
        print('Correct!')
    else:
        print('Try again')
        print('The correct answer is ', answer)


def one_step_mult() -> None:
    a = randint(1, 11)
    b = randint(2, 24)
    # display problem
    print(a, ' * x = ', b)
    ans = input('x = ')
    answer = b / a
    # test
    if string_frac(ans) == answer:
        print('Correct!')
    else:
        print('Try again')
        print('The correct answer is ', answer)       



if __name__ == '__main__':
    a = string_frac('3')
    print(a)
    one_step_add()
    one_step_mult()