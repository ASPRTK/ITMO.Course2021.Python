"КОНТРОЛ"
def process_zip(codes):
    """
    Функция осуществляет поиск почтовых индексов дя введенных города и штата
    Выводи на консоль список с почтовыми индексами (ZIP Code(s)
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
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


