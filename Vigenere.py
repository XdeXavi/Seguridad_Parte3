ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encode(plaintext, key):
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_shift = ALPHABET.index(key_char)
            cipher_index = (char_index + key_shift) % len(ALPHABET)
            ciphertext += ALPHABET[cipher_index]
        else:
            ciphertext += char
    return ciphertext


def vigenere_decode(ciphertext, key):
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_shift = ALPHABET.index(key_char)
            plain_index = (char_index - key_shift) % len(ALPHABET)
            plaintext += ALPHABET[plain_index]
        else:
            plaintext += char
    return plaintext

print('Escribe un cadena y una clave y pulsa ENTER')
text, key = input().strip().split()


print('Codificador Vigenere')
print('0. Codificar')
print('1. Decodificar')
print('Escribe una opción (0/1) y pulsa ENTER')
option = int(input())

if option==0:
    print(vigenere_encode(text, key))
elif option==1:
    print(vigenere_decode(text, key))
else:
    print("ERROR: Opción distinta de 0 ó 1")