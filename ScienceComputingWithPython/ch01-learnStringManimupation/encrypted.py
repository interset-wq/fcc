"""维吉尼亚密码Vigenère cipher

加密基础：
    以 26 个英文字母(a-z)为基础进行替换加密
    使用一个自定义密钥(key)来确定每个字母的偏移量
    非字母字符(如空格、数字等)不进行加密，直接保留

加密步骤：
    将明文和密钥都转换为小写字母处理
    密钥按顺序循环使用(通过key_index % len(key)实现)
    每个密钥字符对应一个偏移量(该字符在字母表中的位置, a=0, b=1, ..., z=25)
    明文中的每个字母按以下规则转换：
        加密后字母位置 = (明文字母位置 + 密钥字符偏移量) % 26
    最终将计算出的新位置对应的字母作为加密结果
"""


def vigenere(message: str, key: str, direction: int = 1) -> str:
    """对一个字符串message进行加密或解密
    
    Args:

        key 用于解密
        direction 
    """

    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # 非字母字符不需要加密
        if not char.isalpha():
            final_message += char
        else:        
            # 从密钥key中获取字符key_char
            # key_index % len(key) 用来处理 key_index > len(key)的情形
            key_char = key[key_index % len(key)]
            key_index += 1

            # 获取密钥字符key_char的下标作为偏移值offset
            offset = alphabet.index(key_char)
            # 获取字符串message中某个字符的下标
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message


def encrypt(message: str, key: str) -> str:
    """encrypt a message"""
    return vigenere(message, key)
    

def decrypt(message: str, key: str) -> str:
    return vigenere(message, key, -1)


if __name__ == '__main__':
    text = 'mrttaqrhknsw ih puggrur'
    custom_key = 'happycoding'
    print(f'\nEncrypted text: {text}')
    print(f'Key: {custom_key}')
    decryption = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decryption}\n')