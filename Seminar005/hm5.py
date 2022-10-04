# Задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# lst = ['абв', 'фыва', 'пролджабв', 'смит', 'апрабв']
# print(*filter(lambda x:not 'абв' in x, lst))

# Задача 2
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# a = int(input('Введите количество конфет '))
# hod = 0
# wins = {0: 'Игрок', 1: 'Бот'}
# while a > 0:
#     if a <= 28:
#         print(f'Выиграл {wins[hod]}')
#         break
# if hod % 2 == 0:
#     print('Ход Игрока')
#     d = int(input('Введите количество конфет, которое хотите взять'))
#     a -= d
#     print(f'Осталось конфет: {a}')
# else:
#     print('Ход Бота')
#     d = a % 29
#     a -= d
#     print(f'Осталось конфет: {a}')
# hod = (hod + 1) % 2

# Задача 3
# Создайте программу для игры в ""Крестики-нолики"".

# # Инициализация карты
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8]) 

# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol

# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win

# game_over = False
# player1 = True
 
# while game_over == False:
 
#     print_maps()
 
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
 
#     step_maps(step,symbol) # делаем ход в указанную ячейку
#     win = get_result() # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
        
# print_maps()
# print("Победил", win) 

# Задача 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file_encode.txt', 'w') as data:
#     data.write('AGHJDOSPVHUILMKLKJK')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')