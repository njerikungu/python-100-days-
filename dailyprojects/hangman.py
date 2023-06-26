import random
import hangman_art
from hangman_words import word_list

from hangman_art import logo, stages
print(logo)

chosen_word = random.choice(word_list)
#print(f"The chosen word is {chosen_word}")

word_len = len(chosen_word)
lives = 6
end_of_game = False


display = []
for _ in range(word_len):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already printed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
            
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word.\n You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    if "_" not in display:
        end_of_game = True
        print("You win!")
                
    print(stages[lives])
