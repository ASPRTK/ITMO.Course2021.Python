import pandas as pd
fixed_df = pd.read_csv('d:/data/bikes.csv',  # Это то, куда вы скачали файл
                       sep=';', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
fixed_df[:3]

#print(fixed_df)
print(fixed_df['Berri 1'][:10])
