#A grid game draws a 6 by 4 grid with each square denoted by “1”. 
#A character “0” can move by entering a row coordinate from 1 to 6 and column co-ordinate from 1 to 4. 
#The character starts at array poistion [0,0] (Figure 1) and will move, 
#for example, to row 0 column 1 (Figure 2) if the user enters 1, 2 for the row and column coordinates. 
#Remember that the indices of the array both start at 0. 
#Write a pseudocode algorithm that creates a 2-D grid[row, column], drawn as shown in Figure 1.
#Prompt the user to enter a row and column value. Update the character position and draw the new grid.

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def draw_grid():
    pos = 0
    for i in range(6):
        print(grid[pos])
        pos += 1

draw_grid()

x = int(input('Please input the x coordinate to move it to\n'))
y = int(input('Please input the y coordinate to move it to\n'))

grid[0][0] = 0
grid[x][y] = 1

draw_grid()