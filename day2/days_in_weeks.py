# Calculates how many days , months, years left you have in based on if you lived till [90] now changed based on user
# https://waitbutwhy.com/2014/05/life-weeks.html

current_age = int(input("what is your current age? "))
live_till = int(input("How old do you think you'll live to? "))


age_left = live_till - current_age 


days = 365 * age_left
weeks = 52 * age_left
months = 12 * age_left

print(f"You have {days} days, {weeks} weeks and {months} months left, if you were to live till {live_till} years old.")

          
