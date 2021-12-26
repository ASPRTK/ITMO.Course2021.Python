from FinalTask.model.InfoSubjectsCSV import InfoSubjectsCSV
from FinalTask.control.createInfoSubject import createInfoSubject
from FinalTask.viev import show

def main():
    while (True):
        show.showMenu()
        infoSubjects = InfoSubjectsCSV()

        valueMenu = input('Введите номер меню: ')
        if valueMenu == "1":
            print("Выбрано 1-Добавить")
            infoSubject = createInfoSubject()
            infoSubjects.add(infoSubject)
            print(infoSubject)
        elif valueMenu == "2":
            print("Выбрано 2-Показать все")
            show.showAllInfoSubjects(infoSubjects)
        elif valueMenu == "3":
            print("Выбрано 3-Показать по дате")
            show.showDateInfoSubjects("2")
        elif valueMenu == "4":
            print("Выбрано 4-Показать по категории")
            show.showCategoryInfoSubjects("Продукты")
        elif valueMenu == "5":
            print("Выбрано 5-Показать по min->max")
        elif valueMenu == "6":
            print("Выбрано 6-Удалить запись")
        elif valueMenu == "0":
            break
            print("Работа приложения завершена")


main()
