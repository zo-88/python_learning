
#student_scores = [78, 65, 89, 86, 55, 91, 64, 89]


student_scores = input("Enter student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
               

for score in student_scores:
    highest_score = 0
    if highest_score < score:
        highest_score = score
        
print(f"The highest score in the class is: {highest_score}")


# using max function()

score_max = max(student_scores)
print(f"This is the maximum score: {score_max}")
print(f"This is the lowerest score: {min(student_scores)}")