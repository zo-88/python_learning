word_list = ["ardvark", "baboon", "camel"]

#step 1
import random

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list) -1 )]
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if guess in chosen_word:
    print(f"{guess} is in {chosen_word}")
    