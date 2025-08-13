import math

num = 12

max_factor = 1

end = math.floor(math.sqrt(num)) + 1

for i in range(1, end):
    if num % i**2 == 0:
        max_factor = i

remaining_under_squire = int(num / max_factor**2)

print('num: ', num)
print(f'squire rooted num: {max_factor}')
print(f'squire factor: {max_factor**2}')
print(f'remaining int: {remaining_under_squire}')
print(f'this is {max_factor}*sqrt({remaining_under_squire})')