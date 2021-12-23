"КОНТРОЛ"
from Labs.Lab06_MVC.lab06_AnsMvc.model.zip_by_location import zip_by_location


def process_zip(codes):
    """
    Запускается по команде 'zip'
    Функция запрашивает у пользователя город и штат и возвращает строку
    с информацией о всех почтовых индексах этого города
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
    :return: Возвращает строку со списком индексов
    """
    city = input('Введите название города для поиска => ')
    print(city)
    city = city.strip().title()
    state = input('Введите название штата для поиска => ')
    print(state)
    state = state.strip().upper()
    zipcodes = zip_by_location(codes, (city, state))

    if len(zipcodes) > 0:
        return ('Найдены следующие почтовые индексы (ZIP Code(s)) для {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))
    else:
        return 'Почтовый индекс (ZIP Code) для {}, {} не найден!'.format(city, state)



