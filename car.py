#Write a program in pseudocode that displays a menu with three option choices for a car rental firm.  The choices are 
#	1: Economy Car 
#	2: Saloon Car 
#	3: Sports Car  

#After the user enters a choice, the program will tell them if it was invalid, in which case the program will end.  
#If a valid choice is entered, the program will ask them if they wish to proceed or cancel.  After they respond, the program will confirm their response and then output the message “Have a nice day.”

choice = input('What car would you like?\n1: Economy Car\n2: Saloon Car\n3: Sports Car\n')

if choice not in [1,2,3]:
    print('Invalid choice.')
else:
    if choice == 1:
        cont = input('Would you like to proceed with your rental of Economy Car?\n')
    elif choice == 2:
        cont = input('Would you like to proceed with your rental of Saloon Car?\n')
    else:
        cont = input('Would you like to proceed with your rental of Sports Car?\n')
    if cont == 'Y':
        print('You have confrmed your purchase. Have a nice day.')
    else:
        print('You have cancelled your purchase.')