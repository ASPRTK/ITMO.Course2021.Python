a = 1
b = 2
a = a + b
print(a, type(a))
c = "start"
d = 'end'
# a = a + c # TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = d
a = a + c
print(a, type(a))

