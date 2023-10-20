coins = [1,2,5,10,20,50]
total = 0

for coin in coins:
    amount = int(input('Please enter the total amount of '+ str(coin) +'p'))
    total = coins*amount

if total >= 100:
    total /= 100
    print('Total takings: £' + str(total))

print('Total takings: ' + str(total) + 'p')