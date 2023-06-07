#a fizzbuzz game
#if a number is divisible by 3 print fizz
#if a number is divisible by 5 print buzz
#if a number is divisible by both 3 and 5 print fizzbuzz

number = 0
for number in range (0,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

