import pandas as pd
import numpy as np

pd.options.display.max_rows = 100

df = pd.read_csv('NUSW-NB15_GT.csv')
df.drop(['Start time', 'Last time','Source IP','Source Port','Destination Port'], axis=1, inplace=True)

category = df.groupby('Attack category').count()
print(df['Attack category'].value_counts())
print(df['Attack subcategory'].value_counts())


