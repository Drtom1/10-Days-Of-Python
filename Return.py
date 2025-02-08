# first_name = input('What is your first name? ')
# first_init = first_name[0:1]
# last_name = input('What is your last name? ')
# last_init = last_name[0:1]
# print('Your initials are: ' + first_init.capitalize() + last_init.capitalize())

# i can use a function to make it all easier 
# but this time the function returns a value
def get_init(name):
    init = name[0:1].upper()
    return init

first_name = input('What is your first name? ')
first_init = get_init(first_name)
last_name = input('What is your last name? ')
last_init = get_init(last_name)
print('Your initials are: ' + first_init + last_init)
