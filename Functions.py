# moving code into a fuction allows to call the function everytime 
# you need that code to run instead of always copying and pasting
from datetime import datetime

def details():
    print('You are currently breating')
    print('You are staring at your system')
    print('Task completed!')
    print(datetime.now())
    print()

name = 'Tom'
details()

for x in range(0,10):
    print(x)
details()
