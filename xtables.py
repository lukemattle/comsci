#Write a pseudocode algorithm to allow the user to input two integers highestNumber and multiplier. 
#The program should output the results of multiplying integers 2, 3... highestNumber by multiplier. 
#For example if the user enters 100 for highestNumber and 7 for multiplier the program should output the numbers 14, 21 ... 98.

highestNumber = int(input('Enter the max number\n'))
multiplier = int(input('Enter the multiplier\n'))
temp = multiplier

if temp > highestNumber:
    print('Max number cannot be lower than multiplier')
    exit(0)
else:
    print(temp)

while temp < (highestNumber - multiplier):
    temp = temp + multiplier
    print(temp)