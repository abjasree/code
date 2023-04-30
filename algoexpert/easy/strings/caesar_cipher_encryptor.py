def caesarCipherEncryptor(string, key):
    # Write your code here.
    new_string = []
    key = key % 26
    for i in string:
        code = ord(i) + key
        new_string.append(get_new_letter(code))
    return "".join(new_string)


def get_new_letter(code):
    if code <= 122:
        return chr(code)
    else:
        return chr(96 + (code % 122))


def caesarCipherEncryptor(string, key):
    # Write your code here.
    alph = list("abcdefghijklmnopqrstuvwxyz")
    new_string = []
    key = key % 26
    for i in string:
        code = alph.index(i) + key
        new_string.append(get_new_letter(code, alph))
    return "".join(new_string)


def get_new_letter(code, alph):
    return alph[code % 26]
