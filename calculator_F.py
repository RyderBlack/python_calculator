def ask_number():
    while True:
        try:
            number1 = float(input("Enter number1: "))
            number2 = float(input("Enter number2: "))
            return number1, number2
        except ValueError:
                print("Error: enter valid number.")

def ask_operation():
    while True:
        operation = input("Enter operation (+, -, *, /) : ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Error : Unknown operation.")

def calculate(number1, number2, operation):
    try:
        if operation == '+':
            return number1 + number2
        elif operation == '-':
            return number1 - number2
        elif operation == '*':
            return number1 * number2
        elif operation == '/':
            if number2 == 0:
                raise ZeroDivisionError
            return number1 / number2
    except ZeroDivisionError as e:
        print(e)
        return None

def main():
    print("Start calculation")
    while True:
        number1, number2 = ask_number()
        operation = ask_operation()
        result =calculate(number1, number2, operation)
        if result is not None:
            print(f"The result of {number1} {operation} {number2} is : {result}")
            staragain = input("Star again ? (yes/no) :").strip().lower()
        if staragain != 'yes':
            print("End.")
            break
if __name__ == "__main__":
    main()
