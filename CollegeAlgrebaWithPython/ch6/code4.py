import math
import sympy

num = 12

end = math.floor(math.sqrt(num)) + 1
max_factor = 1
other_factor = 1
squire_root = 1

for i in range(1, end):
    if num % i**2 == 0:
        max_factor = i**2

other_factor = int(num / max_factor)
squire_root = int(math.sqrt(max_factor))

output = squire_root * sympy.sqrt(other_factor)
print(output)