#Control flow if/ else statements and conditional operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("Can ride")
  age = int(input("what is your age? "))
  if age < 12:
      print("Child tickets are $5")
      bill = 5
  elif age <= 18:
      print("Youth tickets are $7")
      bill = 7
  else:
      print("Adult tickets are $12")
      bill = 12
      
      
  wants_photo = input("Would you like a photo? Y/N: ").lower()
  if wants_photo == 'y':
      bill += 3
  
  print(f"Your final bill is ${bill}")

 
      
      
else:
  print("can't ride")
