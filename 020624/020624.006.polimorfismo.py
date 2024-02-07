'''
'''

class Human:
    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year
    def walk (self):
        return 'Walking'

class Man(Human):
    def __init__(self, name,  born_year, last_name):
        super().__init__(name, born_year)
        self.last_name = last_name


ibra = Man('Marco', 1945, 'Corleone')
print (ibra.name('Ibra'))
print (ibra.walk())