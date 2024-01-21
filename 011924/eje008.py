'''
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
num1 = int(input("Captura el primer número: "))
num2 = int(input("Captura el segundo número: "))

cociente = num1 / num2
resto = num1 % num2

print("----------")

print(f'Su primer número es {num1}, su segundo número es {num2}')

print(f'el cociente de estos números es {cociente}, el resto es {resto}')

