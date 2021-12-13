# сериализациz объектов - модуль pickle
# Пример 1.

D = {'a': 1, 'b': 2}
# Чтобы сохранить словарь в файле передадим его непосредственно в функцию модуля pickle

F = open('datafile.pkl', 'wb')

import pickle
pickle.dump(D, F)           # Модуль pickle запишет в файл любой объект
F.close()

# чтение словаря обратно

F = open('datafile.pkl', 'rb')
E = pickle.load(F)          # Загружает любые объекты из файла
print(E)

# Пример 2.

filename = "datafile_pickle.txt"
# список покупок
shoplist = {"фрукты": ["яблоки", "груши"],
            "овощи": ["морковь", "помидоры"],
            "бюджет": 2300}

# Запись в файл
with open(filename, "wb") as fh:
    pickle.dump(shoplist, fh)  # помещаем объект в файл

# Считываем из хранилища
shoplist_2 = []
with open(filename, "rb") as fh:
    shoplist_2 = pickle.load(fh)  # загружаем объект из файла
print(shoplist_2)
