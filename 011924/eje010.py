'''
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

'''
payasos = int(input('Capture el número de payasos para el último pedido: '))
munecas = int(input('Capture el número de muñecas para el último pedido: '))

print("--------------")

peso_payasos = payasos*112
peso_munecas = munecas*75

peso_paquete = (peso_payasos + peso_munecas) / 1000 #peso en kg

print(f'El peso de su paquete es de {round(peso_paquete,2)}kg')