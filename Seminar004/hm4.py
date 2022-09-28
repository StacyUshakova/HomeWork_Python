# Задача 1
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите натуральное число: '))
# i = 2
# list = []
# old = n
# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old}: {list}")


# Задача 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = list(map(int, input('Введите последовательность чисел через пробел:\n').split()))
# print(list)

# new_list = []
# [new_list.append(i) for i in list if i not in new_list]
# print(f"Список из неповторяющихся элементов: {new_list}")

# Задача 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint

# def create_polynomial(k):
#     coefs = []
#     for i in range(k+1):
#         coefs.append(randint(0, 100))
#     return coefs

# def format_polynomial(coefs):
#     output = ""
#     for i in range(k, -1, -1):
#         c = coefs[i]
#         if c != 0:
#             if output != "": output += (" + " if c > 0 else " - ")
#         else:
#             if c < 0: output += "-"
#         if c != 1 and c != -1:
#             output += str(abs(c))
#             if i > 0: output += "*"
#         if i > 0: output += ("x" if i == 1 else "x^" + str(i))
#     return output

# k = int(input("Задайте степень k: "))
# coefs = create_polynomial(k)
# output = format_polynomial(coefs)
# print(coefs)
# print(output + " = 0")

# with open ('polynomials.txt', 'w') as file:
#     file.write(output)

# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random
def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res


def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res

f = open('dz40.txt', 'w')
f.write(nmnogochlen1())
print(nmnogochlen1())
f.close()

f = open('dz41.txt', 'w')
f.write(nmnogochlen2())
print(nmnogochlen2())
f.close()

f = open('dz40.txt', 'r')
list_5 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_5) == 3:
    c1 = list_5[2][1:]
if len(list_5) >= 2:
    b1 = list_5[1][3:-1]
a1 = list_5[0][:-1]
f.close()

f = open('dz41.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('dz42.txt', 'w')
f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()