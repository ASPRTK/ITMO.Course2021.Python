human = dict(name="Иван Иванченко", age = 25, weight = 83.5)
filename = "HumandataBin.txt"

# 1. Запись в файл
#    При записи бинарных файлов все данные должны быть преобразованы в тип bytes
#    Удобно выполнить преобразование через метод str.encode()
fh = None
try:
    fh = open(filename, "wb")
    fh.write(bytes(human["name"].encode("utf-8")))
    fh.write(bytes(str(human["age"]).encode("utf-8")))
    fh.write(bytes(str(human["weight"]).encode("utf-8")))
finally:
    if fh:
        fh.close()

# 2. Чтение из файла
#    При чтении бинарных файлов необходимо точно знать, сколько байт
#    прочитать и как их декодировать, используя bytes.decode()
#    При редактировании файла в стороннем редакторе файл может быть не читаем
fh = None
try:
    fh = open(filename, "rb")
    name = fh.read(27).decode("utf-8")
    age = int(fh.read(2).decode("utf-8"))
    weight = float(fh.read(4).decode("utf-8"))
    print(name, age, weight)  
finally:
    if fh:
        fh.close()
    
