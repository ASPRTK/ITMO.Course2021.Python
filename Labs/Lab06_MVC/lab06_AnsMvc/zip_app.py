"""
Это программа для определения местоположения по почтовому индексу и почтовому индексу по местоположению,
а также для расчета расстояния между почтовыми индексами.

Почтовый индекс США представляет собой пятизначное целое число.
Местоположение указывается по названию города/населенного пункта и двухбуквенной аббревиатуре
штата.

Sample Execution:
-----------------

Command ('loc', 'zip', 'dist', 'end') => loc
loc

Enter a ZIP Code to lookup => 32963
32963
ZIP Code 32963 is in Vero Beach, FL, Indian River county,
coordinates: (027°41'23.23"N,080°22'32.61"W)


Command ('loc', 'zip', 'dist', 'end') => zip
zip

Enter a city name to lookup => Orlando
Orlando

Enter the state name to lookup => FL
FL
The following ZIP Code(s) found for Orlando, FL: 32801, 32802, 32803, 32804, 32805, 32806, 32807, 32808, 32809, 32810, 32811, 32812, 32814, 32815, 32816, 32817, 32818, 32819, 32820, 32821, 32822, 32824, 32825, 32826, 32827, 32828, 32829, 32830, 32831, 32832, 32833, 32834, 32835, 32836, 32837, 32839, 32853, 32854, 32855, 32856, 32857, 32858, 32859, 32860, 32861, 32862, 32867, 32868, 32869, 32872, 32877, 32878, 32886, 32887, 32890, 32891, 32893, 32897, 32898, 32899


Command ('loc', 'zip', 'dist', 'end') => dist
dist

Enter the first ZIP Code => 12180
12180

Enter the second ZIP Code => 32963
32963
The distance between 12180 and 32963 is 1102.72 miles


Command ('loc', 'zip', 'dist', 'end') => end
end

Done

Course: Python
Author(s): Konstantin Kuzmin
Date: 2/19/2019, modified 12/16/2021
"""


import math
import logging.handlers

from Labs.Lab06_MVC.lab06_AnsMvc import util


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


def zip_by_location(codes, location):
    """
    Функция возвращает массив
    :param codes: Список доступных команда
    :param location:  географические координаты
    местоположения. Первый элемент итерации - широта,
    второй - долгота.
    :return: возвращает массив  zips = []
    """
    zips = []
    for code in codes:
        if location[0].lower() == code[3].lower() and \
           location[1].lower() == code[4].lower():
            zips.append(code[0])
    return zips


def location_by_zip(codes, zipcode):
    """
    Функция проверяет что введенная пользователем команда
    существует и на основе ней генерирует кортеж
    :param codes:  Список доступных команда
    :param zipcode: Строка с введенной командой
    :return: Возвращает кортеж tuple(code[1:])
    """
    for code in codes:
        if code[0] == zipcode:
            return tuple(code[1:])
    return ()


"КОНТРОЛ"
def process_loc(codes):
    """
    Функция на основе почтового индекса (ZIP Code) осуществляет
    поиск соответствующего ему города и штат
    Отображает результат в виде строки с информацией о найденном городе
    :param codes:  Список доступных команда
    Отображает результат на основе введенных данных
    """
    zipcode = input('Введите почтовый индекс (ZIP Code) для поиска => ')
    print(zipcode)
    location = location_by_zip(codes, zipcode)
    if len(location) > 0:
        'Почтовый индекс {} находится в {}, {}, округ {},'
        print('Почтовый индекс {} находится в {}, {}, округ {},'.
              format(zipcode, location[2], location[3], location[4],
                     format_location((location[0], location[1]))))
    else:
        print('Неверный или неизвестный почтовый индекс')


"КОНТРОЛ"
def process_zip(codes):
    """
    Функция осуществляет поиск почтовых индексов дя введенных города и штата
    Выводи на консоль список с почтовыми индексами (ZIP Code(s)
    Функция для ввода названия города и штата
    :param codes: Принимает список команд
    """
    city = input('Введите название города для поиска => ')
    print(city)
    city = city.strip().title()
    state = input('Введите название штата для поиска => ')
    print(state)
    state = state.strip().upper()
    zipcodes = zip_by_location(codes, (city, state))
    if len(zipcodes) > 0:
        print('Найдены следующие почтовые индексы (ZIP Code(s)) для {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))
    else:
        print('Почтовый индекс (ZIP Code) для {}, {} не найден!'.format(city, state))


def process_dist(codes):
    """
      Функция для ввода названия города и штата
      :param codes: Принимает список команд
      Отображает результат на основе введенных данных
      """
    zip1 = input('Enter the first ZIP Code => ')
    print(zip1)
    # logging.info(f'Received the first ZIP {zip1}')
    logger.info(f'Received the first ZIP {zip1}')
    zip2 = input('Enter the second ZIP Code => ')
    print(zip2)
    # logging.info(f'Received the second ZIP {zip2}')
    logger.info(f'Received the second ZIP {zip2}')

    location1 = location_by_zip(codes, zip1)
    location2 = location_by_zip(codes, zip2)
    if len(location1) == 0 or len(location2) == 0:
        print('The distance between {} and {} cannot be determined'.
              format(zip1, zip2))
    else:
        dist = calculate_distance(location1, location2)
        print('The distance between {} and {} is {:.2f} miles'.
              format(zip1, zip2, dist))


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    rfh = logging.handlers.RotatingFileHandler(
        filename='zip_app.log',
        mode='a',
        maxBytes=5*1024*1024,
        backupCount=9,
        encoding=None,
        delay=0
    )
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                        handlers=[rfh])
    logger = logging.getLogger('main')

    zip_codes = util.read_zip_all()

    command = ""
    while command != 'end':
        command = input("Command ('loc', 'zip', 'dist', 'end') => ")
        # logging.info(f'Received command {command}')
        logger.info(f'Received command {command}')
        print(command)
        command = command.strip().lower()
        if command == 'loc':
            process_loc(zip_codes)
        elif command == 'zip':
            process_zip(zip_codes)
        elif command == 'dist':
            process_dist(zip_codes)
        elif command != 'end':
            print("Invalid command, ignoring")
        print()
    print("Done")
    logging.shutdown()
