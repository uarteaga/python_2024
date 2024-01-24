'''
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

'''
monto = float(input("Capture el monto a invertido: "))
interes = 0.04

monto1 = monto*(1+interes)
monto2 = monto1*(1+interes)
monto3 = monto2*(1+interes)

print(f'Su capital obtenido tras 1 año será de ${round(monto1,2)}')
print(f'Tras 2 años será de ${round(monto2,2)}')
print(f'Tras 3 años será de ${round(monto3,2)}')