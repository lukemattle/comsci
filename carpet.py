#Write a pseudocode algorithm for a program which calculates the cost of carpeting a room. 
#The carpet is supplied in a roll 4m wide. The cost of the carpet is £10 per square metre. 
#The program should ask the user to enter the longest dimension (length) and shortest dimension (width) of the room, 
#then calculate and display the length and width and cost of carpet that will be supplied. 
#You can assume that the width of the room is not more than 4m. If a width of more than 4m is entered, 
#display an error message and quit the program. 
#The length could be more or less than 4m. 

length = float(input('Enter the longest dimension\n'))
width = float(input('Enter the shortest dimension\n'))

if width <= 4:
    area = length/4
    cost = area*160
    print('Cost of carpet: £' + str(cost))
else:
    print('Width must be less than 4')
