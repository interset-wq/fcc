"""Convert demical to fraction"""

digits = input('Enter a demical num to convert: ')
exponent = len(digits) - 1

n = float(digits)

numerator = int(n * 10**exponent)
denominator = 10**exponent

percent = n * 100

print('Demical: ', n)
print(f'Fraction: {numerator}/{denominator}')
print(f'Percent: {percent}%')