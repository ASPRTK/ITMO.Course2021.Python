import math

"МОДЕЛЬ"
def calculate_distance(location1, location2):
    """
    Эта функция возвращает расстояние по большому кругу между местоположением1 и
    местоположением2.

    Параметры:
    location1 (iterable): географические координаты
    первого местоположения. Первый элемент итерации - широта,
    второй - долгота.

    location2 (iterable):  географические координаты
    второго местоположения. Первый элемент итерации - широта,
    второй - долгота.

    Возвращается:
    значение с плавающей точкой: Значение расстояния между двумя точками, вычисленное с использованием
    формулы хаверсина
    """

    lat1 = math.radians(location1[0])
    lat2 = math.radians(location2[0])
    long1 = math.radians(location1[1])
    long2 = math.radians(location2[1])
    del_lat = (lat1 - lat2) / 2
    del_long = (long1 - long2) / 2
    angle = math.sin(del_lat)**2 + math.cos(lat1) * math.cos(lat2) * \
        math.sin(del_long)**2
    distance = 2 * 3959.191 * math.asin(math.sqrt(angle))
    return distance
