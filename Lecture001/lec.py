# print('hello world')

# a = 123 тип int
# b = 1.23 тип float
# print(a)
# print(b)

# value = None
# print(type(value))
# a = 123 
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# s = 'hello world' #строка

# print(s) #вывод строки
# print(a, b, s) #вывод нескольких значений

# a = 123 
# b = 1.23
# s = 'hello world'
# print(a, '-' ,b, '-',s)
# print('{} - {} - {}'.format(a,b,s))
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# list = ['1', '2', '3']
# print(list)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)

# f = False
# print(f)

# Арифметические операции:
# +, -, *, /, %, //, **
# Приоритет операций **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 123
# b = -321
# c=a+b
# print(c)

# a = 1.3
# b = 3
# c = round(a*b,3) # округения
# print(c)

# // чтобы получить целое число от деления
# % чтобы получить остаток от деления
#  ** возведение в степень

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in


# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 10
# T = 4
# x = 2
# print(func<T<(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции: if, if-else

# IF
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# ELIF
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# Управляющие конструкции: while

# original = 23
# inverted = 0
# while original!= 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# Когда основное тело цикла перестает работать

# original = 23
# inverted = 0
# while original!= 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# Когда мы знаем, что хотим

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 10, 2): # список от 1 до 10 с шагом 2
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# Немного о строках

# text = 'съешь еще этих мягких французских булок'
# print(len(text)) - Чтобы получить количество символов в ней
# print('еще' in text) - Если хотим проверить наличие какой-нибудь подстроки в строке
# print(text.isdigit()) - Проверить являтся ли все символы строки числами
# print(text.islower()) - Проверить являтся ли все символы строки символами нижнего регистра
# print(text.replase('еще', 'ЕЩЕ') - Если мы хотим что-то заменить

# help(text.istitle) - справочник Python

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])             # c
# print(text[1])             # ъ
# print(text[len(text)-1])   # к
# print(text[-5])            # б
# print(text[:])             # print(text)
# print(text[:2])            # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])           # ешь ещё
# print(text[6:-18])         # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6])           # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ..

# Список – пронумерованная, изменяемая коллекция объектов 
# numbers = [1, 2, 3, 4, 5]
# print(numbers)                # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)           # приведение типа range к list
# print(type(numbers))


# print(numbers)                # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                  # [20, 4, 6, 8, 10]
# print(numbers)                # [10, 2, 3, 4, 5


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)                    # red green blue
# for e in colors:
#     print(e*2)                  # redred greengreen blueblue
# colors.append('gray')           # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red')            #del colors[0] # удалить элемент

# Функции

# Это фрагмент программы, используемый многократно
# def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
