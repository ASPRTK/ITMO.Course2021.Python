import numpy # требует установки модуля pip install numpy

def append_if_not_exists(arr, x):
    if x not in arr:
        arr.append(x)
        
def some_useless_slow_function():
    arr = list()
    for i in range(1000):
        x = numpy.random.randint(0, 1000)
        append_if_not_exists(arr, x)
    return arr

mas = sorted(some_useless_slow_function())
print(len(mas),'\n', mas)
  
