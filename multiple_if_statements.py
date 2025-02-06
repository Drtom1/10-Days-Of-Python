# let us take a look at multiple if statements
State = input('What state are you from? ')
tax = 0
if State == 'Adamawa':
    tax = 0.21
if State == 'Enugu':
    tax = 0.17
if State =='Abia':
    tax = 0.13

else:
    tax = 0.15

# since we can not possibly have multiple states at the same time
# it would be more efficient to use use the elif statement

if State == 'Jos':
    tax = 0.14
elif State == 'Anambra':
    tax = 0.11
elif State == 'Imo':
    tax = 0.25
print('Your tax is: '+ str(tax))