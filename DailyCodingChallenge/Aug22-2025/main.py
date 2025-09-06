def decode(message: str, shift: int):
    import string
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    decode_str = ''
    for char in message:
        if char.isupper():
            index = uppercase.index(char)
            new_index = (index - shift) % 26
            if new_index < 0:
                new_index += 26
            decode_str += uppercase[new_index]
        elif char.islower():
            index = lowercase.index(char)
            new_index = (index - shift) % 26
            if new_index < 0:
                new_index += 26
            decode_str += lowercase[new_index]
        else: 
            decode_str += char
    return decode_str

if __name__ == '__main__':
    print(decode("Xlmw mw e wigvix qiwweki.", 4))
    print(decode("Byffi Qilfx!", 20))
    print(decode("Zqd xnt njzx?", -1))
    print(decode("oannLxmnLjvy", 9))