#Order a pizza

pizza_size = input("What size pizza would you like? S/M/L: ").lower()
add_pepperoni = input("Would you like pepperoni on your pizza? Y/N:  ").lower()
extra_cheese  = input("Would you like extra cheese on your pizza? Y/N:  ").lower()

bill = 0

if pizza_size == 's':
    bill += 15
elif pizza_size == 'm':
    bill += 20
else: 
    bill += 25
    
if add_pepperoni == 'y':
    if pizza_size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f"Your final bill is ${bill}")
    
