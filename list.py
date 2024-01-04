list = [1,2,3,4,5,6,7,8,9]
pos = 0
max_ = 0
temp = 0

for pos in list:
    if pos > max_:
        max_ = pos
        pos = 0

for x in range((len(list) - 1)):
    if pos % 2 == 0:
        temp = list[pos]
        list[pos] = list[pos+1]
        list[pos+1] = temp
    pos += 1

print(str(max_))
print(list)