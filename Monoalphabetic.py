def encrypt(plain_text, key):
    cipher_text = ""
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(' ', '')
    key = key.lower()
    i = 0
    for ch in plain_text:
        cipher_text += chr((((ord(ch)-97)+(ord(key[i] - 97))) % 26) + 97)
        i += 1
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    cipher_text = cipher_text.lower()
    key = key.lower()
    i = 0
    for ch in cipher_text:
        plain_text += chr((((ord(ch) - 97) - (ord(key[i] - 97))) % 26) + 97)
        i += 1
    return plain_text
