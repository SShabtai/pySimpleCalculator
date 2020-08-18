# A simple calculator - Y1, group D, MEET Project 
# Author: Tamar Shabtai 

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates one number power the second numbers
def power(x, y):
    return x ** y

# This function calculates the modulo resulting from the division of one number by the second number
def modulo(x, y):
    return x % y 

def add_to_history(num1, num2, operator, result):
        hist_str = str(num1) + " " + operator + " " + str(num2) + " = " + str(result) 
        if 50 <= len(history):
            history.pop()
        history.append(hist_str)

history = []

print("Hi! Please select operation:")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for dividtion")
print("5 for power")
print("6 for modulo")
print("h for history")
print("q to quit")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/h/q): ")

     # Accept 'q' or 'Q' by adding str.upper()
    if 'Q' == choice.upper():
        print("Thanks for using my simple calculator.")
        break

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', 'h', 'H'): 

        if 'H' == choice.upper():
            print(history)
        else:
            user_input = input("Enter first number: ")
            if user_input.isnumeric(): 
                num1 = float(user_input)

                user_input = input("Enter second number: ")
                if user_input.isnumeric():
                    num2 = float(user_input) 

                    if choice == '1':
                        add_to_history(num1, num2, "+", add(num1, num2)) 
                        print(num1, "+", num2, "=", add(num1, num2)) 

                    elif choice == '2':
                        add_to_history(num1, num2, "-", subtract(num1, num2)) 
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        add_to_history(num1, num2, "*", multiply(num1, num2)) 
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))

                    elif choice == '5':
                        add_to_history(num1, num2, "**", power(num1, num2)) 
                        print(num1, "**", num2, "=", power(num1, num2))

                    elif choice == '6':
                        add_to_history(num1, num2, "%", modulo(num1, num2)) 
                        print(num1, "%", num2, "=", modulo(num1, num2))

                    print() # Just adding a blank line for the separation from the previous calculation. 

                else:
                    print("Please enter a numerical value.")
            else:
                print("Please enter a numeric value.")
    else:
        print("Invalid selection.")


