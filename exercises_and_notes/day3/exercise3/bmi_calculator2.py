# BMI calculator 2.0
''' It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


height = float(height)
weight = float(weight)
bmi = int( weight / (height * height))
# bmi = int(weight/(height ** 2))

intro = "Your BMI is "

if bmi < 18.5:
    print(f"{intro}{bmi}, you're underweight")
elif bmi < 25:
    print(f"{intro}{bmi}, you have a normal weight")
elif bmi < 30:
    print(f"{intro}{bmi}, you're slightly overweight")
else:
    print(f"{intro}{bmi}, you're clinically obese")


