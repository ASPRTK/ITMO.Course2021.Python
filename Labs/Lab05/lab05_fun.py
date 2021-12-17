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


def result(pointsPlayer01, pointsPlayer02, igrok1, igrok2,  textVIN):
    if pointsPlayer01 > pointsPlayer02:
        print(textVIN, igrok1)
    elif pointsPlayer01 < pointsPlayer02:
        print(textVIN, igrok2)
    else:
        print('Ничья')


def rollBone(igrok):
    print('Кубик бросает', igrok)
    time.sleep(2)
    pointsPlayer = randint(1, 6)
    print('Выпало:', pointsPlayer)
    return pointsPlayer



def corGames(igrok1, igrok2):
    countPlayer01 = 0
    countPlayer02 = 0
    for i in range(5):
        # Моделирование бросания кубика первым играющим
        n1 = rollBone(igrok1)
        # Моделирование бросания кубика вторым играющим
        n2 = rollBone(igrok2)
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







def main():
    igrok1, igrok2 = inputPlaer()
    countPlayer01, countPlayer02 = corGames(igrok1, igrok2)
    print('Итог счета: (', igrok1, '/', igrok2, ') - ', countPlayer01, ':', countPlayer02, sep='')
    result(countPlayer01, countPlayer02, igrok1, igrok2,  'По итогу сражения одержал победу:')


main()