import time
from random import randint


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
