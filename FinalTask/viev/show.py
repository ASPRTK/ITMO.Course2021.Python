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

def hederTable(textName):
    print(textName)
    print("N\tКатегория; \t\t\tНазвание; \t\t\tЦена; \t\t\t\tДата;")


def showAllInfoSubjects(infoSubjects: InfoSubjectsCSV):
    hederTable("\n - - - - ->  Список покупок")
    count = 0
    for iSub in infoSubjects.infoSubjects:
        count+=1
        print(count,"\t",iSub.getStrTupleT(), sep="")


def showDateInfoSubjects(infoSubjects, dateBuy):
    hederTable("\n - - - - ->  Список покупок на дату: {} ".format(dateBuy))
    count = 0
    for iSub in infoSubjects.infoSubjects:
        if iSub.dateBuy == dateBuy:
            count += 1
            print(count, "\t", iSub.getStrTupleT(), sep="")


def showCategoryInfoSubjects(infoSubjects, category):
    hederTable("\n - - - - ->  Список покупок для категории: {}".format(category))
    count = 0
    for iSub in infoSubjects.infoSubjects:
        if iSub.category == category:
            count += 1
            print(count,"\t", iSub.getStrTupleT(), sep="")