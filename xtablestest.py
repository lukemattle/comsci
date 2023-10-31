#Write pseudocode for a program that asks the user which times table they would like to be tested on, 
#and then gives them 5 random questions on this table, telling them each time whether they got the answer right or wrong. 
import random

xtable = int(input('What time table would you like to be tested on?\n'))
values = []
temp = xtable

values.append(temp)

for i in range(12):
    temp += xtable
    values.append(temp)

for x in range(5):
    qNo = (random.randint(0,11))
    correct = (values[qNo] - xtable)
    answer = int(input('What is ' + str(qNo) + ' * ' + str(xtable) + '\n'))
    print(correct)
    if answer == correct:
        print('Correct')
    else:
        print('Incorrect')