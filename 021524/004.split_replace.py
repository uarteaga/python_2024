import re

mensaje = "Create and fund dictionary"

patron = '\s'
replace = '-'

vecescambio = 2

#resultado = re.sub(patron, replace, mensaje, vecescambio)
resultado = re.sub(patron, replace, mensaje)

print(resultado)