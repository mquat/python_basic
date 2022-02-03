#with : file을 열고 닫는 것을 좀 더 편하게 할 수 있음 

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("열심히 파이썬 공부하고 있어요!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

