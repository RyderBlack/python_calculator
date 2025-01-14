import re

# Add
def addit(num1,operator, num2):
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
    return result

# Substract
def substractor(num1, operator, num2):
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
    return result

#Multiply
def multiplicator(num1, operator, num2):
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
    return result

#Divide
def dividordef(num1, operator, num2):
    try:
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
        return result
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
        return None

#Main function - Calculator
def calc():
    while True:
        try:
            
            user_choice = input("Enter something (or 'q' to quit): ").replace(" ", "")
             
            
            # let the user exit the program
            if user_choice.lower() == "q":
                print("Exiting the calculator. Thank you!")
                break
            
            parts = re.split('([+-/*])', user_choice)

            if len(parts) != 3:
                print("Invalid format. Please use: number operator number")
                continue
            
            num1 = int(parts[0])
            operator = parts[1]
            num2 = int(parts[2]) 

            if operator == "+":
                addit(num1, operator, num2)
            elif operator == "-":
                substractor(num1, operator, num2)
            elif operator == "*":
                multiplicator(num1, operator, num2)
            elif operator == "/":
                dividordef(num1, operator, num2)
            else:
                print("enter a valid operation.")
                
                
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
        # to ask again for a new calc
        print("\nEnter another calculation or 'q' to quit")
                

if __name__ == "__main__":
    calc()

        



    