# Golubovich Igor for Python Course | homework №3 | task №7

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

a = inputValue('Enter the deposit amount:\n')

b = inputValue('Enter the time in years:\n')

i = 1

while i <= b:
    a = a + (a * 0.1)
    i += 1

print('Your money:', round(a) ,'for', b , 'years')