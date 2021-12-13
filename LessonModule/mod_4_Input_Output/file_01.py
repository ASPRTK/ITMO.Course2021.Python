dirfile = "D:\\data\\"
myfile = open(dirfile+"myfile.txt", 'w+') # Открывает файл (создает/очищает)
k = myfile.write("hello text file\n") # Записывает строку текста
print(k)  # Python 3.0 метод write возвращает количество записанных символов

myfile.write("goodbye text file\n")
myfile.close()

myfile = open(dirfile+"myfile.txt", 'r') # Открывает файл: ‘r’
content = myfile.read() # Прочитать файл целиком 
print("Содержимое:\n", content) 

myfile.close()

lis = ['Первая строка\n', 'Вторая строка\n', 'Третья строка\n']
myfile = open("myfile.txt", 'a')    # Открывает файл (добавляет)
myfile.writelines(lis)              # Запись всех строк из списка в файл

filename = "myfile2.txt"
names = ['Петя', 'Коля', 'Вася']
f1 = open(filename, 'w')
for it in names:                    # Запись всех строк из списка в файл
    f1.write(it + '\t')
f1.close()

myfile = open(filename, 'r')        # Открывает файл: ‘r’ 
content = myfile.read()             # Прочитать файл целиком в строку
print(content) 
myfile.close()


myfile = open("myfile.txt")         # Открывает файл: ‘r’ – по умолчанию
print(myfile.readline())            # Читает строку

fs = open("myfile.txt").read()      # Прочитать файл целиком в строку
print("--", fs)

# просмотреть содержимое файла строку за строкой
# не используется операция чтения из файла
# файлы имеют итератор, который автоматически читает информацию из файла строку за строкой в контексте цикла for
for lin in open("myfile.txt"):
    print("---", lin, end='')

# Чтение файла целиком в список строк (включая символ конца строки)
fl = open("myfile.txt").readlines()
print(fl)
