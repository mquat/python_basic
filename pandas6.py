#mean = the average value 
#median = the value in the middle, after sorting all values ascending
#mode = the value that appears most frequently

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()
y = df["Calories"].median()
z = df["Calories"].mode()

df["Calories"].fillna(y, inplace=True)