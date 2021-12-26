from FinalTask.model.InfoSubjectsCSV import InfoSubjectsCSV
from FinalTask.model.InfoSubjectsCSV import custom_key
from FinalTask.control.createInfoSubject import createInfoSubject
from FinalTask.viev import show
from FinalTask.control import select

def main():
    infoSubjects = InfoSubjectsCSV()
    while (True):
        show.showMenu()
        valueMenu = input('Введите номер меню: ')
        if valueMenu == "1":
            infoSubject = createInfoSubject()
            infoSubjects.add(infoSubject)
            print(infoSubject)
        elif valueMenu == "2":
            show.showAllInfoSubjects(infoSubjects)
        elif valueMenu == "3":
            select.selectDate(infoSubjects)
        elif valueMenu == "4":
            select.selectCategory(infoSubjects)
        elif valueMenu == "5":

            print("Выбрано 5-Показать по min->max")

            copy = sorted(infoSubjects.infoSubjects, key=custom_key)
            for iSub in copy:
                print("\t", iSub.getStrTupleT(), sep="")


        elif valueMenu == "6":
            select.deleteNumber(infoSubjects)
        elif valueMenu == "0":
            break
            print("Работа приложения завершена")


main()
