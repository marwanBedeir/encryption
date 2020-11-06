def encrypt(plain_text, key):
    cipher_text = ""
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(' ', '')
    for ch in plain_text:
        cipher_text += chr((((ord(ch)-97) + int(key)) % 26) + 97)
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    cipher_text = cipher_text.lower()
    for ch in cipher_text:
        plain_text += chr((((ord(ch) - 97) - int(key)) % 26) + 97)
    return plain_text
