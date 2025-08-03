# Basic Calculator Program

# To get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform calculation based on the operation
if operation == '+':
    print(num1, "+", num2, "=", num1 + num2)
elif operation == '-':
    print(num1, "-", num2, "=", num1 - num2)
elif operation == '*':
    print(num1, "*", num2, "=", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")

