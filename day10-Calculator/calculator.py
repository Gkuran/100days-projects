from art import logo;

def add(n1, n2):
    return n1 + n2;

def subtract(n1, n2):
    return n1 - n2;

def multiply(n1, n2):
    return n1 * n2;

def divide(n1, n2):
    return n1 / n2;

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    
    print(logo);
    
    num1 = float(input("Enter the first number: "));

    end_operations = False;
    while end_operations == False:
            
        num2 = float(input("Enter the second number: ")); 
        
        for operation in operations:
            print(operation);    
        choosed_operation = input("Choose an operation from above: ");
        for operation in operations:
            if operation == choosed_operation:
                answer = operations[choosed_operation](num1, num2);       
        print(f"Your calculation: {num1}{choosed_operation}{num2} = {answer}");
        
        end_choose = input(f"Do you want to do another operation with {answer}? 'yes' or 'no'. ").lower();
        if end_choose == "no":
            end_operations = True;
            calculator();
        elif end_choose == "yes":
            num1 = answer;
            
calculator();

