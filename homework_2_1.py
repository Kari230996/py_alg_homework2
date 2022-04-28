'''
Практическое задание № 1

Циклы. Рекурсия. Функции.

https://drive.google.com/file/d/123lPvYqs-d2orJU9sAXVispmmYDMOu9u/view?usp=sharing
'''


while True:
    a, b = float(input('Введите первое число: ')), float(input('Введите второе число: '))
    operation = input("Введите знак операции ('0', '+', '-', '*', '/'): ")

    if operation != '0' and operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('Ошибка! Неверный знак операции')
    elif operation == '0':
        break
    elif operation == '+':
        print(f'{a} {operation} {b} = {a + b}')
    elif operation == '-':
        print(f'{a} {operation} {b} = {a - b}')
    elif operation == '*':
        print(f'{a} {operation} {b} = {a * b}')
    elif operation == '/':
        try:
            print(f'{a} {operation} {b} = {a / b}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')


