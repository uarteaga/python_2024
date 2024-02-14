import random

numbers_list = [1,2,3,4,5,6,7,8,9,0]
letters_list_lowercase = ['a','b','c','d','e']
letters_list_uppercase = ['A', 'B', 'C', 'D', 'E']
characters_list = ['*', '#', '&', '?', '@']

user_numbers = int(input('How many numbers? '))
#user_letters = int(input('How many letters? '))

#print(user_numbers)
#print(user_letters)

password_number = ''
for iteration in range(0, user_numbers):
    #print(iteration)
    random_int = random.choice(numbers_list)
    #print(random_int)
    password_number += str(random_int)

print(password_number)

user_letters_lower = int(input('How many lowercase letters? '))

password_letter = ''

for iteration in range(0, user_letters_lower):
    #print(iteration)
    random_letter = random.choice(letters_list_lowercase)
    #print(random_int)
    password_letter += str(random_letter)

print(password_letter)


user_letters_upper = int(input('How many uppercase letters? '))

password_letter_upper = ''

for iteration in range(0, user_letters_upper):
    #print(iteration)
    random_letter_upper = random.choice(letters_list_uppercase)
    #print(random_int)
    password_letter_upper += str(random_letter_upper)

print(password_letter_upper)

user_characters = int(input('How many special characters? '))

password_characters = ''

for iteration in range(0, user_characters):
    #print(iteration)
    random_character = random.choice(characters_list)
    #print(random_int)
    password_characters += str(random_character)

print(password_characters)

#Pendiente arreglar la concatenación y suffle
concatenar = password_number + password_letter + password_letter_upper + password_characters
random.shuffle(concatenar)


print(concatenar)