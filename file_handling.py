#Assume that file 'test.txt' includes below texts
"""
test.txt 

Hello! 
Welcome to the world of Python.
Good luck!
"""

#create a new file (1)
f = open("test.txt", "x")

#create a new file (2) - create a new file with writing mode
f = open("myfile.txt", "w") 

#open the file
f = open("test.txt", "r")   #r: opens a file for reading (default)
print(f.read())

#write the file
f = open("test.txt", "a")   #a: append to the end of the file 
#f = open("test.txt", "w")  #w: overwrite any existing content
f.write("Now we are ready for studying Python!")
f.close()

#delete the file 
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("This file does not exist!")
