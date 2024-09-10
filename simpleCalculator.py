# 1st
"""def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

def main():
    userInput = input("This is a simple calculator. \n\nPlease separate the number and operator with a space: ")
    try:
        n1, mathType, n2 = userInput.split()
        n1 = int(n1)
        n2 = int(n2)
        
        if mathType == '+':
            result = addition(n1, n2)
        elif mathType == '-':
            result = subtraction(n1, n2)
        elif mathType == '*':
            result = multiplication(n1, n2)
        elif mathType == '/':
            result = division(n1, n2)
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return
        
        print(f"The solution of {n1} {mathType} {n2} = {result}")
        
    except ValueError:
        print("Invalid input. Please enter in the format: number operator number.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
"""

# 2nd:
def evaluate_expression(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Invalid input: {e}"

def main():
    userInput = input("This is a simple calculator. \n\nPlease enter an expression (e.g., 5 + 6 + 8 - 5): ")
    result = evaluate_expression(userInput)
    
    print(f"The result of the expression '{userInput}' is: {result}")
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
