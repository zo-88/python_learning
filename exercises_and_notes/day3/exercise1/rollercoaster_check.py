#Control flow if/ else statements and conditional operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("Can ride")
  age = int(input("what is your age? "))
  if age < 12:
      print("Your ticket is $5")
  elif age <= 18:
      print("Your ticket is $7")
  else:
      print("Your ticket is $12")
else:
  print("can't ride")
