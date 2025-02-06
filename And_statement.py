# instead of multiple nested if statements
# we can add the and condition to simplify things out

# students get a first class if their GPA is >= 85
# and if their lowest grade is >= 70

gpa = float(input('What is your GPA? '))
worst_grade = input('What is your lowest grade? ')
worst_grade = float (worst_grade)

if gpa >= 4.5 and worst_grade >= 3.0:
    print('You made a first class!')
else:
    print('You did not make a first class.')