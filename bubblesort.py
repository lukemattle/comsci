data = [5, 45, 11, 33, 56, 29, 25, 2, 47]

last = len(data) - 1
done = False
noswap = 0

while not done and noswap < last:
    noswap = 0
    for pos in range(last):
        temp = data[pos]
        temp2 = data[pos + 1]

        if temp > temp2:
            data[pos] = temp2
            data[pos + 1] = temp
        else:
            noswap += 1

    if noswap == last:
        done = True

print(data)
