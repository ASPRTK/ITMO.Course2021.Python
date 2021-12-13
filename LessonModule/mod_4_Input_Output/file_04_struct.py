# модуль struct позволяет сохранять и восстанавливать упакованные двоичные данные
import struct
# упаковка в байты
dat1 = struct.pack("hhl", 1, 2, 3) # первое и второе числа трактуются как тип short int, а третье, как long int
print(dat1) # b'\x01\x00\x02\x00\x03\x00\x00\x00'

# размер объекта dat1
size = struct.calcsize('hhl') # size = 8
print('size = ', size)

# распаковка байт в кортеж значений по заданному формату:
tup1 = struct.unpack("hhl", dat1)
print(tup1)

F = open('data.bin', 'wb') # Открыть файл для записи в двоичном режиме

data = struct.pack("<2h", 7,11) # Создать пакет двоичных данных - little-endian (<) порядок от младшего байта к старшему и h повторяется дважды
print(data)

F.write(data) # Записать строку байтов
F.close()

# извлечение значений, преобразуя их в обычные объекты

F = open('data.bin', 'rb')
data = F.read() # Получить упакованные двоичные данные
print(data)

values = struct.unpack('<2h', data) # Преобразовать в объекты
print(values)

# работа со строками

# Для строк код «s» надо указывать число байт – длину строки, иначе будет считаться 1 байт:
print(struct.pack("ss", b"abc", b"XYZW"))  # не указал длину - потерял байты - b'aX'
print(struct.pack("3s4s", b"abc", b"XYZW")) # b'abcXYZW'

#10s – одна 10-символьная строка, а 10c – 10 отдельных символов:
print(struct.unpack('10c', b'abracadabr')) # (b'a', b'b', b'r', b'a', b'c', b'a', b'd', b'a', b'b', b'r')
print(struct.unpack('10s', b'abracadabr')) # (b'abracadabr',)

# Пробелы игнорируются при чтении строки и нужны для удобства чтения кода программистом:
print(struct.pack('>6sh?', b'python', 65, True)) # b'python\x00A\x01'
print(struct.pack('> 6s h ?', b'python', 65, True))  # тоже, но с пробелами b'python\x00A\x01'
print(struct.unpack('> 6s h ?', b'python\x00A\x01')) # (b'python', 65, True)


# Удобно распаковывать байты прямо в именованные кортежи:
from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
record = b'raymond   \x32\x12\x08\x01\x08'
print(Student._make(struct.unpack('<10sHHb', record)))
# Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)






