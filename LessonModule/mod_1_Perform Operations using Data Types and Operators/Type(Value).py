""" Типы данных """

p1 = 65          # число  - целое
print(type(p1))         # <class 'int'>
p1 = 76.87
p2 = 65.0        # число - вещественное
s1 = "Текст"     # текст
print(type(s1)) 
s1 = 58
b1 = True        # логический (булевый)
a = [8, 7, 5.5, 1000, 3.50, 200]

print(p1, p2, s1, b1)   # 65 65.0 Текст True
print(type(p1))         # <class 'int'>
print(type(p2))         # <class 'float'>
print(type(s1))         # <class 'str'>
print(type(b1))         # <class 'bool'>
print(type(a))

# при сложении целого и вещественного, какой получится тип?
p3 = p1 + p2
print(type(p3), p3)

# а если сложить строу и число?
param1 = "string" + str(15)

# а если сложить чисто и строку?
param2 = 15 + int("25")

print(param2)
