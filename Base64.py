def encode(cadena):

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Convertir la cadena a una lista de valores ASCII
    ascii_values = [ord(char) for char in cadena]

    # Inicializar la cadena codificada
    encoded_string = ""

    # Iterar sobre la lista de valores ASCII
    i = 0
    while i < len(ascii_values):
        # Obtener los tres valores ASCII
        chunk = ascii_values[i:i+3]
        i += 3

        # Convertir los valores ASCII a binario
        binary_chunk = ''.join(format(value, '08b') for value in chunk)

        # Añadir ceros al final si es necesario
        if len(chunk) < 3:
            binary_chunk += '0' * (3 - len(chunk)) * 8

        # Dividir el binario en grupos de 6 bits y obtener los índices correspondientes en la tabla Base64
        indices = [int(binary_chunk[j:j+6], 2) for j in range(0, len(binary_chunk), 6)]

        # Construir la cadena codificada usando los índices
        encoded_string += ''.join(base64_chars[index] for index in indices)

    return encoded_string

def decode(cadena):
    # Tabla de decodificación Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Invertir la tabla Base64 para facilitar la decodificación
    base64_dict = {char: i for i, char in enumerate(base64_chars)}

    # Eliminar los caracteres de relleno al final de la cadena
    cadena = cadena.rstrip('=')

    # Inicializar la cadena decodificada
    decoded_string = ""

    # Iterar sobre la cadena codificada en grupos de 4 caracteres
    i = 0
    while i < len(cadena):
        # Obtener los cuatro caracteres
        chunk = cadena[i:i+4]
        i += 4

        # Convertir los caracteres a sus índices en la tabla Base64
        indices = [base64_dict[char] for char in chunk]

        # Convertir los índices a binario y combinarlos en una cadena
        binary_chunk = ''.join(format(index, '06b') for index in indices)

        # Dividir el binario en grupos de 8 bits y convertirlos de nuevo a caracteres ASCII
        for j in range(0, len(binary_chunk), 8):
            byte = binary_chunk[j:j+8]
            if byte != '00000000':
                decoded_string += chr(int(byte, 2))

    return decoded_string

print('Escribe un string y pulsa ENTER')
cadena = input()

print('Codificador Base64')
print('0. Codificar')
print('1. Decodificar')
print('Escribe una opción (0/1) y pulsa ENTER')
option = int(input())

if option == 0:
    print(encode(cadena))
elif option == 1:
    print(decode(cadena))
else:
    print("ERROR: Opción distinta de 0 ó 1")