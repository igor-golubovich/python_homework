# Golubovich Igor for Python Course | homework №3 | task №5


def inputNumber(message):
    while True:
        try:
            userInput1 = float(input(message))
        except ValueError:
            print('!!ERROR!!! Need to enter the number > 0 !!!')
            continue
        if userInput1 < 0:
            print('!!ERROR!!! Need to enter the number > 0 !!!')
            continue
        else:
            return userInput1

x = inputNumber('Enter the number > 0 :\n')

z = int(x)

print('Sum of number =', sum(int(c) for c in str(z)))  #бесконечная но с int


str_x = str(x)                      # число в строку

str_x = str_x.replace('.', '')     # производим замену десятичного разделителя

#print(str_x)

lst_x = list(str_x)          # строку с числом в список строк с цифрами

#print(lst_x)

lst_num = map(int, lst_x)    # преобразовываем каждый элемент полученного списка строк с цифрами в список целых чисел

s = sum(lst_num)               # применяем функцию `sum()`

print('Sum = ', s)