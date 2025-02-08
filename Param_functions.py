# we can pass multiple parameters to a function

def get_init(name, force_upper = True):
# notice that we made the force uppercase true by default to make life easier
# though i can always specify on line 12 if i want to override the default
    if force_upper:
        initial = name[0:1].upper()
    else: initial = name[0:1]
    return initial 

first_name = input('Enter your first name: ')
first_init = get_init(name = first_name, force_upper = False)

print('Your initial is: ' + first_init)