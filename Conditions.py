# here we learn about about conditions in python
price = input('How much did you pay? ')
price =float(price)

if price >= 1.00:
    tax =0.07
    print('Your tax rate is: ') + str(tax)
    
# adding else statement
else:
    tax = 0
    print('Tax rate is: ' + str(tax))
