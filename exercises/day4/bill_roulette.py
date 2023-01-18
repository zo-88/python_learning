# using random module and len() function
import random

print("lets play bill roulette, let's see who's going to pay the bill")
name = input("Enter everyone's name separated by a comma: ")


names = name.split(', ')

#print(names)


#random_index = random.randint(0, len(names)- 1)


#person_picked = names[random_index].capitalize()
#using random choice() function instead

person_picked = random.choice(names).capitalize()

print(f"{person_picked} is going to buy the meal today!")

