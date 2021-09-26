# Golubovich Igor for Python Course | homework №3 | task №1


x = input('Enter the first value:\n')
y = input('Enter the second value:\n')

def inputX1(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
 
def inputY1(str):
    try:
        float(str)
        return True
    except ValueError:
        return False        



number_x = inputX1(x)
number_y = inputY1(y)

#print(number_x)
#print(number_y)


Xint = x.isnumeric()
Yint = y.isnumeric()


#print(Xint)
#print(Yint)


if number_x == True and number_y == True:
    if Xint == True and Yint == True:
        if 3 <= int(x) <= 21 and 3 <= int(y) <= 21:
            R1 = abs(int(x) - int(y))
            print('output: ' + str(R1))
        else:
            R2 = x + y
            print('output: ' + str(R2))
    else:
        if 3 <= float(x) <= 21 and 3 <= float(y) <= 21:
            R3 = abs(float(x) - float(y))
            print('output: ' + str(R3))
        else:
            R4 = x + y
            print('output: ' + str(R4))
else:
    R5 = x + y
    print('output: ' + str(R5))














