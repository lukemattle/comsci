while birdFound == False:
    if bird == birdName[count]: 
        birdFound = True 
        birdsObserved = input("Enter number of birds observed: ")
        birdCount[count] = birdCount(count) + birdsObserved 
count += 1
    