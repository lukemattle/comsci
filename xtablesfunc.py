#using a subroutine called multiples() which takes table, startnum, endnum and pupilName as parameters.  
#The subroutine will output the message and multiplication table.  
#The main program will prompt the user to enter the values and will then pass them to the routine.  

def multiples():
    table = int(input('What times table would you like?\n'))
    startnum = int(input('From what number in the table?\n'))
    endnum = int(input('To what number in the table?\n'))
    pupilName = input('What is your name?\n')
    print(f'Hi {pupilName}, here is your {table} times table, from {startnum} to {endnum}.')
    for x in range(startnum,endnum + 1):
        print(f'{table} x {x} = {table*x}')

multiples()