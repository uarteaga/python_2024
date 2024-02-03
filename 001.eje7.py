'''
007. 
Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados
'''

def obtener_cuadrados():

 # Creamos listas vacías
 lst = []
 sqr_lst = [] 

 # Definimos tamaño de lista
 n = int(input("Define el tamaño de la lista : "))
 
 # Iteramos hasta el rango de la lista
 for i in range(0, n):
    ele = int(input())

    # agregamos numero a la lista
    lst.append(ele)  
    
 #Mostramos lista
 print(lst)

 # Recorremos la lista original
 for num in lst:

  # Calculamos el cuadrado del número actual
  sqr = num ** 2

  # Agregamos el cuadrado a la lista de cuadrados
  sqr_lst.append(sqr)

 # Imprimimos la lista de cuadrados
 print(sqr_lst)

# Ejemplo de uso
cuadrados = obtener_cuadrados()

print(cuadrados)
