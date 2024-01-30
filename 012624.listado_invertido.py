'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list.reverse() 

for number in my_list:
   print(number, end=", ")

#for number in range(1,11,-1):

 #   print(number, end=", ")