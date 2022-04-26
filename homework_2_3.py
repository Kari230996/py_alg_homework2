'''
Практическое задание № 2

Циклы. Рекурсия. Функции.

https://drive.google.com/file/d/123lPvYqs-d2orJU9sAXVispmmYDMOu9u/view?usp=sharing
'''


n = int(input("Введите целое натуральное число: "))

while n != 0:
    last_digit = n % 10
    n = n // 10
    print(last_digit,  end = '')


