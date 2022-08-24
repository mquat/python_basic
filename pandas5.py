import pandas as pd

df = pd.read_csv('data.csv')

# remove rows which have cells with empty values
# then dropna() returns a new dataframe 
new_df = df.dropna()
print(new_df.to_string())

#if you want to change the original dataframe, then use inplace = True
df.dropna(inplace = True)

#replace an empty cell with a value
df.fillna(130, inplace = True)

#replace a designated cell with a value
df['calories'].fillna(130, inplcae = True)