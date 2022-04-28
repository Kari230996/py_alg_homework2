'''
Практическое задание № 2

Циклы. Рекурсия. Функции.

https://drive.google.com/file/d/123lPvYqs-d2orJU9sAXVispmmYDMOu9u/view?usp=sharing
'''


def first(n):
    if n == 1:
        return n
    else:
        return n + (n-1)

def second(n):
    return n * (n+1) // 2


n = 1

while True:
    if first(n) == second(n):
        print(f"Для n = {n} - True")
        n += 1
    else:
        print(f"Для n = {n} - False")
        break