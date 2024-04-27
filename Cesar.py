def descifrar_cesar(cadena):
    for rotacion in range(26):
        texto_descifrado = rotacion_cesar(cadena, rotacion)
        print(f'Rotación {rotacion}: {texto_descifrado}')

def rotacion_cesar(cadena, rotacion):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''
    for letra in cadena:
        if letra.upper() in alfabeto:
            indice = alfabeto.find(letra.upper())
            indice_desplazado = (indice - rotacion) % len(alfabeto)
            if letra.isupper():
                resultado += alfabeto[indice_desplazado]
            else:
                resultado += alfabeto[indice_desplazado].lower()
        else:
            resultado += letra
    return resultado

print('Escribe un string y pulsa ENTER')
cadena = input()

print('Codificador Cesar')
print('0. Codificar')
print('1. Decodificar')
print('Escribe una opción (0/1) y pulsa ENTER')
option = int(input())

if option==0:
    print('Escribe el numero de rotacion N')
    rot = int(input()) * -1
    print(rotacion_cesar(cadena, rot))
elif option==1:
    descifrar_cesar(cadena)
else:
    print("ERROR: Opción distinta de 0 ó 1")