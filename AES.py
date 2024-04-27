from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def aes_cbc_decrypt(ciphertext_hex, key, iv):
    ciphertext = bytes.fromhex(ciphertext_hex)

    backend = default_backend()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    decryptor = cipher.decryptor()

    return decryptor.update(ciphertext) + decryptor.finalize()


key = b'SeguridadInforma'
iv = b'SeguridadInforma'

ciphertext_hex = 'f6994c079e2984d406e90a908076ed69'

plaintext = aes_cbc_decrypt(ciphertext_hex, key, iv)
print("Texto decodificado:", plaintext)