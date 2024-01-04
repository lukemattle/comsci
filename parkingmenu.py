#Write pseudocode for a program which displays a menu with 5 options, and for the first four options, calls the relevant subroutine.  
#	Option 1: 	Set all spaces in the car park to “empty”
#	Option 2:	Park a car. This option asks the user to enter the registration number of a car and the grid reference
 #               where it has been parked.  The program checks that this is an empty space, and if it is, 
  #              puts the registration number in the appropriate element of the array.
   #             If it is not, it asks the user to enter the grid reference.
#	Option 3:	Remove a car. This option asks the user to enter the registration number, searches the grid for the number 
 #               and then resets it to “empty”.
#	Option 4:	Display the car park grid
#	Option 5: 	Quit

cont = True
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

while cont == True:
    choice = input("""1. Reset all spaces in the car park to 'empty'\n
    2. Park a car\n
    3. Remove a car\n
    4. Display the car park grid\n
    5. Quit\n""")

def opt1():
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

def opt2():
    x = int(input('Please enter the x coordinate of the desired place\n'))
    y = int(input('Please enter the y coordinate of the desired place\n'))

    if x < 6 and y < 10:
        x -= 1
        y -= 1

        if space[x][y] == 'empty':
            reg = input('Please enter the registration of your car\n')
            space[x][y] = reg
            draw_grid()
        else:
            print('Space not empty. Try again\n')
    else:
        print('x must be between 1-6 and y must be between 1-10. Try again\n')

def opt3():
    reg = input('Please enter the registration of your car.')
    pos = 0
    for i in range(10):
        if space[pos] == reg:
        pos += 1


def opt4():
    for i in range(10):
        print(space[i])