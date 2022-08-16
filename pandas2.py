#Series = a column in a table (one-dimensional array)
#a dict can be also used when creating a Series (The keys become the labels)

import pandas as pd

a = [1, 7, 2]
b = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(a)
myvar = pd.Series(a, index=['x','y','z'])
mycal = pd.Series(b)

print(myvar)
print(myvar[0])     #1 
print(myvar['x'])   #1

print(mycal['day2'])    #380