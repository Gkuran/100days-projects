from game_data import *;
from art import *;
import random;


def main():
    
    print(logo);
    
    score = 0;    
    endgame = False;
    
    while endgame == False:
        
        numA = random.randint(0, len(data)+1);
        print(f"Compare A: {data[numA]['name']}, {data[numA]['description']}, {data[numA]['country']}");
        
        print(vs);

        numB = random.randint(0, len(data)+1);
        print(f"Compare B: {data[numB]['name']}, {data[numB]['description']}, {data[numB]['country']}");
        
        userGuess = input("Who has more followers? Type 'A' or 'B': ");
        
        if userGuess == "A":
            if data[numA]["follower_count"] > data[numB]["follower_count"]:
                score += 1;
                print(f"You're right! Current score: {score}"); 
            else:
                print(f"Sorry, that's wrong! Final score: {score}");
                endgame = True;
                
        elif userGuess == "B":
            if data[numB]["follower_count"] > data[numA]["follower_count"]:
                score += 1;
                print(f"You're right! Current score: {score}"); 
            else:
                print(f"Sorry, that's wrong! Final score: {score}");
                endgame = True;
                
main();
            
