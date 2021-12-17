

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
