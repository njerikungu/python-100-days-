#Build a ip calculator
#Below is an example of how it works
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = input("What is the total bill?\n$")
tip = input("What percentage tip would you like to give?\n$")
pple = input("What is the number of people sharing the meal?\n")
actual_tip = (float(int(tip)/100) * int(bill))
print(actual_tip)
actual_bill = (float(int(bill) +float(actual_tip)) / int(pple))
print(actual_bill)
print(f"Each person's bill is {round(actual_bill)}!")



