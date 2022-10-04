# НОД

# 1 Вариант
# def Find_GCD(a, b): # GCD = greatest common divisor
#     while a != b:
#         print(a, " ", b)
#         if a > b: a -= b
#         else: b -= a
#     return a


# x = int(input('Введите первое число: ')) 
# y = int(input('Введите второе число: ')) 
# if x > y: k = x
# else: k = y
# while(True):
#     if (k % x == 0) and (k % y == 0):
#         res = k
#         break
#     k += 1
# print(f'Наименьшее общее кратное двух чисел равно: {res}')

# 2 Вариант
# x, y = 3, 8
# if x > y: x = max 
# else: x = min 
# print(min, max) 

# 3 Вариант
# if x > y: big_num = x
# else: big_num = y
# while(True):
#     if (big_num % x == 0) and (big_num % y == 0):
#         result = big_num
#         break
#     big_num += 1
# print(result)

# 4 Вариант - Из большего вычитаем меньшнн, пока они не сравняются
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a

# print(a)

# 5 Вариант
# a = 123
# b = 23
# if a < b :
#     a, b = b, a

# while b!=0:
#     a, b = b, a % b

# print(a)



# Задача 2
# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". То есть, 
# функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

# 1 Вариант
# str1 = 'alibaba'
# str2 = 'li'
# # print(str2 in str1)
# bl = lambda x:str1 in str2
# print(bl)

# 2 Вариант
# contains = lambda s, sample='ra': sample in s  
# s = input()
# print(contains(s))


# Задача 3
# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы 
# выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# разность 2х соседних числел дб равно 1, если больше, то число пропущено

# 1 Вариант
# with open('tex.txt','r') as n:
#     lst = [int(i) for i in n.readline().split()]
#     for i in range(1,len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             print(lst[i]-1)

# 2 Вариант
# def find_num(lst):
#     for i in range(1, len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             return i, lst[i] - 1
#     return -1, -1

# with open("data.txt", "r") as fin:
#     lst = [int(i) for i in fin.readline().split()]
#     print(lst)
#     pos, num = find_num(lst)
#     print(pos,num)
#     if (pos != -1):
#         lst.insert(pos, num)
#     print(lst)


# Задача 4
# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)

