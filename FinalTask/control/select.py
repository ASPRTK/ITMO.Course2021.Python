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
