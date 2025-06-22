from sympy import symbols, var, factor

x, y = var('x, y')

eq = x**2 - 4

print(factor(eq))
