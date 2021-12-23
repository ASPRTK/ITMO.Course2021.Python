"КОНТРОЛ"


from Labs.Lab06_MVC.lab06_AnsMvc.model.calculate_distance import calculate_distance
from Labs.Lab06_MVC.lab06_AnsMvc.model.classLogger import myLogger
from Labs.Lab06_MVC.lab06_AnsMvc.model.location_by_zip import location_by_zip


def process_dist(codes):
    """
    Функция определяет расстояние между двумя города
    Требует ввести пользователя почтовый индекс двух точек
    Выводи на консоль строку с расстоянием
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
    """
    # logging.basicConfig(level=logging.DEBUG)
    zip1 = input('Введите первый почтовый индекс (ZIP Code) => ')
    print(zip1)
    # logging.info(f'Received the first ZIP {zip1}')
    myLogger.info(f'Received the first ZIP {zip1}')
    zip2 = input('Введите второй почтовый индекс (ZIP Code) => ')
    print(zip2)
    # logging.info(f'Received the second ZIP {zip2}')
    myLogger.info(f'Received the second ZIP {zip2}')

    location1 = location_by_zip(codes, zip1)
    location2 = location_by_zip(codes, zip2)
    if len(location1) == 0 or len(location2) == 0:
        print('Расстояние между {} и {} не может быть определено'.
              format(zip1, zip2))
    else:
        dist = calculate_distance(location1, location2)
        print('Расстояние между {} и {} составляет {:.2f} мили'.
              format(zip1, zip2, dist))
