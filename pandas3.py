#Dataframe (Each Series is like a column, multi-dimensional tables)

import pandas as pd

data = {
    'country' : ['Korea','Thailand','France'],
    'capital' : ['Seoul','Bangkok','Paris']
}

myvar = pd.DataFrame(data)
print(myvar)