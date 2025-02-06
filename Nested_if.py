# sometimes you will need to use nesting in python
country = input('What country are you from? ')
if country.lower() == 'nigeria':
    tribe = input('What is your tribe? ')
    if tribe.lower() == 'igbo':
        greeting = 'ndewo!'
    elif tribe.lower() == 'yoruba':
        greeting = 'ekaro!'
    elif tribe.lower() == 'hausa':
        greeting= 'salam alekum!'

else: 
    greeting = 'Hello, user!'

print(greeting)


