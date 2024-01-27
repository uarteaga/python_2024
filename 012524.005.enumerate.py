'''
005 enumerate
'''
'''
course = 'learning_python'
for index, character in enumerate (course):
    #print(index, character)
    if character == 'i':
        print(index, character)
        print(f'index of {character} in potition {index}')
'''
my_courses = ['Python', 'Scrum', 'Docker', 'NGINX']

for index course in enumerate(my_courses):
    print(index, course)
    find = input('find: ')
    if find == index:
        print (f'Course {course} found in index {index}')