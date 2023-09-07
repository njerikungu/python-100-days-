alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        #or new_position = position - shift_amount
    
    for char in start_text:
        if char in alphabet:
         position = alphabet.index(char)
         new_position = position + shift_amount
         end_text += alphabet[new_position]
        else:
           end_text += char
    print(f"The {cipher_direction}d text is {end_text}.")

should_continue = True
while should_continue:
    text = input("Type your text: \n")
    shift = int(input("Type shift amount: \n"))
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    shift %= 26
    #if the user enters a number bigger than the number of 
    # letters in the alphabet the we do us up there.
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input ("Type 'yes' if you want to go again. Otherwise 'no'\n")
    if result == 'no':
       should_continue = False
       print("Goodbye.")
