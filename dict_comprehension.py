incorrect_score = {'jason':80, 'emma':75, 'sam':90}

correct_score = {name:score+5 for (name,score) in incorrect_score.items() if score<80}
print(correct_score)

