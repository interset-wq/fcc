from sympy import var, Eq
from sympy.solvers import solve

x, y = var('x, y')

first = 2*x + 10

# constract equation, just like math.
# i.e. y = 2*x + 10
eq1 = Eq(first, y)

# figure x out
sol = solve(eq1, x)

print('x = ', sol[0])