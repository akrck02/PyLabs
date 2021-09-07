
exit = "no";

# Main Calc operations
def add(x,y): return x + y;
def substract(x,y): return x - y;
def multiply(x,y): return x * y;
def divide(x,y): return x / y; 
def power(x,y): return x ** y;

def getUserInput() : 
    try: 
        x = float(input("Enter first number : "));
        y = float(input("Enter second number : "));
    except: 
        print("Error: Invalid number");
        return getUserInput();
    
    return x,y;

def calcMode(n): 

    inputs = getUserInput();
    x = inputs[0];
    y = inputs[1];

    if(n == 1):
        txt = "Operation: {0} + {1}";

        print(txt.format(x,y))
        print("Result : ", add(x,y));
    elif(n == 2):
        txt = "Operation: {0} - {1}";
        print( txt.format(x,y) );
        print("Result : ", substract(x,y));
    elif(n == 3):
        txt = "Operation: {0} * {1}";
        print( txt.format(x,y) );
        print("Result : ", multiply(x,y));
    elif(n == 4):
        txt = "Operation: {0} / {1}";
        print( txt.format(x,y) );
        print("Result : ", divide(x,y));
    elif(n == 5):
        txt = "Operation: {0} ^ {1}";
        print( txt.format(x,y) );
        print("Result : ", power(x,y));





print("#################################")
print("       MATH CALCULATOR v1.0      ")
print("#################################")

while(exit != "yes"):

    print("\nSelect your mode:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")


    mode = -1;
    try: 
        mode = int(input("\nEnter your mode: "));
        if(mode < 1 or mode > 5): 
            raise TypeError()

    except:
        print("\n-------------------------------------")
        print("Select a valid mode.")
        print("-------------------------------------")
        continue;

    print("\n")
    calcMode(mode);

    print("\n-------------------------------------")
    exit = input("exit the program? (yes/no): ")
    print("-------------------------------------")