"МОДЕЛЬ"
def degree_minutes_seconds(location):
    """
    Функция на основе георграфических координат определяет градусы
    минуты и секунды

    :param location: (iterable): географические координаты
    местоположения. Первый элемент итерации - широта,
    второй - долгота.

    :return: градусы минуты секунды
    """

    minutes, degrees = math.modf(location)
    degrees = int(degrees)
    minutes *= 60
    seconds, minutes = math.modf(minutes)
    minutes = int(minutes)
    seconds = 60 * seconds
    return degrees, minutes, seconds