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
