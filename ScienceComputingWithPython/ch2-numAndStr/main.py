def verify_card_number(card_number: str) -> bool:
    """通过卢恩算法判断卡号是否有效"""
    
    # 卡号的逆序
    card_number_reversed = card_number[::-1]

    """逆序序号是奇数的求和"""
    sum_of_odd_digits = 0
    # 逆序序号是奇数的不需要操作
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    """逆序序号是偶数的求和"""
    sum_of_even_digits = 0
    # 逆序序号是偶数的要乘以2，
    # 如果大于等于10，个位数字与十位数字相加；小于10，不操作
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    
    """经过前面操作之后得到的数字求和，如果能被10整除，则卡号有效"""
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main() -> None:
    """主函数"""

    card_number = '4111-1111-4555-1142'

    # 删除空格和连字符
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__ == '__main__':
    main()