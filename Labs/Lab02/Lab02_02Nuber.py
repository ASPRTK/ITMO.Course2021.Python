# Работа с числами

#param = "string" + 15 #  не выполнимая операция
# Не выполняется автоприведение

# Преобразование данных
param = "string" + str(15)
print("param", param)

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)

# Форматирование строк
a = 1/3
print("a", a)
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))


