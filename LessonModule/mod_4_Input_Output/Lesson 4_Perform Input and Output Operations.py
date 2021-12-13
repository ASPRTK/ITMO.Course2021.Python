#!/usr/bin/env python
# coding: utf-8

# # Lesson 4: Perform Input and Output Operations

# ## Working With Files

# ### Запись в файл

# In[55]:


dirfile = "D:\\data\\"    # можете заменить на свой каталог
namefile = dirfile + "myfile.txt"    # полный путь к файлу
myfile = open(namefile, 'w')     # Открывает файл (создает/очищает)
k = myfile.write("hello text file\n")       # Записывает строку текста
print(k)  # Python 3.0 метод write возвращает количество записанных символов
myfile.write("goodbye text file\n")
myfile.close()


# In[48]:


lis = ['Первая строка\n', 'Вторая строка\n', 'Третья строка\n']
myfile = open(namefile, 'a')       # Открывает файл (открытие на дозапись, информация добавляется в конец файла)
myfile.writelines(lis)             # Запись всех строк из списка в файл


# In[51]:


names = ['Петя', 'Коля', 'Вася']
f1 = open(namefile, 'a')
for it in names:          # Запись всех строк из списка в файл
    f1.write(it + '\t')
f1.close()


# ### Чтение из файла

# In[52]:


myfile = open(namefile, 'r') # Открывает файл: ‘r’ - на чтение 
content = myfile.read()      # Прочитать файл целиком в строку
print(content) 
myfile.close()


# In[37]:


myfile = open(namefile)  # Открывает файл: ‘r’ – по умолчанию
print(myfile.readline()) # Читает строку


# In[38]:


fs = open(namefile).read() # Прочитать файл целиком в строку
print(fs)


# In[54]:


# просмотреть содержимое файла строку за строкой
for lin in open(namefile):
    print(lin, end='')


# In[61]:


# Чтение файла целиком в список строк (включая символ конца строки)
fl = open(namefile).readlines()
print(fl)


# ### with ... as - менеджеры контекста

# Конструкция with ... as используется для оборачивания выполнения блока инструкций менеджером контекста

# In[60]:


# Предыдущий пример можно записать с помощью with…as 
# функциональность при этом не изменится
with open(namefile, 'r') as fobj:
    f = fobj.readlines()
    print(f)     


# ### Работа с форматом CSV

# In[62]:


# Read the CSV file using the csv module
import csv
with open('D:\data\input.csv') as csvfile:
    inputcsv = csv.reader(csvfile, delimiter=',')
    for i in inputcsv:
        print(i)


# In[ ]:




