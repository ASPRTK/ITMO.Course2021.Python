
# Работа со строками
string1 = " This is a string."
string2 = "This is another string."
print(string1)
print(string2)
string3 = string1 + " " + string2
print(string3)

# Функции принимые к строке
print("len()", len(string3)) # len() - определяет длину строки;
print("title()", string3.title()) # title() - преобразует первый символ каждого слова в строке к верхнему регистру;
print("lower()", string3.lower()) # lower() - символы строки преобразуются к нижнему регистру;
print("upper()", string3.upper()) # upper() - символы строки преобразуются к верхнему регистру;
print("rstrip()", string3.rstrip()) # rstrip() – удаляются пробелы в конце строки;
print("lstrip()", string3.lstrip()) # lstrip() – удаляются пробелы в начале строки;
print("lstrip()", string3.strip()) # strip() - удаляются пробелы с обоих концов;
print("strip('0')", string3.strip('0')) # strip('0') - удаляются с обоих концов указанные символы в параметре функции.

# Извлечение символов и подстрок
print("\nИзвлечение символов и подстрок")
d = "qwerty"
ch = d[2] # извлекается символ ‘e’
print("ch", ch)
chm = d[1:3]
print("chm", chm)
print("d[1:], d[:3], d[:], d[1:5:2]")
print(d[1:], d[:3], d[:], d[1:5:2])
