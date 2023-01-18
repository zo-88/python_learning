# using random module and len() function
import random

people = ['Angela', 'Ben', 'Jenny', 'Micheal', 'Chloe']

random_index = random.randint(0, len(people)- 1)



person = people[random_index]

print(f"{person} is going to buy the meal today!")

