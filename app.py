from rich.console import Console
from rich.panel import Panel
import os

console = Console()

# the menu
menu = """
1. Addition
2. Subtraction
3. Multiply
4. Divide
5. Exponentiation
"""


# bold style for prints
bold_start = '\033[1m'
bold_end   = '\033[0m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
       
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')
    
    
    

# display choice to user
def calc_choice():
    print("+-------------------+")
    console.print(Panel(menu, title="[bold cyan]Menu[/bold cyan]", expand=False))
    print("+-------------------+")
    # print("""
    #     \033[1;36m+-------------------+
    #     |     \033[1;33m=== Menu ===\033[1;36m   |
    #     +-------------------+
    #     | 1. Addition        |
    #     | 2. Subtraction     |
    #     | 3. Multiply        |
    #     | 4. Divide          |
    #     | 5. Exponentiation  |
    #     +-------------------+\033[0m
    # """)


# the 5 calculations
def additor(x,y):
    return x + y
def subtrator(x,y):
    return x - y
def multiplicator(x,y):
    return x * y
def dividor(x,y):
    if y ==0:
        return ("error! don't divide by 0")
    return x / y
def exponentor(x,y):
    return x ** y

def get_number(user_input_number):
    while True:
        try:
            num = input(user_input_number)
            if '.' in num:
                return float(num)
            else:
                return int(num)
        except ValueError:
            console.print("[bold red]Error: Please enter a valid number[/bold red]")


# the main code - the calculator
def calculator():
    
    while True:
        try:
            
            calc_choice()
            
            choice = input("\nWhat operation do you want to do: ")
            if choice in ["1", "2", "3", "4", "5"]:
                
                num1 = get_number("enter the first number : ")
                num2 = get_number("enter the second number: ")         

                
                clear_screen()
                calc_choice()
                
                # match case to determine the operation to do
                match choice:
                    case "1":
                        print(f"\nresult: {num1} + {num2} = {bold_start}{additor(num1, num2)}{bold_end}")
                    case "2":
                        print(f"\nresult: {num1} - {num2} = {bold_start}{subtrator(num1, num2)}{bold_end}")
                    case "3":
                        print(f"\nresult: {num1} * {num2} = {bold_start}{multiplicator(num1, num2)}{bold_end}")
                    case "4":
                        print(f"\nresult: {num1} / {num2} = {bold_start}{dividor(num1, num2)}{bold_end}")
                    case "5":
                        print(f"\nresult: {num1} ** {num2} = {bold_start}{exponentor(num1,num2)}{bold_end}")
                    case _:
                        print("again, enter a number between 1 and 5")
                
                input("\nPress Enter to continue...")
                clear_screen()
                
            else:
                console.print("[bold red]error choose a number between 1 and 5[bold red]")
                input("\nPress Enter to continue...")
                clear_screen()
                
        
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")        
        except KeyboardInterrupt:
            clear_screen()
            print("Thank you!")
            return None

   
# run the code     
if __name__ == "__main__":
    calculator()
