sample = [1, 2, 3] 
a = [8, 7, 5.5, 1000, 3.50, 200]
mylist = ["List item 1", 2, 3.14]

dd = [ [sample], [a], [mylist] ]
dd = [ sample, a, mylist ]
print(dd)
dd[1][2] = 34
print(dd)

ddd = list(zip(sample, a, mylist))
'''
zip()  возвращает итератор кортежей, где i-й кортеж содержит i-й элемент
из каждой последовательности аргументов или итераций'''

print(ddd)
ddd[1][2] = 34
print(ddd[0][2][3])
