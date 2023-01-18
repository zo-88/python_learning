rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random 
images = [rock,paper,scissors]

random_index = random.randint(0,len(images)-1)

computer_choice = random_index
#print(computer_choice)

user_choice = int(input("Pick 0:Rock , 1:Paper , 2: Scissors: "))

#  print choices
print(f"\nYou chose:\n{images[user_choice]}")
print(f"\n Computer chose:{images[random_index]}")


if computer_choice == user_choice:
  print("It's a draw")
elif computer_choice > user_choice:
  print("Computer wins")
else:
  print("You win")
