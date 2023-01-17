# count how many times true love appears in 2 names

name1 = input("enter first name: ").lower()
name2 = input("enter second person's name? ").lower()




combined_names = name1 + name2

love_sum = 0
true_sum = 0


true_sum += combined_names.count('t')
true_sum += combined_names.count('r')
true_sum += combined_names.count('u')
true_sum += combined_names.count('e')

love_sum += combined_names.count('l')
love_sum += combined_names.count('o')
love_sum += combined_names.count('v')
love_sum += combined_names.count('e')




love_score = str(true_sum) + str(love_sum)
print(love_score)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}%, you are alright together.")
else:
    print(f"Your score is {love_score}%")



    
    