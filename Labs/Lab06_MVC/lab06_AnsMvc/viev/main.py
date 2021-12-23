import logging

from Labs.Lab06_MVC.lab06_AnsMvc.control.process_dist import process_dist
from Labs.Lab06_MVC.lab06_AnsMvc.control.process_loc import process_loc
from Labs.Lab06_MVC.lab06_AnsMvc.control.process_zip import process_zip
from Labs.Lab06_MVC.lab06_AnsMvc.model.classLogger import myLogger
from Labs.Lab06_MVC.lab06_AnsMvc.model.classModelZipCode import classModelZipCode



def help_print():
    """
    Отображает информацию о командах
    :return:
    """
    print("Command - 'loc' - заращивает почтовы индекс, возвращает город и штат; \n"
          "Command - 'zip' - запрашивает город и штат, возвращает почтовый индекс; \n,"
          "Command - 'dist' - определяет расстояние между двумя почтовыми станциями; \n"
          "Command - 'help' - информация о командах; \n"
          "Command - 'end' - завершение приложение; \n")


def main():
    # logging.basicConfig(level=logging.DEBUG)
    ZC = classModelZipCode()
    command = ""
    while command != 'end':
        command = input("Command ('loc', 'zip', 'dist', 'help', 'end') => ")
        myLogger.info(f'Received command {command}')
        print(command)
        command = command.strip().lower()
        if command == 'loc':
            print(process_loc(ZC.getZipCodes()))
        elif command == 'zip':
            print(process_zip(ZC.getZipCodes()))
        elif command == 'dist':
            print(process_dist(ZC.getZipCodes()))
        elif command == 'help':
            help_print()
        elif command != 'end':
            print("Недопустимая команда!")
        print()
    print("Работа завершена!")
    logging.shutdown()


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    main()
