import re

txt = 'Hi! My name is Emma. Call me at 1111111.'
pattern = 'number'
re_search = re.search('Call', txt)
re_findall = re.findall('name', txt)

print(re_search)
print(re_findall)

