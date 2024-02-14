def generator():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

generator_example = generator()
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))

'''
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))

for iterador in generator():
    print(iterador)
'''