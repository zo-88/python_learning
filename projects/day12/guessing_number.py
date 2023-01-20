# Guessing number game
import random

logo = '''
   ___                          _____  _                 __                    _                 
  / _ \ _   _   ___  ___  ___  /__   \| |__    ___    /\ \ \ _   _  _ __ ___  | |__    ___  _ __ 
 / /_\/| | | | / _ \/ __|/ __|   / /\/| '_ \  / _ \  /  \/ /| | | || '_ ` _ \ | '_ \  / _ \| '__|
/ /_\\ | |_| ||  __/\__ \\__ \  / /   | | | ||  __/ / /\  / | |_| || | | | | || |_) ||  __/| |   
\____/  \__,_| \___||___/|___/  \/    |_| |_| \___| \_\ \/   \__,_||_| |_| |_||_.__/  \___||_|   
                                                                                                 
'''

# 1: print welcome statement
print(logo)
print("Welcome to the Number Guessing Game!")
#2 pick random number 
computer_number = random.randint(1,101)
print(f"answer is {computer_number}")


# 2: choose difficulty and assign difficulty :

game_level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

if game_level == 'easy':
    attempts = 10
else:
    attempts = 5
    
#print(attempts)
#print(type(attempts))




def guess_the_number(times, num):
    guessed_number = False
    loser = False
    while times !=0 and guessed_number == False:
        
        guess = int(input("Guess a number: "))
        if guess > num:
            print("Too high")
            print("Guess again")
            times -= 1
            print(f"You have {times} attempts left.")
        elif guess < num:
            print("Too low")
            print("Guess again")
            times -= 1
            print(f"You have {times} attempts left.")
        elif guess == num:
            print(f"You won! The answer is {num}")
            guessed_number = True
    if times == 0:
        print("You lost")
        print("You ran out of lives")
      
            
        
 
 
print(f"You have {attempts} attempts to guess the number.")
guess_the_number(times=attempts, num= computer_number)


    
            