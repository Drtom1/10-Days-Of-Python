# using boolean variables can save you time and re-execution
# used for complicated if statements

gpa = float(input('What is your GPA? '))
lowest_grade = float(input('What is your lowest grade? '))
if gpa >= 4.5 and lowest_grade >= 3.5:
    first_class = True
else:
    first_class = False

# later in your code, if you want to check
# if student is first class, just check the boolean vcariable

if first_class:
    print('You made first class! ')

else:
    print('You did not make first class. ')
    