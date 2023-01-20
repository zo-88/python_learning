# Guessing number game
import random

# 1: print welcome statement
print("Welcome to the Number Guessing Game!")


# 2: choose difficulty :

game_level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

# 3 assign difficult based on answer

if game_level == 'easy':
    attempts = 10
else:
    attempts = 5
    
#print(attempts)
#print(type(attempts))


# generate a random number

computer_number = random.randint(1,101)

print(computer_number)


def guess_the_number(times, num):
    guessed_number = False
    loser = False
    while times !=0 and guessed_number == False:
        
        guess = int(input("Guess a number: "))
        if guess > num:
            print("too high")
            print("Guess again")
            times -= 1
            print(f"You have {times} attempts left.")
        elif guess < num:
            print("too low")
            print("Guess again")
            times -= 1
            print(f"You have {times} attempts left.")
        elif guess == num:
            print("You won")
            guessed_number = True
    if times == 0:
        print("You lost")
        print("You ran out of lives")
      
            
        
 
 
print(f"You have {attempts} attempts to guess the number.")
guess_the_number(times=attempts, num= computer_number)


    
            