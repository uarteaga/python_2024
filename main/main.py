def suma_cinco(numero):
    try:
        if numero:
            return int(numero) + 5
        else:
            return print('Por favor ingresa un número: ')
    except ValueError as error:
        return error


print (suma_cinco(1))

#assert(suma_cinco(1)) == 6
#assert(suma_cinco(1)) == 1