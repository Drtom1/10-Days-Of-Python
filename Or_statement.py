# in or statement, when any one of the conditions is true
# it will give the desired output

school = input('What school do you attend? ')
fees = 0
if school == 'FUTO' or school == 'UNN' or school == 'UNIPORT' or school== 'UNIBEN':
    fees = 5000
else:
    fees = 10000
print('Your school fee is:' + str(fees))