import names, random, numpy as np
help(names)

rows = 10
id = np.array(range(1,11))

lastname = np.array([''.join(names.get_last_name()) for _ in range(rows)])
firstname = np.array([''.join(names.get_first_name()) for _ in range(rows)])

print('firatname:\n', firstname, '\nlastname:\n', lastname)

lastn = names.get_last_name()
firstn = names.get_first_name()

print("\n", lastn, firstn)
