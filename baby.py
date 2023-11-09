#The birth weights in grams of 100 babies, which vary between 1500 to 4000 grams, are held in an array weight. 
#Write pseudocode for an algorithm which calculates the average birth weight, 
#and then prints out the number of babies who are more than 500 grams below the average weight, 
#together with the average weight of these.

import random

weight = []
pos = 0
light = 0

for i in range (100):
    temp = random.randint(1500,4000)
    weight.append(temp)

totalweight = sum(weight)
avgweight = (totalweight / 100)

for i in range (100):
    if weight[pos] < (avgweight - 500):
        light += 1
    pos += 1

print(f'Average weight: {avgweight}')
print(f'Babies more than 500 grams below average: {light}')