print("select an operation :")
print("addition = 1")
print("subtraction = 2")
print("multiply = 3")
print("divide = 4")
print("exponentiation = 5")
print("continuous = 6")
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
    print("")
    num1 = float(input("enter the frist number : "))
    num2 = float(input("enter the second number: "))
    choice = input("what order you want to do: ")
    print("")
    if choice in ["1", "2", "3", "4", "5", "6"]:
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


        elif choice == "6":
            print("select an operation :")
            print("addition = 1")
            print("subtraction = 2")
            print("multiply = 3")
            print("divide = 4")
            print("exponentiation = 5")
            choice2 = input("what order you want to do: ")
            if choice2 in ["1", "2", "3", "4", "5"]:
                if choice2 == "1":
                    print(f"result: {num1} + {num2} = {add(num1, num2)}")
                    num4 = num1 + num2
                elif choice2 == "2":
                    print(f"result: {num1} - {num2} = {subs(num1, num2)}")
                    num4 = num1 - num2
                elif choice2 == "3":
                    print(f"result: {num1} * {num2} = {mult(num1, num2)}")
                    num4 = num1 * num2
                elif choice2 == "4":
                    print(f"result: {num1} / {num2} = {div(num1, num2)}")
                    num4 = num1 / num2
                elif choice2 == "5":
                    print(f"result: {num1} ** {num2} = {exp(num1,num2)}")
                    num4 = num1 ** num2


                while True: 
                        num3 = float(input("enter an other number : "))
                        print("select an operation :")
                        print("addition = 1")
                        print("subtraction = 2")
                        print("multiply = 3")
                        print("divide = 4")
                        print("exponentiation = 5")
                        choice3 = input("what order you want to do: ")
                        if choice3 in ["1", "2", "3", "4", "5"]:
                            if choice3 == "1":
                                num3 = num3 + num4
                                print( num3)
                                num4 = num3
                            elif choice3 == "2":
                                num3 = num3 - num4
                                print(num3)
                                num4 = num3
                            elif choice3 == "3":
                                num3 = num3 * num4
                                print(num3)
                                num4 = num3
                            elif choice3 == "4":
                                num3 = num3 / num4
                                print(num3)
                                num4 = num3
                            elif choice3 == "5":
                                num3 = num3 ** num4
                                print(num3)
                                num4 = num3

    else:
            print("error take a number between 1 and 5")
            return calculator

calculator()