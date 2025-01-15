print("select an operation :")
print("addition = 1")
print("subtraction = 2")
print("multiply = 3")
print("divide = 4")
print("exponentiation = 5")
def add(x,y):
    return x + y
def subs(x,y):
    return x - y
def mult(x,y):
    return x * y
def div(x,y):
    if y ==0:
        return ("error! don't divide by 0")
    return x / y
def exp(x,y):
    return x ** y

def calculator():
 while True:
    choice = input("what order you want to do: ")
    if choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("enter the frist number : "))
        num2 = float(input("enter the second number: "))

        if choice == "1":
            print(f"result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"result: {num1} - {num2} = {subs(num1, num2)}")
        elif choice == "3":
            print(f"result: {num1} * {num2} = {mult(num1, num2)}")
        elif choice == "4":
            print(f"result: {num1} / {num2} = {div(num1, num2)}")
        elif choice == "5":
            print(f"result: {num1} ** {num2} = {exp(num1,num2)}")
    else:
            print("error take a number between 1 and 5")

calculator()
