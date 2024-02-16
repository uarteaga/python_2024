import re

#special sequences
mensajes = ["A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.", "Returns a Match object if there is a match anywhere in the string", "Dictionaries are used to store data values in key:value pairs."]

'''
#patron = "\AA"
patron = "\AReturns"

resultado = re.findall(patron, mensaje2)
print(resultado)

if resultado:
    print('found!')

else:
    print("NOT found!")

'''

#patron = r"\bval"
#patron = "\s"
patron = "\S"

for index, mensaje in enumerate(mensajes):
    resultado = re.findall(patron, mensaje)
    if resultado:
        print(f'Patrón {patron}, encontrado en el indice {index}, : mensaje {mensaje}')



'''
    #print(mensajes)

    if resultado:
        print(resultado)
'''


