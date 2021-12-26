from FinalTask.model.InfoSubjectsCSV import InfoSubjectsCSV


def showMenu():
    print("")
    print("1-Добавить")
    print("2-Показать все")
    print("3-Показать по дате")
    print("4-Показать по категории")
    print("5-Показать по min->max")
    print("6-Удалить запись")
    print("0-Завершить работу")


def showAllInfoSubjects(infoSubjects: InfoSubjectsCSV):
    print("\n - - - - ->  Список покупок")
    print("Категория; \t\t\tНазвание; \t\t\tЦена; \t\t\tДата;")
    for iSub in infoSubjects.infoSubjects:
        print(iSub.getStrTupleT())


def showDateInfoSubjects(infoSubjects, dateBuy):
    print("\n - - - - ->  Список покупок на дату: {} ".format(dateBuy))
    print("Категория; \t\t\tНазвание; \t\t\tЦена; \t\t\tДата;")
    for iSub in infoSubjects.infoSubjects:
        if iSub.dateBuy == dateBuy:
            print(iSub.getStrTupleT())


def showCategoryInfoSubjects(infoSubjects, category):
    print("\n - - - - ->  Список покупок для категории: {}".format(category))
    print("Категория; \t\t\tНазвание; \t\t\tЦена; \t\t\tДата;")
    for iSub in infoSubjects.infoSubjects:
        if iSub.category == category:
            print(iSub.getStrTupleT())