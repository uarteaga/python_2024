'''
003 lambda
- Son funciones anónimas
- puede tomar cualquier número de argumentos, pero solo tiene una expresión
- El resultado se guarda en una varaible, la función lambda puede recibir 1, 2 o cualquier número de parámetros (argumentos)
'''
def suma(numero):
    resultado = numero + 1
    return resultado

#print(suma(2))

resultado =lambda numero: numero+1
#print(resultado(1))

resultado_dos = lambda numero_uno, numero_dos: numero_uno + numero_dos + 1

print(resultado_dos(2,2))