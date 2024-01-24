'''
001. input
la función input me permite interactuar con el usuario y solicitar datos para crear una variable
'''
#user_name = input("what's your name")
#print(f'hello {user_name}')

#user_phone = input("Phone number: ")
#print ('+52'+ user_phone)
#print (type (user_phone))

costo_hora = 200
horas_trabajadas = input('Horas trabajadas')
resultado = costo_hora * int(horas_trabajadas)
print(f'salario: ${resultado}.00')