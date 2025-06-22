def f(x: float) -> float:
    """math function f(x) = 4x + 3"""
    y = 4*x + 3
    return y

print(5, '\t', f(5))

for x in range(11):
    print(x, '\t', f(x))