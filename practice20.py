#pickle : 파일 형태로 저장해주는 것 

import pickle
profile_file = open("profile.pickle", "wb")    #pickle에서는 바이너리를 같이 명시해줘야 하며(wb), encoding은 따로 명시하지 않는다
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file)  #profile에 있는 정보를 profile_file에 저장해라 
profile_file.close()

profile_file2 = open("profile.pickle", "rb") 
profile2 = pickle.load(profile_file2) #file에 있는 정보를 Profile 에 불러오기 
print(profile2)
profile_file.close()

