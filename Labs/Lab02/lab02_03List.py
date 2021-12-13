# Списки
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]

# Доступные методы
print(dir(list))
# Справка о методе
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

# Изменение через индексирование
print(list1)
list1[0] = 100
print(list1)
list1.append(0)  # Добавление в конец
print(list1)
list1.insert(1, 0)  # Добавление в индекс 1
print(list1)
list1.remove(0)  # Удаление по значению
print(list1)
element = list1.pop()  # Удаление c конца и возвращает эл
print(list1, element)
del list1[2]  # Удаление по позиции
print(list1)
del list1[2:5]  # Удаление блока по позиции
print(list1)

# Сортировка элементов списка
list1.sort()  # Сортировка
print(list1)
list1.append(0)
list2 = sorted(list1)  # Возвращает отсортированный список не изменяя предыдущий
print("list1", list1)
print("list2", list2)
