# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello, World!")
a = 5
a = a + 3
print('a', a)

a = 5
b = a + 7
print('b', b)
import time

delay = 3
a = int(input())
print(a ** 2)
time.sleep(delay)
# Теперь после выполнения программы окно консоли замирает на
# указанное в переменной delay время (3 секунды).


import math

help(math)  # help – посмотрите справочную информацию для модуля math:
print(dir(math))  # dir - набор методов объекта
help(math.sqrt)

list1 = [82, 8, 23, 97, 92]
dir(list1)
help(list1.insert)
