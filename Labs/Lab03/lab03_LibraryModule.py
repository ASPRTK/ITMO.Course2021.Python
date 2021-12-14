# Практическое занятие 3. Работа с модулями стандартной библиотеки

# Обработка модулей выполняется двумя инструкциями:
# import – позволяет клиентам (импортерам) получать модуль целиком.
# from – позволяет клиентам получать определенные имена из модуля.
import math
import statistics

# 1. С помощью справочной информации изучите состав модулей math и
# statistics.
# help(math)
# help(statistics)

# 2. Напишите программу, в которой создайте список из десяти целых чисел.
import random


def createList():
    myList = []
    for i in (range(0, 10)):
        myList.append(random.randint(20, 50))
    return myList


mylist = createList()
print(mylist)

# 3. Затем реализуйте подсчет суммы чисел списка, среднего значения,
# медианы (median) и стандартного отклонения (stdev), предварительно
# импортировав соответствующие модули.
print("Сумма чисел списка", sum(mylist))
print("Медиана списка", statistics.median(mylist))
print("Стандартное отклонение списка", statistics.stdev(mylist))

# 4. Реализуйте программу, в которой генерируется случайное число на
# интервале от 1 до 100. Для генерации числа используйте функцию randint
# модуля random.
randomValue = random.randint(1, 100)
print(randomValue)
