#Input 10 marks, find highest & average mark, allow user to see if a specific mark exists in the entered marks

marks = []
markno = 1
max_ = 0
pos = 0

amount = int(input('How many marks would you like to enter?\n'))

for i in range(amount):
    mark = int(input('Please enter mark ' + str(markno) + '\n'))
    marks.append(mark)
    markno += 1

for mark in marks:
    if mark > max_:
        max_ = mark

for i in range (len(marks)):
    avg = sum(marks)
    avg /= len(marks)
    avg = round(avg,1)

def search():
    pos = 0
    search = int(input('Please enter the score you want to search for\n'))
    while pos < (amount - 1):
        if marks[pos] == search:
            print('Mark ' + str(search) + ' found at position ' + str(pos + 1))
            break
        pos += 1

print('The highest mark was ' + str(max_))
print('The average mark was ' + str(avg))
choice = input('Would you like to search for a mark?\n')

if choice in ['yes', 'Yes', 'y', 'Y']:
    search()
else:
    print('Bye')