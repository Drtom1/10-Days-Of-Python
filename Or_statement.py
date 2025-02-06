# in or statement, when any one of the conditions is true
# it will give the desired output

school = input('What school do you attend? ')
fees = 0
if school == 'FUTO' or school == 'UNN' or school == 'UNIPORT' or school== 'UNIBEN':
    fees = 5000
else:
    fees = 10000

# instead of using multiple or statements,
# we can use the in statement to make code cleaner

if school in('UNICAL', 'UNIUYO', 'FUTA', 'LASU', 'ESUT'):
    fees = 2500
print('Your tuition is: ' + str(fees))