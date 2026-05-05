# calculator_functions.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = input("Choose: ")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == "1":
    print(add(a, b))
elif choice == "2":
    print(subtract(a, b))
elif choice == "3":
    print(multiply(a, b))
elif choice == "4":
    print(divide(a, b))
else:
    print("Invalid choice")