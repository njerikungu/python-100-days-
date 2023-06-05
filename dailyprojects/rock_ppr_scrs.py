#a rock paper scissors with the computer

import random

choice = input("What do you choose? Input 0 for Rock, 1 for Scissors and 2 for  Paper\n")
print(" 0 is for Rock\n 1 is for Scissors\n 2 is for Paper") 
my_choice = int(choice)

choices = ["Rock", "Scissors", "Paper"]
number_of_choices = len(choices)
comps_choice = random.randint(0, number_of_choices - 1)
comps_final_choice = choices[comps_choice]
print(f"Computer selected {comps_final_choice}!")

if my_choice == comps_choice:
    print("You draw!")
elif my_choice < comps_choice:
    print("You win!")
elif my_choice > comps_choice:
    print("You lose!")
else:
    print("Invalid choice")



