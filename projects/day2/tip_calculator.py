#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this


print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? €"))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15: "))
people = int(input("How many people to split the bill? "))


# Calculate tip amount per person
percentage = float(percentage / 100 + 1) 
total_bill = round(bill * percentage,2)
per_person = round(total_bill/people,2)

#print amount per person including tip

print(f"Each person should pay: €{per_person}")


