'''
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

'''
monto = float(input("Capture el monto a invertir: "))
interes = int(input("Capture el interés anual(%): "))
anios = int(input("Capture el número de años: "))

interes = (interes / 100)

print(f'Su capital obtenido tras su inversión será de ${round(monto*interes*anios,2)}')
