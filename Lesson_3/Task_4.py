# Golubovich Igor for Python Course | homework №3 | task №4

import math


def inputFigure(message):
    while True:
        try:
            userInput1 = int(input(message))
        except ValueError:
            print('!!!ERROR!!! Need to enter the number from 1 to 3 !!!')
            continue
        if userInput1 < 1:
            print('!!!ERROR!!! Need to enter the number from 1 to 3 !!!')
            continue
        elif 3 < userInput1:
            print('!!!ERROR!!! Need to enter the number from 1 to 3 !!!')
            continue
        else:
            return userInput1

figure = inputFigure('Enter a number to calculate the area figures:\n1 - rectangle\n2 - triangle\n3 - circle\nInput number:  ')



def inputValue(message):
    while True:
        try:
            userInput2 = float(input(message))
        except ValueError:
            print('!!!ERROR!!! Need to enter positive number > 0 !!!')
            continue
        if userInput2 <= 0:
            print('!!!ERROR!!! Need to enter positive number > 0 !!!')
            continue
        else:
            return userInput2


#value_length = inputValue('Enter value: ')


def inputTc(b):
    while True:
        try:
            userInput3 = float(input(b))
        except ValueError:
            print('!!!ERROR!!! Need to enter positive number > 0 !!!')
            continue
        if userInput3 <= 0:
            print('!!!ERROR!!! Need to enter positive number > 0 !!!')
            continue       
        elif userInput3 >= (Ta + Tb):
            print("!!ERROR!!! Tc > (Ta + Tb) It isn't triangle!!!")
            continue
        else:
            return userInput3


if figure == 1:
    print("You've chosen rectangle.")
    Ra = inputValue('Enter the value of the side "A" of the rectangle : ')
    Rb = inputValue('Enter the value of the side "B" of the rectangle : ')
    Sr = Ra * Rb
    print('S of rectangle = ' + str(Sr))
elif figure == 3:
    print("You've chosen circle.")
    Cr = inputValue('Enter the value of the radius of the circle : ')
    Sc = math.pi * (Cr ** 2) 
    print('S of circle = ' + str(Sc))
else:
    if figure == 2:
        print("You've chosen triangle.")
        Ta = inputValue('Enter the value of the side "A" of the triangle : ')
        Tb = inputValue('Enter the value of the side "B" of the triangle : ')
        Tc = inputValue('Enter the value of the side "C" of the triangle : ')
        if (Ta + Tb) <= Tc:
            print("!!!ERROR!!! Tc > (Ta + Tb) It isn't triangle!!!")
            Tc = inputTc('Need to enter Tc wich < then (Ta + Tb):\n')
            P = (Ta + Tb + Tc) / 2
            Rt = math.sqrt(P * (P - Ta) * (P - Tb) * (P - Tc)) 
            print('S of triangle = ' + str(Rt))
        else:
            P = (Ta + Tb + Tc) / 2
            Rt = math.sqrt(P * (P - Ta) * (P - Tb) * (P - Tc)) 
            print('S of triangle = ' + str(Rt))
