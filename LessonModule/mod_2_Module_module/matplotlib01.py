"""
Библиотека на языке программирования Python для визуализации данных двумерной
(2D) графикой.
Получаемые изображения могут быть использованы в качестве иллюстраций
в публикациях
"""

import matplotlib.pyplot as plt # Импортируем библиотеку 
dt = [5,25,75,55,85,95]

plt.title('Chart Title') 
plt.xlabel('Time') 
plt.ylabel('Price')
plt.legend()

plt.plot(dt)

plt.show() 
