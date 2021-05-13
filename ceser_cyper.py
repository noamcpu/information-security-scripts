alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    if k < 0 or k > 26:
        return False
    plaintext_ans = ""
    for i in (range(len(plaintext))):
        if plaintext[i] in alphabet:
            tmp = alphabet.find(plaintext[i])
            decrypt = alphabet[tmp + k]
            plaintext_ans += str(decrypt)
    return print(plaintext_ans)


encrypt("jkl", 2)
# do stuff and return ciphertext
