# Задание 1. Базовое решение

# ! Реализовать класс с конструктором. Определить значения по умолчанию для
# некоторых аргументов, чтобы их можно было не указывать в тех случаях,
# когда какие-то определенные значения недоступны или бессмысленны.
# ! Реализовать с помощью свойств инкапсуляцию.
# ! Добавить в класс методы, определяющие поведение.
# ! Реализовать производные классы (не менее двух) и методы, характерные для них.
# ! Реализовать отношение композиции.
# ! Реализовать для базового класса перегрузку двух любых стандартных
# операторов, например, сложения и вычитания. Методы перегрузки должны
# возвращать новый объект того же класса.

class Person(object):
    def __init__(self, name, surname, age=0):
        """Constructor"""
        self.__name = name.capitalize()
        self.__surname = surname.capitalize()
        self.__age = age

    def __add__(self, other):
        name = self.get_name() + "-" + other.get_name()
        surname = self.get_surname() + "-" + other.get_surname()
        return Person(name, surname)

    def get_age(self):
        return self.__age
    def set_age(self, value):
        if value in range(1, 100):
            self.__age = value
        else:
            print("Недопустимый возраст")
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname

    def get_info(self):
        return "{} {}: Возраст {};".format(self.__name, self.__surname, self.__age)

class Manager(Person):
    def __init__(self, name, surname, nameDepartment, age=0):
        """Constructor"""
        Person.__init__(self, name, surname, age)
        self.__nameDepartment = nameDepartment
    def get_nameDepartment(self):
        return self.__nameDepartment

    def get_info(self):
        return "Менеджер отдела {} - {} {}: Возраст {};"\
            .format(self.get_nameDepartment(), self.get_name(), self.get_surname(), self.get_age())


def main():
    person = Person("Арк", "Дарк", 25)
    print(person.get_info())
    person2 = Person("марк", "Дарк",)
    print(person2.get_info())
    person2.set_age(20)
    print(person2.get_info())
    manager = Manager("Тофу", "Мофу", "магии", 34)
    print(manager.get_info())

    personAdd = person + person2
    print(personAdd.get_info())


main()
