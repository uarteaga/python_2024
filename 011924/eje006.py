'''
Ejercicio 6
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
suma =n(n+1)/2
'''

numero = int(input("Captura número entero: "))

numero = abs(numero)

print('valor absoluto es:', numero)

print('resultado de operación es: ')
n = numero*(numero+1)/2
print(n)
