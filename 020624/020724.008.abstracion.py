'''
008 Abstracción

'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        pass

class Car(Vehicle):

    def drive(self):
        return f'Conduciendo un {self.brand} del modelo {self.model}'


class Truck(Vehicle):

    def drive(self):
        return f'Conduciendo en el campo, mi {self.brand} del modelo {self.model}'

class Bike(Vehicle):
    
    def drive(self):
        return f'Conduciendo mi moto {self.brand} del modelo {self.model} en la pista'


car_one = Car('VW', 'Jetta')
print(car_one.drive)
print(car_one.drive())

truck_one = Truck('Ford', 'Lobo')
print(truck_one.drive)
print(truck_one.drive())

bike_one = Bike('Ducatti', '8480')
print(bike_one.drive)
print(bike_one.drive())

