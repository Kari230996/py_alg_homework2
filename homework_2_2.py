'''
Практическое задание № 2

Циклы. Рекурсия. Функции.

https://drive.google.com/file/d/123lPvYqs-d2orJU9sAXVispmmYDMOu9u/view?usp=sharing
'''


n = int(input('Введите любое натуральное число: '))

counter1 = 0
counter2 = 0

while n != 0:
    last_digit = n % 10

    if last_digit % 2 == 0:
        counter1 += 1
    else:
        counter2 += 1

    n = n // 10

print(f'Количество чётных чисел составляет: {counter1}, из нечётных: {counter2}')

