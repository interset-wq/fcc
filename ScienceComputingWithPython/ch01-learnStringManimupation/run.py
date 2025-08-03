from encrypted import decrypt

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'
print(f'\n加密后的文本: {text}')
print(f'密钥: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\n解密后的文本: {decryption}\n')