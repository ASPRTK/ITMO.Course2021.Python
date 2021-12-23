"КОНТРОЛ"
from Labs.Lab06_MVC.lab06_AnsMvc.model.format_location import format_location
from Labs.Lab06_MVC.lab06_AnsMvc.model.model_location_by_zip import model_location_by_zip


def process_loc(codes):
    """
    Функция запрашивает у пользователя почтовый адрес
    и возвращает строку с городом и штатом
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
    Отображает результат на основе введенных данных
    :return: Возвращает строку с городом и штатом
    """
    zipcode = input('Введите почтовый индекс (ZIP Code) для поиска => ')
    print(zipcode)
    location = model_location_by_zip(codes, zipcode)
    if len(location) > 0:
        'Почтовый индекс {} находится в {}, {}, округ {},'
        return ('Почтовый индекс {} находится в {}, {}, округ {},'.
              format(zipcode, location[2], location[3], location[4],
                     format_location((location[0], location[1]))))
    else:
        return 'Неверный или неизвестный почтовый индекс'


