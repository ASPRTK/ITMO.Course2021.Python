import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

filename = 'numbers.json'
f_obj = open(filename, 'w')
json.dump(numbers, f_obj)
f_obj.close()

f_obj = open(filename, 'r')
numbers = json.load(f_obj)
print(numbers)
print(type(numbers))

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

    
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)
