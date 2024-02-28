# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar


numero = int(input('ingresa un número: '))
resultado = numero % 2

if resultado == 0:
    print(f'el número {numero} es par')
else:
    print(f'el número {numero} es impar')
