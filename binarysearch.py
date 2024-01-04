data = [5, 9, 11, 15, 19, 25, 34, 39, 47, 48]

search = int(input('What would you like to search for?\n'))

found = False
first = 0
last = len(data) - 1

while first <= last and not found:
    mid = (first + last) // 2
    if data[mid] == search:
        found = True
    elif search < data[mid]:
        last = mid - 1
    else:
        first = mid + 1

if found:
    print(f'Your search was found at position {mid}')
else:
    print('Your search was not found in the list.')
