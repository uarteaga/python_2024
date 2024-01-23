'''
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''
horas_trabajadas = input('Captura horas trabajadas:')
coste_hora = input('Captura coste de horas:')
paga = int(horas_trabajadas) * int(coste_hora)

print(f'Su paga correspondiente es ${paga}.00')