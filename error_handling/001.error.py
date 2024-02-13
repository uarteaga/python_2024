

while True:
    try:

        age = int(input('age? '))
        10/age
        print(age)

    except TypeError:
        print('Error 001: Ingresa un número')    
    except ValueError:
        print('Error 002: seguramente ingresaste una letra, ingresa un número')
    except ZeroDivisionError:
        print('Error 003: Se capturó un 0, este no es un número válido')
    
    else:
        print('Datos guardados correctamente')
        break