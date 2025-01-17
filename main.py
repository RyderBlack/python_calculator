import re

global cmd_history
cmd_history = []


def print_result(num1, operator, num2, result):
    print(f"{num1} {operator} {num2} = {result}")
    return result

#Main function - Calculator
def calc():
    while True:
        try:
            
            user_choice = input("Enter your calculation (or 'q' to quit): ").replace(" ", "")
                      
            # let the user exit the program
            if user_choice.lower() == "q":
                print("Exiting the calculator. Thank you!")
                break
            
            parts = re.split('([+-/*])', user_choice)        
            # print(parts)
            cmd_history.append(parts)
            print(cmd_history)

            if len(parts) != 3:
                print("Invalid format. Please use: number operator number")
                continue
            
            num1 = int(parts[0])
            operator = parts[1]
            num2 = int(parts[2])
    
            match operator:
                case "+":
                    result = num1 + num2
                    print_result(num1, operator, num2, result)
                case "-":
                    result = num1 - num2
                    print_result(num1, operator, num2, result)
                case "*":
                    result = num1 * num2
                    print_result(num1, operator, num2, result)
                case "/":
                    try:
                        result = num1 / num2
                        print_result(num1, operator, num2, result)
                    except ZeroDivisionError:
                        print("Error: Cannot divide by zero")
                        # return None
                case _:
                    print("enter a valid operation.")
                
                
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        except KeyboardInterrupt:
            print("Goodbye!")
            return None
            
            

if __name__ == "__main__":
    calc()

        



    