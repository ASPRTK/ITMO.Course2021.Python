from FinalTask.model.InfoSubject import InfoSubject
from FinalTask.viev import show


def selectCategory(infoSubjects):
    print("Доступные категории: ", end="")
    setCategorys = set()
    for iSub in infoSubjects.infoSubjects:
        setCategorys.add(iSub.category)
    print(setCategorys)
    category = input('\nУкажите категорию: ')
    show.showCategoryInfoSubjects(infoSubjects, category)


def selectDate(infoSubjects):
    print("Доступные даты: ", end="")
    setDates = set()
    for iSub in infoSubjects.infoSubjects:
        setDates.add(iSub.dateBuy)
    print(setDates)
    dateBuy = input('\nУкажите дату: ')
    show.showDateInfoSubjects(infoSubjects, dateBuy)


def deleteNumber(infoSubjects):
    dateBuy = input('\nВведите номер записи для удаления: ')
    if dateBuy == "end" or dateBuy =="'end'":
        print("Отмена удаления")
    if not dateBuy.isdigit():
        print("ERROR!!!! Для удаление необходимо ввести номер записи")
        print("Для отмены введите 'end'")
        deleteNumber(infoSubjects)
    dateBuy = int(dateBuy)
    print("Удаление", dateBuy, dateBuy+1)



