from collections import OrderedDict


def encrypt(plain_text, key):
    cipher_text = ""
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(' ', '')
    pairs = []
    i = 0
    while i < len(plain_text):
        if plain_text[i] == plain_text[i+1]:
            plain_text = plain_text[:i+1] + add_char(plain_text[i]) + plain_text[i+1:]
            i = 0
        else:
            i += 2
        if i == len(plain_text) - 1:
            plain_text += add_char(plain_text[i])
    i = 0
    while i < len(plain_text):
        pairs.append((plain_text[i], plain_text[i+1]))
        i += 2

    mat = initialize_mat(key)
    for row in mat:
        print(row)

    for a, b in pairs:
        a_x, a_y = get_index(a, mat)
        b_x, b_y = get_index(b, mat)
        if a_x == b_x:
            cipher_text += mat[a_x][(a_y + 1) % 5] + mat[b_x][(b_y + 1) % 5]
        elif a_y == b_y:
            cipher_text += mat[(a_x + 1) % 5][a_y] + mat[(b_x + 1) % 5][b_y]
        else:
            cipher_text += mat[a_x][b_y] + mat[b_x][a_y]
    return cipher_text


def initialize_mat(key):
    key = key.lower()
    key = key.replace('j', 'i')
    key = list(OrderedDict.fromkeys(key))  # to remove duplication
    mat = [[0 for _ in range(5)] for _ in range(5)]
    alphabetic = "abcdefghiklmnopqrstuvwxyz"
    x = 0
    y = 0
    i = 0

    while i < len(key):
        mat[x][y] = key[i]
        i += 1
        y += 1
        if y == 5:
            y = 0
            x += 1
            if x == 5:
                break

    for ch in alphabetic:
        if ch not in key:
            mat[x][y] = ch
            y += 1
            if y == 5:
                y = 0
                x += 1
    return mat


def get_index(ch, mat):
    if ch == 'j':
        ch = 'i'
    return [(index, row.index(ch)) for index, row in enumerate(mat) if ch in row][0]


def add_char(ch):
    return 'x' if ch != 'x' else 'j'


def decrypt(cipher_text, key):
    plain_text = ""
    cipher_text = cipher_text.lower()
    mat = initialize_mat(key)
    for row in mat:
        print(row)
    i = 0
    while i < len(cipher_text)-1:
        a_x, a_y = get_index(cipher_text[i], mat)
        b_x, b_y = get_index(cipher_text[i+1], mat)
        i += 2
        if a_x == b_x:
            plain_text += mat[a_x][(a_y - 1) % 5] + mat[b_x][(b_y - 1) % 5]
        elif a_y == b_y:
            plain_text += mat[(a_x - 1) % 5][a_y] + mat[(b_x - 1) % 5][b_y]
        else:
            plain_text += mat[a_x][b_y] + mat[b_x][a_y]
    return plain_text
