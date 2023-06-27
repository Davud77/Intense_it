# Функции - именованная часть кода

import math


CHECK_LIST = ['админ', 'superuser', 'суперадмин']  # константа


# access_level = input('Введите ваш уровень доступа: ')
# if access_level in CHECK_LIST:
#     print('Доступ разрешен!')
# else:
#     print('В доступе отказано!')
# # --------------------------------------------------
# access_level = input('Введите ваш уровень доступа: ')
# if access_level in CHECK_LIST:
#     print('Доступ разрешен!')
# else:
#     print('В доступе отказано!')


# Функция без аргументов
# ШАБЛОН
# def <имя функции>():  # определение функции
#     <тело функции>  # перечень действий к выполнению

# <имя функции>()  # вызов функции

def access_check():  # определяем функцию с именем access_check
    access_level = input('Введите ваш уровень доступа: ')  # тут и ниже тело функции
    if access_level in CHECK_LIST:
        print('Доступ разрешен!')
    else:
        print('В доступе отказано!')
    
access_check()  # вызов функции access_check
# print(access_level)  # ошибка, переменная не видна вне функции
access_check()  # вызов функции access_check


# Функции с неск. аргументами
# ШАБЛОН
# def <имя функции>(<параметры функции>):  # определение функции с параметрамиы
#     <тело функции>  # исполняемая часть

# <имя функции>(<аргументы функции>)  # вызов функции с аргументами


def sqrt_with_check(num):  # задается 1 параметр - num
    if num >= 0:
        return math.sqrt(num)  # return прерывает выполнение функции и возвращает значение
    else:
        return 0  # в противном случае команда return вернет значение 0
    

print(round(sqrt_with_check(10), 2))  # вызов функции с одним аргументом
print(sqrt_with_check(-3))  # вызов функции с одним аргументом


def greeting(name, surname):  # name, surname - параметры
    print(f'Здравствуйте, {surname} {name}')

greeting('Магомед', 'Магомедов')  # вызов функции с двумя аргументами


# Области видимости - глобальная и локальная
# Глобальная область видимости для переменных, объявленных вне функций
# Локальная область видимости для переменных, объявленных внутри функций

def incr(num):  # объявление функции для инкрементации
    # print(num + 1)  # переменная num существует только внутри функции
    # num_list.append(num + 1)  # num_list - глобальная переменная, но изменяется в функции
    num_list = [1, 2, 3, 4]  # локальная переменная, удалится по завершении функции


# print(num)
num_list = [1, 2, 3]  # глобальная переменная, т.к. объявлена вне какой-либо функцииы
incr(3)  # вызов функции
print(num_list)