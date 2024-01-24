'''
002 tuplas
- las tuplas se usan con '()'
- las tuplas pérmiten, int, string, boolean, permite cualquier tipo de valor
- las tuplas permiten duplicados

'''

my_tuple = (1,2,3,4,5,6,'7',False, 1)
#print(my_tuple[0])
#my_tuple[2] = 30

my_new_tuple = my_tuple[1:3:1]
print(my_new_tuple)

#print(5 in my_new_tuple)

print(my_tuple.count(2))
print(my_tuple.count(1))