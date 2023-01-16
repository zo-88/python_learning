# program that checks if the number given is even or odd

should_repeat = True

while should_repeat:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
    
    repeat_answer = input("Do you want to check another number? y/n ").lower()
    if repeat_answer == 'n':
        print("Ok, goodbye")
        should_repeat = False
        
             