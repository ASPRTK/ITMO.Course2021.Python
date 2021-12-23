from Labs.Lab06_MVC.lab06_AnsMvc.model.degree_minutes_seconds import degree_minutes_seconds


def format_location(location):
    """
    Функция возвращает строку с информацией о локации
    в виде широты и долготы
    :param location: (iterable): географические координаты
    местоположения. Первый элемент итерации - широта,
    второй - долгота.
    :return:
    Строка для отображения информации о  локации (широта и долгота точки)
    """
    ns = ""
    if location[0] < 0:
        ns = 'S'
    elif location[0] > 0:
        ns = 'N'

    ew = ""
    if location[1] < 0:
        ew = 'W'
    elif location[0] > 0:
        ew = 'E'

    format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
    latdegree, latmin, latsecs = degree_minutes_seconds(abs(location[0]))
    latitude = format_string.format(latdegree, latmin, latsecs)
    longdegree, longmin, longsecs = degree_minutes_seconds(abs(location[1]))
    longitude = format_string.format(longdegree, longmin, longsecs)
    return '(' + latitude + ns + ',' + longitude + ew + ')'

