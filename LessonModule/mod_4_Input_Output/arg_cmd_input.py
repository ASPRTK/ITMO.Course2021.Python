from sys import argv # Модуль sys позволяет работать с аргументами скрипта с помощью argv

filename = argv[1]  # первый параметр - имя файла
names = argv[2:]    # остальные параметры

f1 = open(filename, 'w')
for it in names:                    # Запись всех параметров из списка в файл
    f1.write(it + '\t')
f1.close()

with open(filename, 'r') as fobj:
    content = fobj.readline()             # Читает содержимое как строку
    print(content)  


## В командной строке запустить файл, например, находящийся в папке D:\data и передать параметры:
##   имя текстового файла: D:\data\test.txt для сохранения данных
##   и сами данные через пробел: Polo Dolo Bolo Molo
##
## Например:
## C:\Users\niko> python D:\data\arg_cmd_input.py D:\data\test.txt Polo Dolo Bolo Molo
## Результат вывода:
## Polo    Dolo    Bolo    Molo

