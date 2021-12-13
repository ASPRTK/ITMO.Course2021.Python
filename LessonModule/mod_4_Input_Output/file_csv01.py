# работа с CSV-файлом в Python (последовательность)
import csv

filename = "data_01.csv"

# список покупок
shoplist = {"яблоки": [12, 100], "груши": [31, 250], "морковь": [3, 35]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as fh:
    writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
    writer.writerow(["Наименование", "Вес", "Цена/кг."])  # Заголовки столбца
    for name, values in sorted(shoplist.items()):
        writer.writerow([name, *values])
    writer.writerow(["рис", "4", "70"])  # Допишем произвольную запись

# Чтение файла
rows = []
with open(filename, "r", encoding="utf-8") as fh:
    reader = csv.reader(fh)
    rows = list(reader)   # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
    print(row)
