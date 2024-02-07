'''
002 Static Methods (class methods / decoradores)
- los metodos estáticos pueden ser accesibles sin instanciar un objeto, solo llamando la clase
'''
class Student:

    def __init__(self, id, full_name):
        self.id = id
        self.full_name = full_name

    def speak (self):
        return 'Speaking'

    def walk (self):
        return 'Walking'

    @staticmethod
    def run (self):
        return 'Running'

    @classmethod
    def sleep (cls, starting, ending):
        return f'Sleeping from {starting} to {ending}'
        

#ulises = Student(100, "Ulises Arteaga")
#print(ulises.speak())

#print(f'sin instanciar un objeto: {Student.run()}')

print(Student.sleep("10:00 PM", "6:00 AM"))