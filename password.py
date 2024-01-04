#Write pseudocode for a subroutine called getPword() that takes one parameter, called attempt, which can have a value of 1 or 2. 
#The subroutine should prompt the user to enter a password if attempt = 1, 
#or prompt the user to re-enter a password if the attempt = 2, and then return the password.  
#The subroutine should also check that the length of the password is a valid length between 6 to 8 characters.  
#The main program will verify that the two passwords are the same, and re-prompt for entry if they are not.  
#If both passwords are the same, a message is displayed, informing the user that the password change has been successful. 

def getPword():
    while True:
        att1 = input('Please enter a password between 6 and 8 characters.')
        if len(att1) in range(6,8):
            att2 = input('Please re-enter your password.')
            if att1 ==  att2:
                print(f'Success. Your password is {att1}')
                break
            else:
                print('Passwords do not match.')
        else:
            print('Invalid.')
            
getPword()