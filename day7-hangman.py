from hangman_art import stages, logo;
from hangman_words import word_list;
from replit import clear;
import random;

print(logo);
lives = (len(stages)-1);

chosen_word = random.choice(word_list);

display = [];
for i in range(len(chosen_word)):
    display += "_";
    
end_game = False;
while end_game == False:
    
    #print(chosen_word);
    guess = input("Guess a letter: ").lower();  
    clear();
      
    if guess in display:
        print("You've already guessed that.");
        
    for i in range(len(chosen_word)):
        letter = chosen_word[i];
        if letter == guess:
            display[i] = letter;
    print(f"{' '.join(display)}");
            
    if guess not in chosen_word:
        print(f"{guess} are not in the word. ");
        lives -= 1;
        if lives == 0:
            end_game = True;
            print("You lose the game. :(");

    if not "_" in display:
        end_game = True;
        print("You win the game!");
    
    print(stages[lives]);
