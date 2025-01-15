from rich.console import Console
from rich.panel import Panel

console = Console()

menu = """
1. Addition
2. Subtraction
3. Multiply
4. Divide
5. Exponentiation
"""



bold_start = '\033[1m'
bold_end   = '\033[0m'

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
def substrator(x,y):
    return x - y
def multiplicator(x,y):
    return x * y
def dividor(x,y):
    if y ==0:
        return ("error! don't divide by 0")
    return x / y
def exponentor(x,y):
    return x ** y

# the main code - the calculator
def calculator():
    
    while True:
        try:
            calc_choice()
            choice = input("\nwhat order you want to do: ")
            if choice in ["1", "2", "3", "4", "5"]:
                
                num1 = input("enter the first number : ")
                if "." in num1:
                    num1 = float(num1)
                else:
                    num1 = int(num1)
                    
                num2 = input("enter the second number: ")
                if "." in num2:
                    num2 = float(num2)
                else:
                    num2 = int(num2)

                match choice:
                    case "1":
                        print(f"\nresult: {num1} + {num2} = {bold_start} {additor(num1, num2)} {bold_end}")
                    case "2":
                        print(f"\nresult: {num1} - {num2} = {bold_start} {substrator(num1, num2)} {bold_end}")
                    case "3":
                        print(f"\nresult: {num1} * {num2} = {bold_start} {multiplicator(num1, num2)} {bold_end}")
                    case "4":
                        print(f"\nresult: {num1} / {num2} = {bold_start} {dividor(num1, num2)} {bold_end}")
                    case "5":
                        print(f"\nresult: {num1} ** {num2} = {bold_start} {exponentor(num1,num2)} {bold_end}")
                    case _:
                        print("again, enter a number between 1 and 5")
            else:
                print("error choose a number between 1 and 5")
                
        except KeyboardInterrupt:
            print("Thank you!")
            return None

   
# run the code     
if __name__ == "__main__":
    calculator()
