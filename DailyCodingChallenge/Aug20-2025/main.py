def squares_with_three(n: int) -> int:
    counter = 0
    for i in range(n+1):
        if '3' in str(i**2):
            counter += 1
    return counter

if __name__ == '__main__':
    print(squares_with_three(1)) # should return 0.
    print(squares_with_three(10)) # should return 1.
    print(squares_with_three(100)) # should return 19.
    print(squares_with_three(1000)) # should return 326.
    print(squares_with_three(10000)) # should return 4531.