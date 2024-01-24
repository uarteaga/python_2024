'''
001 Dictionaries
Sirven para guardar multiples valres de datos
Para declarar un diccionario utilizamos las llaves "{ }"
Se compone de un 'key' y un 'value', siempre en pares
'''

car_dir = {
    'key': 'value',
    'marca': 'BMW',
    'modelo': 'Jetta',
    'anio': 2015,
    'version': 'sport',
    'direccion_fabrica': ['calle conocida', 'calle desconocida'],
    'vendido': True
}

print(car_dir)

print(car_dir['direccion_fabrica'][0])
print(car_dir['direccion_fabrica'][1])
print(car_dir['marca'])
print(car_dir['modelo'])
print(car_dir['anio'])

print(len(car_dir))


studet_dir = dict(nombre = 'Maggie', edad = 12, matricula = '12345FJS')

print(type(studet_dir))
print(studet_dir['edad'])

