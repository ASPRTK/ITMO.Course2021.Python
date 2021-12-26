from FinalTask.viev import show

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
    index = input('\nВведите номер записи для удаления: ')
    if index == "end" or index == "'end'":
        print("Отмена удаления")
    if not index.isdigit():
        print("ERROR!!!! Для удаление необходимо ввести номер записи")
        print("Для отмены введите 'end'")
        deleteNumber(infoSubjects)
    index = int(index) - 1
    print(infoSubjects.deleteIndex(index))


def sortedMinMax(infoSubjects):
    print("")
    print("1-Сортировка по категории")
    print("2-Сортировка по названиям")
    print("3-Сортировка по ценам")
    print("4-Сортировка по датам")
    index = input('Выберите вид сортировки: ')
    if index == '1':
        copy = sorted(infoSubjects.infoSubjects, key=sortedByCategory)
        show.showAllCopyList(copy)
    if index == '2':
        copy = sorted(infoSubjects.infoSubjects, key=sortedByProduct)
        show.showAllCopyList(copy)
    if index == '3':
        try:
            copy = sorted(infoSubjects.infoSubjects, key=sortedByCost)
            show.showAllCopyList(copy)
        except ValueError:
            print("сортировка по ценам не возможна, так одна из цен не число!")
    if index == '4':
        copy = sorted(infoSubjects.infoSubjects, key=sortedByData)
        show.showAllCopyList(copy)


def sortedByCategory(infoSubject):
    return infoSubject.category


def sortedByProduct(infoSubject):
    return infoSubject.product


def sortedByCost(infoSubject):
    if infoSubject.cost:
        return int(infoSubject.cost)
    return infoSubject.cost


def sortedByData(infoSubject):
    return infoSubject.dateBuy
