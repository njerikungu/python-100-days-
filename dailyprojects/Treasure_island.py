print ("Welcome to Treasure Island!")

step1 = input("You're at a cross road. \nWhere do you wish to go, Left or Right?\n")

if step1 == "Right":
    print("Fell into a hole!\nGame Over!")
else:
    step2 = input("Do you want to Swim or Wait?\n")
    if step2 == "Swim":
        print("Attacked by trout!\nGame Over!")
    else:
        step3 = input("Which door do you want to enter, Red, Blue or Yellow?\n")
        if step3 == "Red":
            print("Burned by fire!\nGame Over!")
        elif step3 == "Blue":
            print("Eaten by beasts!\nGame Over!")
        elif step3 == "Yellow":
            print("You win!")
        else:
            print("Game over!")



