MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0;
is_on = True;

def make_coffee(drink_name, order_ingredients):
    
    '''Deduct the required ingredients from the resources.'''

    for item in order_ingredients:
        resources[item] -= order_ingredients[item];
    print(f"Here's your {drink_name} ☕ ");

def transaction_successful(money_received, drink_cost):
    
    '''Return True if payment is accepted or False if money is insufficient.'''
    
    if money_received >= drink_cost:
        
        change = round(money_received - drink_cost, 2);
        print(f"Here's ${change} in change. ");
        
        global profit;
        profit += drink_cost;
        
        return True;
    else:
        print("Sorry, that's not enough money. ");
        return False;
    

def enough_resources(order_ingredients):
    
    '''Return True if order can be made or False if the resources are insufficient.'''
    
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's no enough {item}. ");
            return False;
    return True;

def process_coins():
    
    '''Returns the total - calculated - from coins inserted.'''
    
    print("Please, insert coins: ");
    total = int(input("How many quarters? ")) * 0.25; 
    total += int(input("How many dimes? ")) * 0.1; 
    total += int(input("How many nickles? ")) * 0.05; 
    total += int(input("How many pennies? ")) * 0.01; 
    return total;

def main():  
      
    global is_on;
    while is_on == True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower();
        
        if order == "off":
            is_on = False;
        elif order == "report":
            print(f"water: {resources['water']}ml");
            print(f"Milk: {resources['milk']}ml");
            print(f"Coffee: {resources['coffee']}g");
            print(f"Money: ${profit}");
        else:
            drink = MENU[order];
            if enough_resources(drink["ingredients"]):
                payment = process_coins();
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(order, drink["ingredients"]);

main();            
            