score = int(input('Enter the exam score. '))
atn = int(input('Enter the attendance. '))

grade = 'F'

if attendance > 90:
    print('Grade =' + grade)
else:
    if exam > 90:
        grade = 'A'
    elif exam > 80:
        grade = 'B'
    elif exam > 70:
        grade = 'C'
    else:
        grade = 'F'
print('Grade =' + grade)