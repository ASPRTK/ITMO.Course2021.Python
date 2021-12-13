human = dict(name="Иван Иванов", age = 25, weight = 83.5)
filename = "Humandata.txt"

# 1. Запись в файл
#    При записи текстовых файлов все данные должны быть преобразованы в тип str
#    По умолчанию, write() не добавляет перенос строки, однако его можно добавить самостоятельно
fh = None
try:
    fh = open(filename, "w", encoding="utf-8")
    # При добавлении переноса записываемые данные будут на отдельной строке
    fh.write(human["name"] + "\n")
    fh.write(str(human["age"]) + "\n")
    # Как альтернатива - print() позволяет не переводить в строку и не добавлять перенос вручную
    print(human["weight"], file = fh) # установить параметр file в открытый файловый объект
finally:
    if fh:
        fh.close()

# 2. Чтение из файла
#    Для чтения отдельной строки достаточно вызвать метод readline().
#    В конце полученной строки знак переноса - \n, который можно убрать методом str.strip()
fh = None
try:
    fh = open(filename, encoding="utf-8")
    # Читаем первые 3 строки и преобразуем при необходимости
    name = fh.readline().strip()
    age = int(fh.readline())
    weight = float(fh.readline())
    print(name, age, weight)  
finally:
    if fh:
        fh.close()
    
