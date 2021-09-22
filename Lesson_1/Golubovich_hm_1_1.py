# Golubovich Igor for Python Course | homework №1 | task №1

import math

def inputSeconds(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('!!ERROR!!! Need to enter the number of seconds from 0 to 86400!!!')
            continue
        if userInput < 0:
            print('!!ERROR!!! Need to enter the number of seconds from 0 to 86400!!!')
            continue
        elif 86400 < userInput:
            print('!!ERROR!!! Need to enter the number of seconds from 0 to 86400!!!')
            continue
        else:
            return userInput
            break


time = inputSeconds('Enter the number of seconds from 0 to 86400:\n')

hours = math.floor(time / 3600)

minutes = math.floor((time % 3600) / 60)

seconds = (time % 3600) % 60

#print(hours)
#print(minutes)
#print(seconds)

print('hours minutes seconds')
print(hours, minutes, seconds, sep = '      ')