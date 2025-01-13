
def addit(num1,operator, num2):
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
    return result

def substractor(num1, operator, num2):
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
    return result

def multiplicator(num1, operator, num2):
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
    return result

def dividordef(num1, operator, num2):
    try:
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
        return result
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")

def calc():
    
    user_choice = input("Enter something : ")
    parts = user_choice.split()

    num1 = int(parts[0])
    operator = parts[1]
    num2 = int(parts[2]) 

    # print(f"{num1} {operator} {num2}")

    if len(parts) != 3:
        raise ValueError("Invalid format. Please use: number operator number")

    if operator == "+":
        return addit(num1, operator, num2)
    elif operator == "-":
        return substractor(num1, operator, num2)
    elif operator == "*":
        return multiplicator(num1, operator, num2)
    elif operator == "/":
        return dividordef(num1, operator, num2)
    else:
        print("entrez une operation valide.")
        

calc()
        



    