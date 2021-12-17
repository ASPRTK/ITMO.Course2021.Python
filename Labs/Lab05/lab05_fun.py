# Практическое занятие 5. Применение функций

# 1. Создайте функцию, реализующую ввод имен игроков. Подумайте каким
# образом можно вернуть вносимые данные в программу.
# 2. Создайте функцию, реализующий ядро игры.
# 3. Реализуйте с помощью функции победителя игры.


# Ввод имен играющих
import time
from random import randint


def inputPlaer():
    igrok1 = input('Введите имя 1-го играющего: ')
    igrok2 = input('Введите имя 2-го играющего: ')
    return igrok1, igrok2


igrok1, igrok2 = inputPlaer()


# ЗАДАЧА 01: Добавьте в программу цикл for, реализующий 5 партий (бросков):
def corGames():
    countPlayer01 = 0
    countPlayer02 = 0
    for i in range(5):
        # Моделирование бросания кубика первым играющим
        print('Кубик бросает', igrok1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        # Моделирование бросания кубика вторым играющим
        print('Кубик бросает', igrok2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        # Определение результата (3 возможных варианта)
        if n1 > n2:
            print('\tВыиграл', igrok1)
            countPlayer01 += 1
        elif n1 < n2:
            print('\tВыиграл', igrok2)
            countPlayer02 += 1
        else:
            print('\tНичья')
        return countPlayer01, countPlayer02


countPlayer01, countPlayer02 = corGames()
# ЗАДАЧА 02:  Добавьте реализацию определения победителя. Например, с помощью
# подсчета количества побед каждым игроком, или суммированием очков.
# ЗАДАЧА 03:  После цикла добавьте оператор ветвления для определения итогового
# победителя.

print('Итог счета: (', igrok1, '/', igrok2, ') - ', countPlayer01, ':', countPlayer02, sep='')


def result(countPlayer01, countPlayer02, textVIN):
    if countPlayer01 > countPlayer02:
        print(textVIN, igrok1)
    elif countPlayer01 < countPlayer02:
        print(textVIN, igrok2)
    else:
        print('Ничья')


result(countPlayer01, countPlayer02, 'По итогу сражения одержал победу:')
