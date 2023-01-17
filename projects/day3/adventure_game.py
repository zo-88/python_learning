#Choose your adventure -- if , elif and else statements

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

end = 'GAME OVER'

left_or_right = input("You've come to a spilt path, choose right to enter the swamp or left to enter the dark forrest L/R? ").lower()

if left_or_right == 'l':
    print("You're now entering the dark forrest.....")
    enter = input("You come across a house do you enter Y/N? ").lower()
    if enter == 'y':
        door = input("You go into the hallway there are two doors which one do you enter Red/Yellow/Blue?").lower()
        if door == 'red':
            print("You found the treasure it's a 10% coupon for a 2-1 shampoo!")
            print("You won!")
        elif door == 'yellow':
            print("You've enter and see a huge clock on the wall and realise actually you're late for work!")
            print(end)
        elif door == 'blue':
            print("You bam your head on the way in. It hurts a little, you can't complete the adventure.")
            print(end)
        else:
            print("You didn't pick a door. You're too indecisive for this adventure. Go home!")
            print(end)
    else:
        print("You stumbled across forrest Bunnies and die from cuteness")
        print(end)
        
else:
    print("You entered the swamp , you were eaten by a swamp shark.")
    print(end)