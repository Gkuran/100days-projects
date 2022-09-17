from replit import clear;
from art import logo;

def highest_bidding(bidding_record):
    
    highest_bid = 0;
    for name in bidding_record:
        bid_value = bidding_record[name];
        if bid_value > highest_bid:
            highest_bid = bid_value;
            winner = name;
    print(f"The winner of the auction is {winner} with a bid value of ${highest_bid}");

print(logo);

bids = {};

bidding_end = False;

while bidding_end == False:    
    name = input("What's your name? ");
    price = int(input("What's your bid? $"));

    bids[name] = price;
    continue_bidding = input("Are there any other bidders? 'yes' or 'no'.");
    
    if continue_bidding == "no":
        bidding_end = True;
        highest_bidding(bids);
    elif continue_bidding == 'yes':
        clear();
        

