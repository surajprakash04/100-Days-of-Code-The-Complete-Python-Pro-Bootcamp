student_scores = [213,245,53,64,35,34,865,356,387,97,76,643,12]

highest_score = 0
itr = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)