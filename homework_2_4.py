'''
Практическое задание № 4

Циклы. Рекурсия. Функции.

https://drive.google.com/file/d/123lPvYqs-d2orJU9sAXVispmmYDMOu9u/view?usp=sharing
'''

n = int(input("Введите количество элементов (n): "))

i = 0
range_num = 1
sum = 0

while i < n:
    sum += range_num
    range_num /= -2
    i += 1
print(f"Cумма n элементов: {sum}")