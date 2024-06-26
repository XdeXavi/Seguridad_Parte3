from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def aes_cbc_encrypt(plaintext, key, iv):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext.hex()


def aes_cbc_decrypt(ciphertext_hex, key, iv):
    ciphertext = bytes.fromhex(ciphertext_hex)

    backend = default_backend()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    decryptor = cipher.decryptor()

    return decryptor.update(ciphertext) + decryptor.finalize()


key = b"SeguridadInforma"
iv = b"SeguridadInforma"

plaintext = b"Hello World"
ciphertext_hex = aes_cbc_encrypt(plaintext, key, iv)
print("Texto cifrado en AES CBC de Hello World:", ciphertext_hex)

ciphertext = "f6994c079e2984d406e90a908076ed69"

decryptedtext = aes_cbc_decrypt(ciphertext, key, iv)
print("Texto descifrado:", decryptedtext.decode())
