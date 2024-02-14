import random

random_number_float = random.random()
print(random_number_float)
print(round(random_number_float,5))

random_number_int = random.randint(1,20)
print(random_number_int)

friends = ['Hugo', 'Maria', 'Ulises', 'Maggie']
random_choice = random.choice(friends)

print(random_choice)