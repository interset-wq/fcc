import re
# 用于生成比random更安全的伪随机数
import secrets
import string


def generate_password(length: int=16, 
                      nums: int=1, 
                      special_chars: int=1, 
                      uppercase: int=1, 
                      lowercase: int=1) -> str:
    """generate a safe password randomly
    传入的其他数字表示至少包含，例如nums=1表示至少有一个数字
    """

    # Define the possible characters for the password
    letters = string.ascii_letters # 英文大小写字母
    digits = string.digits # 阿拉伯数字
    symbols = string.punctuation # 特殊符号
    # print(letters, digits, symbols, sep='\n\n')

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'), # 数字
            (special_chars, fr'[{symbols}]'), # 特殊符号
            (uppercase, r'[A-Z]'), # 大写字母
            (lowercase, r'[a-z]') # 小写字母
        ]

        # Check constraints        
        if all(
            # 这是一个列表推导式
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)