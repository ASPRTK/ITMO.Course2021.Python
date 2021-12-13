"""
NumPy — это библиотека с открытым исходным кодом,
 предназначенная для обработки многомерных массивов и матриц
Центральным элементом в библиотеке является однородный
(состоящий из элементов одного типа) многомерный массив,
представленный классом ndarray
"""
import numpy as np # Импортируем библиотеку NumPy

# работа с массивами

lst = [7, 8]
arrlst = np.array(lst) # массив-вектор на основе списка
""" функция array() принимает любую последовательность элементов """
print("массив-вектор на списке: ", arrlst)

array1 = np.arange(10) # вектор из целых чисел от 0 до 9
""" функция arange() создает массив на основе числовой последовательности"""
array2 = np.arange(5, 15)
array3 = np.arange(1, 5, 0.5)
print("массивы на range:\n", array1,"\n", array2,"\n", array3)

arr1 = array1*2
arr2 = array1*array2
print("array1*2:\n", arr1,"\narray1*array2:\n", arr2)
print("Применение функции 'sin' к элементам массива:\n", np.sin(array1)) # функции numpy
print("Применение функции 'sum' к элементам массива:\n", np.sum(array1))
print("Исходный массив 'array1':\n", array1)
print("Применение функции 'mean' к массиву:", array1.mean()) # функции массива


nd_array = np.array([[1,2],
                    [3,4]])
print("Двумерный массив:\n", nd_array)
print("Количество элементов:", nd_array.size)

nd_array2 = np.array([[5,6],
                    [7,8]])
print("Еще Двумерный массив:\n", nd_array2)
nd_arrayS = nd_array + nd_array2
print("Операция '+' с двумерными массивами:\n", nd_arrayS)


# работа с матрицами

"""
np.matrix()
Matrix является удобным инструментом для задания матрицы.
При этом можно передать в качестве аргумента список Python или массив Numpy.
"""
a = [[1, 2], [3, 4]] # список в качестве основы для матрицы
matr1 = np.matrix(a)
print("Матрица:\n", matr1)

matr11 = np.matrix('[1, 2; 3, 4]') # создание в 'Matlab' стиле
#print("Матрица:\n", matr11)

m = np.array([[5, 6], [7, 8]]) #  на основе массива numpy
matr2 = np.matrix(m)
print("Матрица:\n", matr2)

m1m2 = matr1 + matr2 # Сложение матриц
m1m2 = matr1 - matr2 # Вычитание  матриц
m1k = matr1 * 7      # Умножение матрицы на число
m1m2 = matr1*matr2   # Умножение матриц
m1m2 = matr1.dot(matr2)
print("Сумма матриц:\n", m1m2)
print("Умножение матрицы на 7:\n", m1k)

m1T = matr1.T  # Транспонирование матриц
m2T = np.transpose(matr2)
print("Исходная матрица:\n", m1T, "\nЕе транспонирование:\n", m2T)

arWhere = np.where(array1 % 2 == 0, array1 * 10, array1 / 10) # функция возвращает один из двух заданных элементов в зависимости от условия
print(arWhere) # четные элементы умножает на 10, нечетные делит на 0

# Пример реализации обработки данных с помощью пороговой функции.
a = np.random.rand(10)
print(a)
ap1 = np.where(a > 0.95, True, False)
print(ap1)
ap2 = np.where(a > 0.95, 1, -1)
print(ap2)

import matplotlib.pyplot as plt
plt.title('Stock Prices of Largest Software Companies')
plt.xlabel('Dates')
plt.ylabel('Stock Price')
plt.plot(array1, array2, color="r", marker="*", linestyle="none")
plt.show()


