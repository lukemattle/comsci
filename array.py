#Write a program to read 6 numbers into an array numbers[0] to numbers[5], 
#output them in reverse order and then output the total and average.

array = [0,1,2,3,4,5]
numbers = []
pos = 5

for i in range(len(array)):
    temp = array[i]
    numbers.append(temp)

for x in range(len(numbers)):
    print(numbers[pos])
    pos -= 1

print(sum(array))
print(sum(array) / 6)
