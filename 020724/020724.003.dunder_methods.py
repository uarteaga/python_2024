'''
003 Dunder Methodes / magic methodes
- Se caracterizan por inicar con doble guión bajo en cada método
- Un ejemplo es __init__ que nos ayuda a inicializar los atributos de un método.
- la mayoria o casi todos los magic methodes se pueden modificar
'''

class Laptop:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f"Hello, I'm a {self.brand} model {self.model} color {self.color}, this is cool, right?"

laptop_one = Laptop('Mac', 'MacBook Pro', 'silver')
print(laptop_one.__str__())
print('-------')
print(str(laptop_one))