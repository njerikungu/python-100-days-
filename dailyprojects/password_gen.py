#password generator
#generates random password

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

numletters = int(input("How many letters do you want in your password?\n"))
numnumbers = int(input("How many numbers do you want in your password?\n"))
numsymbols = int(input("How many symbols do you want in your password?\n"))

password_list = []
for char in range (0, numletters):
    selected_char = random.choice(letters)
    password_list += selected_char 
print(password_list)

for char in range (0, numnumbers):
    selected_char = random.choice(numbers)
    password_list += selected_char
print(password_list)

for char in range (0, numsymbols):
    selected_char = random.choice(symbols)
    password_list += selected_char
print(password_list)

#to use the random.shuffle, we first change the string to a list
random.shuffle(password_list)
print (password_list)

#changing this password back to a string

password = ""
for char in password_list:
    password += char
    
print(password)
