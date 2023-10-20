#A teacher has a class of 30 pupils.  Each pupil has taken 3 tests during the year.  
#The teacher needs to know the average class score for test1, test2 and test3.  
#She also needs to know the overall average test score for the year. 
#Write an algorithm in pseudocode that will allow the teacher to input all results and print this information. 

test1 = []
test2 = []
test3 = []
count = 0

while count < 31:
    temp1 = int(input('Please enter a test score for Test 1\n'))
    count += 1
    test1.append(temp1)
count = 0

while count < 31:
    temp2 = int(input('Please enter a test score for Test 2\n'))
    count += 1
    test2.append(temp1)
count = 0

while count < 31:
    temp3 = int(input('Please enter a test score for Test 3\n'))
    count += 1
    test3.append(temp1)
count = 0

avg1 = (sum(test1)/30)
avg2 = (sum(test2)/30)
avg3 = (sum(test3)/30)

avg4 = (avg1+avg2+avg3)/3

print('Average score for Test 1: '+ str(avg1))
print('Average score for Test 2: '+ str(avg2))
print('Average score for Test 3: '+ str(avg3))
print('Average score for all tests: '+ str(avg4))
