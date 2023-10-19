import math

walls = int(input('How many walls do you want to paint? '))
unp = int(input('How unpaintable areas do you have? '))
coats = int(input('How many coats do you want to paint? '))
total = 0

while walls > 0:
    width = float(input('What is the width of wall' + str(walls) + ' in meters? '))
    length = float(input('What is the length of wall' + str(walls) + ' in meters? '))
    temp = width*length
    total += temp
    walls -= 1

while unp > 0:
    width = float(input('What is the width of unpaintable area' + str(walls) + ' in meters? '))
    length = float(input('What is the length of unpaintable area' + str(walls) + ' in meters? '))
    temp = width*length
    total -= temp
    unp -= 1

total *= coats
total /= 11
print('You need ' + str(math.ceil(total)) + ' cans of paint')