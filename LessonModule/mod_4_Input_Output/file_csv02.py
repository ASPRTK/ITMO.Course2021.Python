# работа с CSV-файлом в Python (словарь)
import csv

filename = "data_02.csv"

# список покупок
shoplist = {"яблоки": [12, 100], "груши": [31, 250], "морковь": [3, 35]}

# класс csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
# Создает и возвращает объект для записи данных как словаря значений в CSV-файл.

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
    writer.writeheader()                         # Записывает заголовки в файл
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1])) # Записывает словарь row в CSV-файл


# class csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
# Создает и возвращает объект для чтения данных из CSV-файла как словаря значений.

# Чтение файла
rows = []
with open(filename, "r", encoding="utf-8") as fh:
    reader = csv.DictReader(fh)
    rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
    print(row)
