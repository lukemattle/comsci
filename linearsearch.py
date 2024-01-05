data = [5, 9, 11, 15, 19, 25, 34, 39, 47, 48]
pos = 0
found = False

search = int(input('What would you like to search for?\n'))

while found == False and pos < len(data):
    if data[pos] == search:
        found = True
    else:
        pos += 1

print(f'Your search was found as position {pos}')