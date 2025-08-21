def sum_of_squares(n: int) -> int:
    n = sum(i**2 for i in range(1, n+1))
    return n

if __name__ == '__main__':
    print(sum_of_squares(5))
    print(sum_of_squares(10))
    print(sum_of_squares(1000))