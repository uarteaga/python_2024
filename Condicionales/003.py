# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num_uno = int(input('intresa un número:'))
num_dos = int(input('intresa un número:'))

if num_dos == 0:
    print('El segundo número no puede ser 0')
else:
    division = num_uno/num_dos
    print(division)