"КОНТРОЛ"
from Labs.Lab06_MVC.lab06_AnsMvc.model.format_location import format_location
from Labs.Lab06_MVC.lab06_AnsMvc.model.location_by_zip import location_by_zip


def process_loc(codes):
    """
    Функция на основе почтового индекса (ZIP Code) осуществляет
    поиск соответствующего ему города и штат
    Отображает результат в виде строки с информацией о найденном городе
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
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


