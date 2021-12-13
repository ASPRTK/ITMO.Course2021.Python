# This script will create an "Employee Table" with randomized employee names and hire dates and export to a CSV file.
# Change the rows variable to control the number of rows exported.

import names, random, datetime, numpy as np, pandas as pd, time, string, csv
rows = 100
id = np.array(range(1,101))
lastname = np.array([''.join(names.get_last_name()) for _ in range(rows)])
firstname = np.array([''.join(names.get_first_name()) for _ in range(rows)])
nowdate = datetime.date.today()
hiredate = np.array([nowdate - datetime.timedelta(days=(random.randint(30,180))) for _ in range(rows)])
hiretime = np.array([str(random.randint(7,20)) + ':' + str(random.randint(0,59)) + ':00' for _ in range(rows)])

# Функция zip объединяет в кортежи элементы из последовательностей переданных в качестве аргументов
inputzip = zip(id,lastname,firstname,hiredate,hiretime) 
print(inputzip)

inputlist = list(zip(id,lastname,firstname,hiredate,hiretime))
print(inputlist)

df = pd.DataFrame(inputlist)
#df = pd.DataFrame(inputzip)

df.to_csv('input_m.csv',index=False,header=["ID","LastName","FirstName","HireDate","HireTime"])

print(df)
