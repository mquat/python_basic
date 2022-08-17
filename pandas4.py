import pandas as pd

#read json file 
df = pd.read_json('data.json')
print(df.to_string())   #print the dataframe

#read csv file
df = pd.read_csv('data.csv')
print(df.to_string())   #print the dataframe

#change the maximum number of rows
#if the dataframe contains more than 200 rows, print(df) will return the headers/the first and last 5 rows
pd.options.display.max_rows = 200   
df = pd.read_csv('data.csv')

#example: if contains 300 rows -> row0, row1, row2, row3, row4 ... row296, row297, row298, row299, row300
print(df)