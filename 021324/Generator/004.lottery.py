import random

def lottery():

    for iterador in range(4):

        yield random.randint(1, 10)
    
    yield random.randint(100, 110)

for value in lottery():
    print(f'The winner is... {value}')


