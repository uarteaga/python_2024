'''
002 super()
- el metodo super() hace referencia a la clase padre
- Humano (padre) = super() para hacer herencia
'''

class Animal:
    def __init__(self, especie , edad):
        self.especie = especie
        self.edad = edad

class Perro(Animal):

    def __init__(self, especie, edad, nombre):
        #super().__init__(especie, edad)
        Animal.__init__(self, especie, edad)
        self.nombre = nombre
    
    def mueve(self):
        return super().mueve()

perro_uno = Perro('pitbull', '4', 'Iggy')

print(perro_uno.especie)
print(perro_uno.edad)
print(perro_uno.nombre)
print(perro_uno.mueve())

