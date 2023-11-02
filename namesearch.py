#A teacher uses a program that stores pupil names in an array. The array is indexed from 0, so the first element in the array is name[0].
#Occasionally the teacher needs to search for a name to find the student’s record number, which is index + 1. 
#Write a pseudocode algorithm that will search an array name containing max elements, 
#to find a name and output record number if it exists. If the name does not exist the user should be told the term was not found.  
#Use appropriate prompts for input and output in your solution.

found = 0
name = ['john', 4533, 'bob', 3424, 'kevin', 1344]

iname = input('Please input the name you would like to search.\n')

for i in range(len(name)):
    if iname == name[i]:
        found = 1
        pos = i

if found = 1
    print('Student found! Name: ' + str(name[pos]) + ' Record number: ' + str(name[pos + 1]))
else:
    print('Student not found.')