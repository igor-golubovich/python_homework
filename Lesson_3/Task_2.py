# Golubovich Igor for Python Course | homework №3 | task №2


def number(b):
    while True:
        try:
            userInput = float(input(b))
        except ValueError:
            print('!!ERROR!!! Need to enter the number from 3 to 23!!!')
            continue
        if userInput < 3 or 23 < userInput:
            print('!!ERROR!!! Need to enter the number from 3 to 23!!!')
        else:
            return userInput


x = number('Enter the first number from 3 to 23\n')

y = number('Enter the second number from 3 to 23\n')


# print(x)
# print(y)


def operat(o):
    while True:
        inputZ = input(o)
        if inputZ == '+':
            o1 = x + y 
            print('output: ' + str(o1))
            break
        elif inputZ == '-':
            o1 = x - y 
            print('output: ' + str(o1))
            break
        elif inputZ == '*':
            o1 = x * y 
            print('output: ' + str(o1))
            break
        elif inputZ == '/':
            o1 = x / y 
            print('output: ' + str(o1))
            break
        else:
            print('!!ERROR!!! Need to enter only: +, -, *, / !!!')
            inputZ = input('Enter only: +, -, *, /:\n')
            continue



z = operat('Enter operation only: +, -, *, /:\n')


