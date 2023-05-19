"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# loop
while True:
# get user input    
    user_input = input("What function do you want to perform? ")
    tokens = user_input.split(' ')
# if the first token is q, quit the loop
    if "q" in tokens:
        break
    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue


# define variables for tokens
    operator = tokens[0]
    num1 = tokens[1]
    if not num1.isdigit() and not num2.isdigit():
        print("Not a valid input.")
        continue
    
    if len(tokens) < 3:
        num2 = 0
    else:
        num2 = tokens[2]
    
    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))
        
    elif operator == "*":
        result = multiply(float(num1),float(num2))
        
    elif operator == "/":
        result = divide(float(num1),float(num2))
        
    elif operator == "square":
        result = square(float(num1))
        
    elif operator == "cube":
        result = cube(float(num1))
        
    elif operator == "pow":
        result = power(float(num1), float(num2))
        
    elif operator == "mod":
        result = mod(float(num1), float(num2))
        
    else:
        result = "Please enter a valid operation."

    print(result)
