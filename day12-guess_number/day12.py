#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Include an ASCII art logo.
# If they got the answer correct, show the actual answer to the player.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo;
import random;

global lives

lives = 0;

def main():
    
    print(logo);
    
    global lives;
    
    print("Welcome to the Number Guessing Game!");
    print("I'm thinking a number between 1 and 100.");
    secret_number = random.randint(1, 100);
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ");

    if difficulty == "easy":
        lives = 10;
    elif difficulty == "hard":
        lives = 5;
 
    compare_guess(secret_number);

def compare_guess(secret_number):
    
    global lives;
    #print(f"lives: {lives}");
    #print(f"Nun: {secret_number}");
    
    endgame = False
    while endgame == False:
        guess = int(input("Guess a number between 1 and 100: "));
        if guess == secret_number:
            print("Right guess! You win!!");
            endgame = True;
        elif guess > secret_number:
            print("Too high.");
            lives -= 1;
            print(f"You have {lives} guesses remaining.")
        elif guess < secret_number:
            print("Too low.");
            lives -= 1;    
            print(f"You have {lives} guesses remaining.")
            
        if lives == 0:
            print("Out of guesses. You lose.");
            endgame = True;

main();


