# Задание 2. Исключения
# ! Реализуйте в своем проекте поддержку исключений.
# ! Создайте в своем проекте классы исключений и покажите их применение.
# ! Предложите в вашей процедуре (любой на ваш выбор) реализацию возбуждения
# исключения в случае нахождения некого соответствия вместо того, чтобы
# возвращать флаг состояния, который должен интерпретироваться вызывающей
# программой, т.е. с помощью исключения обеспечить способ подачи сигнала,
# не возвращая значение.
import random


class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class ValueTooSmallError(Error):
    """Вызывается, когда входное значение мало"""
    pass


class ValueTooLargeError(Error):
    """Вызывается, когда входное значение велико"""
    pass


def main():
    number = random.randint(1, 10)
    count = 0
    while True:
        count += 1
        try:
            i_num = int(input("Загадано число от 1 до 10: "))
            if i_num < number:
                raise ValueTooSmallError
            elif i_num > number:
                raise ValueTooLargeError
            break
        except ValueTooSmallError:
            print("Попробуйте число больше!\n")
        except ValueTooLargeError:
            print("Попробуйте число меньше!\n")

    step = ""
    if count==1:
        step = "шаг"
    elif count<=5:
        step = "шага"
    elif count<=20:
        step = "шагов"

    print("Вы угадали число {} за {} {}.".format(number, count, step))


if __name__ == "__main__":
    main()
