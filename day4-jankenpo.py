rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random;

options = [scissors, paper, rock];
random_number = random.randint(0, len(options)-1);

player_choice = int(input("Type 0 for scissors, 1 for paper and 2 for rock. "));
player_choice = options[player_choice];
computer_choice = options[random_number];

print(player_choice);
print(computer_choice);

if player_choice == scissors:
    if computer_choice == paper:
        print("You win!");
    elif computer_choice == rock:
        print("You lose!");
    else:
        print("It's a draw");
        
if player_choice == paper:
    if computer_choice == rock:
        print("You win!");
    elif computer_choice == scissors:
        print("You lose!");
    else:
        print("It's a draw");    
    
if player_choice == rock:
    if computer_choice == scissors:
        print("You win!");
    elif computer_choice == paper:
        print("You lose!");
    else:
        print("It's a draw!");
