# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


nombre = input('Captura tu nombre: ')
sexo = input('Captura tu sexo (H/M): ')

if sexo == 'M' and nombre[0] < 'M':
    print('Perteneces al grupo A')
elif sexo == 'H' and nombre[0] > 'M':
    print('Perteneces al grupo A')
else:
    print('Perteneces al grupo B')
