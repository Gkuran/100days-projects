from typing import final


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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print();
pathChoice = input("On your journey the path diverges in two separate ways. On the left, there some type of silent forest around the path... With dark dead trees; meanwhile to the right you can see a path between two large mountains; and a light far away to the path, shining in the horizon. What path would you choice? 'left' or 'right'\n ").lower();

if pathChoice == "left":
    lakeChoice = input("In the middle of the forest you find a lake... The moonlight on the water surface looks like a beautiful mirror and you find yourself tempted to swim there. What will you do? 'swim' or 'turn around'" ).lower();
    if lakeChoice == "turn around":
        finalChoice = input("You turn around and see a cabin that wasn't there before; a old wood cabin. Inside the cabin you find three doors: A red door, a yellow door and a blue one. Which door do you choose?").lower();
        if finalChoice == "red door":
            print("You open the door and a demon comes out and smash your head against the floor. Game over.");
        elif finalChoice == "yellow door":
            print("You see a gold open chest shining liking a gold morning sun; the treasure. Congratulations!");
        elif finalChoice == "blue door":
            print("Opening the door activates a trap. A shotgun barrel ejects from behind the door and shoots you. Game over.");
    else:
        print("You get drowned. Game over.");
else:
    print("You find Brazil.\n");
    print('''         
 _                   _ _ 
| |                 (_) |
| |__  _ __ __ _ _____| |
| '_ \| '__/ _` |_  / | |
| |_) | | | (_| |/ /| | |
|_.__/|_|  \__,_/___|_|_|         
          ''');
    print("Game over.");
