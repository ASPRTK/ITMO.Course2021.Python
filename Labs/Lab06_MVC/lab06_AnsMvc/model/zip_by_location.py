"МОДЕЛЬ"
def zip_by_location(codes, location):
    """
    Функция проверяет существует ли локация в списке
    и возвращает зип коды для это локации
    :param codes: Принимает список кодов прочитаны из файла zip_codes_states.csv
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
