'''
003 sets
- Los sets se forman usando llaves '{ }'
- Los sets no son indexables
- No permite duplicados
- Permite Int, Str, Boolean, 
'''

my_set = {1,2,3,4,5, 1}
#print(type(my_set))
my_other_set = {5, 6, 7, 8, 9, 'Set', False, 6.50}
print(my_set)
print(my_other_set)

print(my_set.difference(my_other_set))
#print(my_other_set.difference(my_set))

my_other_set.discard(7)
print(my_other_set)