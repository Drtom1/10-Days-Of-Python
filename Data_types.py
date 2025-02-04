# to get current date and time 
# we need to use the datetime libraries
from datetime import datetime, timedelta 
current_date = datetime.now()
print('today is: ' + str(current_date))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = current_date - one_day

print('Yesterday was: ' + str(yesterday))


# we can also use the date function to control date formatting

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year ' + str(current_date.year))

# testing the strptime function

birthday = input('When is your birthday (dd/mm/yy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print ('Birthday: ' + str(birthday_date))
# converting it using the strp function allows you to use the date functions

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
