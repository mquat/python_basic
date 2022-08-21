import pandas as pd

df = pd.read_csv('data.csv')

#information of the data
print(df.info())

#quick overview of the DataFrame : head() 
print(df.head(10))  #print the first 10 rows
print(df.head())    #print the first 5 rows 
print(df.tail())    #print the last 5 rows 