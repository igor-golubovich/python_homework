# Golubovich Igor for Python Course | homework №3 | task №6

def inputValue(message):
    while True:
        try:
            userInput1 = int(input(message))
        except ValueError:
            print('!!!ERROR!!! Need to enter positive number > 0 !!!')
            continue
        if userInput1 <= 0:
            print('!!!ERROR!!! Need to enter positive number > 0 !!!')
            continue
        else:
            return userInput1


a = inputValue('Enter the first number:\n')

b = inputValue('Enter the second number:\n')

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print('НОД = ', a)