#
# ## Кортежи
print(dir(tuple))
help(tuple.index)
help(tuple.count)

seq = (2, 8, 23, 97, 92, 44, 17, 8, 39, 11, 12)
print(seq)
print("seq.count(8)", seq.count(8))  # количество 8к
print("seq.index(8)", seq.index(44))  # индекс 8ки
listseq = list(seq)  # Кортеж преобразован в список
print(listseq)
print("type(listseq)", type(listseq))

#
# ## Словари
print("\nСловари")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D)
D['food']
D['quantity'] += 10
print(D)
dp = {}  # Пустой словарь

# Добавим значение в словарь
decKey = input("Enter the key: ")
decValue = input("Enter the value: ")
D[decKey] = decValue
print(D)

#
# ## Вложенность хранения данных
rec = {
    "name": {"firstname": "Bob", "lastname": "Smith"},
    "job": ["dev", "mgr"],
    "age": 25
}

print(rec)
print("firstname", rec["name"]["firstname"])
print("lastname", rec["name"]["lastname"])
rec["job"].append("janitor")
print(rec)