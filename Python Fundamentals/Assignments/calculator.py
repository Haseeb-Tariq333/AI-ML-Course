def calculator(a, b, operation):
    if operation == '+':
        print(f"Addition = {a} + {b} = {a + b}")
    elif operation == '-':
        print(f"Subtraction = {a} - {b} = {a - b}")
    elif operation == '*':
        print(f"Multiplication = {a} x {b} = {a * b}")
    elif operation == '/':
        print(f"Division = {a} / {b} = {a / b}")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation you want to perform: ")
calculator(a, b, operation)