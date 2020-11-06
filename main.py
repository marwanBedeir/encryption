import Caesar as ca, Monoalphabetic as mo, Play_fair as pf
if __name__ == '__main__':
    key = "occurrence"
    plain_text = "I will come next section"
    cipher_text = "pfiztzeort"

    # cipher_text = ca.encrypt(plain_text, key)
    # cipher_text = mo.encrypt(plain_text, key)
    # cipher_text = pf.encrypt(plain_text, key)
    #
    # plain_text = ca.decrypt(cipher_text, key)
    # plain_text = mo.decrypt(cipher_text, key)
    plain_text = pf.decrypt(cipher_text, key)

    print("Plaintext : ", plain_text)
    print("The key : ", key)
    print("Cipher text : ", cipher_text)
