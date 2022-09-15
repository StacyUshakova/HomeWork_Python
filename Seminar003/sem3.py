# Задача 1
# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

# fname = input('файл') # создаем переменную
# f = open(fname, 'w') # открываем файл
# while True: # записываем построчно данные
#     s = input() # вводим наши значения
#     if s == '': # пустая строка (окончание ввода по условию задачи)
#         break
#     f.write(s+'\n') # если нет пустой строки, то записываем в наш файл, \n - специальный символ, который переносит на новую строчку
# f.close()

# fname = input('файл')
# f = open(fname, 'w')
# while True:
#     s = input()
#     if s == '':
#         break
#     f.write(s+'\n')
# f.close()

# Задача 2
# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

# f = open('textfile.txt','r')
# countLines = 0
# countwordsInLines = []
# countCharsInLines = []
# for line in f:
#     countLines+=1
#     if line != '\n':
#         countwordsInLines.append(line.count(' ') + 1)
#     else:
#         countwordsInLines.append(0)
#     countCharsInLines.append(line.count('') -2)
# f.close()
# print(countLines)
# print(countwordsInLines)
# print(countCharsInLines)

# f = open('article.txt','r')
# line = 0
# for i in f:
#     line += 1

# flag = 0
# word = 0
# for j in i:
#     if j != ' ' and flag == 0:
#         word += 1
#         flag = 1
#     elif j == ' ':
#         flag = 0

# print(len(i), 'симв.', word, 'сл.')
# print(line, 'стр.')
# f.close()

# Задача 3
# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая принимает
# неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного
# элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
# тесты
# # k1=22, k2=31, k3=11, k4=91
# name='Елена', age=31, weight=61, eyes_color='grey'



# Задача 4
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент
# списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
# Тесты
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

