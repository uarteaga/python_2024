import re

mensaje = "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern."

#palabra = "sequence"
#resultado = re.search(palabra, mensaje)

'''
if resultado:
    print('found!')

else:
    print('NOT found!')
'''

#findall
#metacharts []

#patron = "[a-c]"

#resultado = re.findall(patron, mensaje)
#print(resultado)

# \d

'''
patron = "\d"

resultado = re.findall(patron, mensaje)
print(resultado)
print(type(resultado))

'''
#patron = "t..t"
#patron = "s....h"
patron = "f."
resultado = re.findall(patron, mensaje)
print(resultado)