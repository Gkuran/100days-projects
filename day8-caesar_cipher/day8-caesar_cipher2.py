from art import *;


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):
     
    shift = shift % 26;
    if direction == "decode":
        shift *= -1;
        
    shifted_letters = [];
    for letter in text:
        if letter in alphabet:
            ind = alphabet.index(letter);
            shifted_indexes = ind + shift;
            shifted_letters.append(alphabet[shifted_indexes]);
        else:
            shifted_letters.append(letter);
   
    shifted_text = "".join(shifted_letters);
    print(f"The {direction}d text is {shifted_text}");

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

print(logo);

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

end = False;
while end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
    text = input("Type your message:\n").lower();
    shift = int(input("Type the shift number:\n"));

    caesar(text, shift, direction);
    finish = input("Type 'yes' if you want to use again or 'exit' to finish the session.\n");
    if finish == "exit":
        end = True;
        print("Session ended...");