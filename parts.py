#A parts supply company uses 4-digit part numbers.  The last digit indicates the production run. 
#If the production run is 6,7 or 8 it is considered to be an old model.  
#Write a pseudocode algorithm that prompts the user to enter a part number.  
#The length of the part number should be equal to 4 digits, otherwise an error message will be displayed and the user will be prompted to input the part number again. 
#The algorithm should count the total number of parts entered and the number of old model parts and output these totals.  
#Data input will terminate when the user inputs 9999. 
part = '0'
partcount = 0
oldcount = 0

while part != '9999':
    part = input('Enter the part number.\n')
    if len(part) == 4:
        if part[3] not in ['6','7','8']:
            partcount += 1
        else:
            partcount += 1
            oldcount += 1
    else:
        print('Input a 4 digit number.')

print('You entered '+ str(partcount) +' parts and '+ str(oldcount) +' were old.')