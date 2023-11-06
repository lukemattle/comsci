#A company runs a private car park near an airport. The car park has 10 rows numbered 1-10 and each row has spaces (referred to as columns) 
#numbered 1-6 for 6 cars. Customers leave their cars with keys at the car park office, 
#and a driver parks it in a free space and then records where it is parked. 
#The space is referenced by its grid coordinates row and column. E.g. a car parked in the 3rd row, 5th space would have the grid reference [3,5]. 
#The driver enters the car registration into the computer. 
#A car with registration AV61 HFU parked at grid reference [3,5] would assign “AV61 HFU” to park[3,5]. 
#Empty spaces are denoted, for example, by park[3,5] = “empty”
#Write pseudocode for a program which :
#Initialises the grid, with each element holding “empty”.
#“Parks a car”. This option asks the user to enter the registration number of a car and the grid reference (row and column number) 
#where it has been parked.  
#Validates the user entry row between 1 and 10, column between 1 and 6 and asks user to re-enter until entry is valid.
#Checks that this is an empty space, and if it is, puts the registration number in the appropriate element of the array. 
#If it is not, displays  “That space is taken” and asks the user to re-enter the grid reference.
#Displays the grid.

parked = False
space = [['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty']]

def draw_grid():
    pos = 0
    for i in range(10):
        print(space[pos])
        pos += 1

draw_grid()

while parked == False:
    x = int(input('Please enter the x coordinate of the desired place\n'))
    y = int(input('Please enter the y coordinate of the desired place\n'))

    if x < 6 and y < 10:
        x -= 1
        y -= 1

        if space[x][y] == 'empty':
            reg = input('Please enter the registration of your car\n')
            space[x][y] = reg
            draw_grid()
            parked = True
        else:
            print('Space not empty. Try again\n')
    else:
        print('x must be between 1-6 and y must be between 1-10. Try again\n')