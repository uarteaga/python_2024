'''
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

'''
print("------------")
precio_normal = float(3.45)
precio_viejo = float(precio_normal*.6)

ventas = int(input('Capture el número de barras vendidas que no son del día: '))

print("------------")
print(f'El precio normal de una barra del día es de: {precio_normal}€')
print(f'Una barra que no es del día tiene un descuento del 60%, por lo que su precio es de: {precio_viejo}€')

print("------------")
print(f'Por lo tanto, el precio a pagar por la ventas será de: {round(ventas*precio_viejo,2)}€')
print("------------")