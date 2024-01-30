'''
001. functions
bloques de código que se pueden reutilizar y llamar
pueden o no recibir parámetros (argumentos)
'''
'''
def say_hello():
    print("hello")

#llamando la función
say_hello()

def say_hello_user(user_name):
    print(f'Hello {user_name}')

say_hello_user("Ulises")
say_hello_user("Maggie")
say_hello_user("Paulina")
'''

def wellcome_user(user_name):
    return f"Hello {user_name}"
    
print(wellcome_user("Ulises"))