numerator = 12
denominator = 24
factor = 1

"""find the great common factor"""

# find all common factors
for i in range(1, denominator + 1):
    if numerator % i == 0 and denominator % i == 0:
        # the last one is the greatest common factor
        print(i)
        factor = i

# divide the greatest common factor
n = int(numerator / factor)
d = int(denominator / factor)

print(f'original: {numerator}/{denominator}')
print(f'reduced: {n}/{d}')