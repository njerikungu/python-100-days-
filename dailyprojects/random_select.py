#first import the module
import random

name_string = input("Give me everybody's names, separated by a comma.\n")
#use .split to add the comma in the list about to be created
names = name_string.split(",")

# to use the random selection,
# find the length of the list

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_to_pay = (names[random_choice])
print(f"Today's bill will be paid by {person_to_pay}!")



