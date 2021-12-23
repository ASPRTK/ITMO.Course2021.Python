" ????????"
"МОДЕЛЬ"
def location_by_zip(codes, zipcode):
    """
    Функция проверяет есть ли введеный пользователем код в списке почтовх индексов
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
    :param zipcode: Почтовый индекс ввведеный пользоваетлем
    :return: Возвращает кортеж tuple(code[1:]) с информацие о локации с данным почтовым адреосом
    """
    for code in codes:
        if code[0] == zipcode:
            return tuple(code[1:])
    return ()

