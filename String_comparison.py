favourite_food = input('What is your favourite meal?: ')
if favourite_food == 'fried rice':
    print('So you must be a good chef!')
else:
    print('I was thinking you liked fried rice')

# in python when comparing two strings, they are not equal if they are not in the same case


if favourite_food.lower() == 'fried rice':
    print('So you must be a good chef! ')

# this will compare lower case version of input
# and gives an output based on conditions specified