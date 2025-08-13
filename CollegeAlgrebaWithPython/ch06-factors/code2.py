"""convert demical to fraction"""

def greatest_common_factor(a: int, b: int) -> int:
    """find the greatest common factor"""
    end = a if a <= b else b
    greatest = 1
    # print(end)
    for i in range(1, end + 1):
        if a % i == 0 and b % i == 0:
            greatest = i
    return greatest
            

num = input('Input a demical: ')
digits = len(num) - 1
num = float(num)
numerator = int(num * 10**digits)
denominator = 10**digits

g = greatest_common_factor(numerator, denominator)
n = int(numerator / g)
d = int(denominator / g)

print(f'demical: {num}')
print(f'fraction: {numerator}/{denominator}')
print(f'reduced: {n}/{d}')
