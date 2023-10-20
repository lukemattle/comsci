#Write pseudocode for a program which asks the user to enter the total bill for a restaurant
#meal, and the total number of people who had a meal. The program should add 10% to the
#bill as a tip, and then calculate and display to the nearest penny what each person owes, assuming the bill is evenly split.

price = float(input('Please enter the total bill.\n'))
people = int(input('Please enter the number of people.\n'))

tip = price / 10
price += tip
pricepp = price / people
pricepp = round(pricepp, 2)

print('Total bill per person: £' + str(pricepp))