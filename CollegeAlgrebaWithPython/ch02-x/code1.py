from sympy import symbols
from sympy.solvers import solve # return <class 'list'>

# use symbol to express unknown num,just like x in math
x = symbols('x')
print(type(x))
# equation here, eq==0
# eq = x - 2
eq = input('input your equation here: 0 = ')

# print tha answer
print('x = ', solve(eq, x))
