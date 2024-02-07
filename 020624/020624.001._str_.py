'''
__str__ = permite representar el objeto con un string
'''

class Car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    def __str__ (self):
        return f'This is a {self.brand} {self.model} color {self.color}'

#instance
jetta = Car("VW", "Jetta", "Blanco")

print(jetta)

ibiza = Car("Seat", "Ibiza", "Gris")

print(ibiza)