#An online bookstore gives free 2nd class mail delivery (code 2) for any order value greater than or equal to £15.00
#For order values less than £15.00, 2nd class mail delivery costs £3.50.
#For any value of order, a customer may choose to pay £5.00 for guaranteed next day delivery (code 1).

price = float(input('How expensive is the book you would like to purchase?'))
nday = input('Would you like next day delivery for £5? Y or N')
delivery = float(0)

if nday == 'Y':
    delivery = 5
elif price < 15:
    delivery = 3.5
else:
    delivery = 0

print('Your postage cost is ' + str(delivery))