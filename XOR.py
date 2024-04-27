def xor_encode_decode(mensaje, clave):
    encoded_bytes = bytearray()
    for i, m in enumerate(mensaje.encode('iso-8859-1')):
        k = clave.encode('iso-8859-1')[i % len(clave)]
        encoded_bytes.append(m ^ k)
    return encoded_bytes.decode('iso-8859-1')
def xor_cifrado(texto_plano, clave):
    texto_cifrado = ""
    for i in range(len(texto_plano)):
        # Aplicar XOR a cada carácter del texto plano con la clave
        caracter_cifrado = chr(ord(texto_plano[i]) ^ ord(clave[i % len(clave)]))
        texto_cifrado += caracter_cifrado
    return texto_cifrado

print('Escribe un cadena y una clave y pulsa ENTER')
text, key = input().strip().split()


print('Codificador XOR')
print('0. Codificar')
print('1. Decodificar')
print('Escribe una opción (0/1) y pulsa ENTER')
option = int(input())

if option==0:
    print(xor_cifrado(text, key))
elif option==1:
    print(xor_encode_decode(text, key))
else:
    print("ERROR: Opción distinta de 0 ó 1")