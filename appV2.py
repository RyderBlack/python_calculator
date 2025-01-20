from rich.console import Console
from rich.panel import Panel
import os

console = Console()
history = []
result_history = []


# the menu
menu = """
1. Addition
2. Subtraction
3. Multiply
4. Divide
5. Exponential
      ===
6. Show History
7. Delete History
      ===
8. Continue Last Calculation
"""


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
       
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')
    
    
    

# display choice to user
def display_menu():
    print("     +-------------------+")
    console.print(Panel(menu, title="[bold cyan]Menu[/bold cyan]", expand=False))
    print("     +-------------------+")



# the 5 calculations
def additor(x,y):
    result = x + y
    console.print(f"\n[bold green]result is: {x} + {y} = {result}[/bold green]")

    result_history.append(result)
    history.append(f'{x} + {y} = {result}')
    result_history.append(result)
    return result

def subtrator(x,y):
    result = x - y
    console.print(f"\n[bold green]result is: {x} - {y} = {result}[/bold green]")

    result_history.append(result)
    history.append(f'{x} - {y} = {result}')
    return result

def multiplicator(x,y):
    result = x * y
    console.print(f"\n[bold green]result is: {x} * {y} = {result}[/bold green]")

    result_history.append(result)
    history.append(f'{x} * {y} = {result}')
    return result

def dividor(x,y):
    if y ==0:
        return console.print("[bold red]error! don't divide by 0[/bold red]")
    else:
        result = x / y
        console.print(f"\n[bold green]result is: {x} / {y} = {result}[/bold green]")

        result_history.append(result)
        history.append(f'{x} / {y} = {result}')
        return result

def exponentor(x,y):
    result = x ** y
    console.print(f"\n[bold green]result is: {x} ** {y} = {result}[/bold green]")

    result_history.append(result)
    history.append(f'{x} ** {y} = {result}')
    return result


def show_history():
    print(history)
    
    
def delete_history():
    history.clear()
    console.print("The history has been deleted.")


# get the input numbers and sort if int or float
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
            
            display_menu()
            
            choice = input("\nWhat operation do you want to do: ")
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                
                if choice in ["1", "2", "3", "4", "5"]:
                    num1 = get_number("enter the first number : ")
                    num2 = get_number("enter the second number: ") 
                
                clear_screen()
                display_menu()
                
                # match case to determine the operation to do
                match choice:
                    case "1":
                        additor(num1, num2)
                    case "2":
                        subtrator(num1,num2)
                    case "3":
                        multiplicator(num1, num2)
                    case "4":
                        dividor(num1, num2)
                    case "5":
                        exponentor(num1,num2)
                    
                    #history related choices    
                    case "6":
                        if not history:
                            print("there is no history at the moment")
                        else:
                            show_history()
                    case "7":
                        if not history:
                            print("there is no history to delete")
                        else:
                            delete_history()
                                
                    # continue last calc          
                    case "8":
                        if not result_history:
                            print("there is no history to start with")
                        else:
                            
                            clear_screen()
                            display_menu()
                            
                            last_result = result_history[-1]
                            choice2 = input("what other calculation do you want to do? ")
                            
                            if choice2 in ["1", "2", "3", "4", "5"]:
                                num3 = get_number("enter the new number : ")
                                
                            match choice2:
                                case "1":
                                    additor(last_result, num3)
                                case "2":
                                    subtrator(last_result, num3)
                                case "3":
                                    multiplicator(last_result, num3)
                                case "4":
                                    dividor(last_result, num3)
                                case "5":
                                    exponentor(last_result, num3)   
                         
                    # wildcard just in case        
                    case _:
                        print("again, enter a number between 1 and 5")
                
                input("\nPress Enter to continue...")
                clear_screen()
                 
            else:
                console.print("[bold red]error choose a number between 1 and 5[/bold red]")
                input("\nPress Enter to continue...")
                clear_screen()
                
        
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")        
        except KeyboardInterrupt:
            clear_screen()
            console.print("[bold blue]Thank you for using our calculator![/bold blue]")
            return None


   
# run the code     
if __name__ == "__main__":
    calculator()
