text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message: str, key: str, direction: int = 1) -> str:
    """encrypt/decrypt a message. use custom_key to encrypt. 
    get the char of the custom_key in order, 
    then get its index in alphabet as offset
    """

    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message


def encrypt(message: str, key: str) -> str:
    """encrypt a message"""
    return vigenere(message, key)
    

def decrypt(message: str, key: str) -> str:
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')