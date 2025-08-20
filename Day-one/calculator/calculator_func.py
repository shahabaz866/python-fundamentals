def get_number(prompt):
    while True:
        try:
            return float(input(prompt))   
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
def get_operations():
    valid_op=['+','-','*','/']
    while True:
        op = input("Enter the operation (+, -, *, /): ")
        if op in valid_op:
            return op
        else:
            print("❌ Invalid operation. Please choose one of +, -, *, /")
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    num1 = get_number("Enter first number: ")
    op = get_operations()
    num2 = get_number("Enter second number: ")
    
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("❌ Error: Division by zero")
    else:
        print("❌ Invalid operation")


calculator()
