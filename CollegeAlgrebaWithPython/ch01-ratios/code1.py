"""解简单的比例方程"""
# 0 is unknown, numerator(分子), denominator(分母), 
# parentheses(小括号), subtract(减法)

n1 = 1
d1 = 2
n2 = 0 # unknown
d2 = 16

if n2==0:
    # n2 is unknown
    ans = n1 * d2 / d1
    print('n2 = ', ans)

if d2==0:
    # d2 is unknown and we need solve it out
    ans = n2 * d1 / n1
    print('d2 = ', ans)