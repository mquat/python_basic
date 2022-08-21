#Dataframe (Each Series is like a column, multi-dimensional tables)

import pandas as pd

data = {
    'country' : ['Korea','Thailand','France'],
    'capital' : ['Seoul','Bangkok','Paris']
}

myvar = pd.DataFrame(data)
print(myvar)

#or, can load the JSON file
#JSON file has the same format as Python dictionaries
df = pd.read_json('data.json')
print(df.to_string())