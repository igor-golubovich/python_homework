# Golubovich Igor for Python Course | homework №5 | task №1

# def input_type(message):
#     while True:
#         try:
#             userInput1 = int(input(message))
#         except ValueError:
#             print('!!!ERROR!!! Need to enter the number from 1 to 5 !!!')
#             continue
#         if userInput1 < 1:
#             print('!!!ERROR!!! Need to enter the number from 1 to 5 !!!')
#             continue
#         elif 5 < userInput1:
#             print('!!!ERROR!!! Need to enter the number from 1 to 5 !!!')
#             continue
#         else:
#             return userInput1



# def validation(fnc):
#     def wrapper(type_f, inp_value):
#         inp_value = []
#         if type_f == 1:
#             for i in inp_value:
#                 i = int(i)
#                 print(type(i))
#                 inp_value.append(i)
#             return fnc(type_f, inp_value)
#     return wrapper
            


# @validation
# def inp_f(type_f, inp_value):
#     return inp_value


# x =  input('Enter a list of values:\n')
# y = input_type('Enter a number to define the data type:\n1 - int\n2 - float\n3 - str\n4 - typle\n5 - list\nInput number:  ')

# a = inp_f(x, y)


# __________________________________________________________

dic_value = {
    1 : int,
    2 : float,
    3 : str,
    4 : tuple,
    5 : list,
}

def input_type(message):
    while True:
        try:
            userInput1 = int(input(message))
        except ValueError:
            print('!!!ERROR!!! Need to enter the number from 1 to 5 !!!')
            continue
        if userInput1 < 1:
            print('!!!ERROR!!! Need to enter the number from 1 to 5 !!!')
            continue
        elif 5 < userInput1:
            print('!!!ERROR!!! Need to enter the number from 1 to 5 !!!')
            continue
        else:
            return userInput1



# def validation_1(type_arg):
#     def actual_decorator(func):       
#         def wrapper(x):
#             x = type_arg(x)
#             return func(x)
#         return wrapper
#     return actual_decorator

# x = input('Enter a list of values:\n')
z = int(input_type('Enter a number to define the data type:\n1 - int\n2 - float\n3 - str\n4 - tuple\n5 - list\nInput number: '))
y = (dic_value.get(z))
print(y)


# @validation_1(type_arg = y)
# def inp_f(x):
#     return a



# a = inp_f(x)
# print(a)
# print(type(a))




