# You want a program that can do addition, subtraction, multiplication, and division.

no1 = int(input("Enter the first number:  "))
no2 = int(input("Enter the second number: "))

op = input("Enter the Operator (+, -, *, /): ")

if op == "+":
    print(f"Addition is {no1 + no2}")

elif op == "-":
    print(f"Subtraction is {no1 - no2}")

elif op == "*":
    print(f"Multiplication is {no1 * no2}")

elif op == "/":
    if no2 == 0:
        print("Division by zero is not allowed")
    else:
        print(f"Division is {no1 / no2}")

else:
    print("Invalid operator")

# Build a program that takes two numbers and an operator (+, −, ×, ÷) and returns the result.

# a = float(input("Enter the First Number:- "))
# b = float(input("Enter the Second Number:- "))

# operator = input("Enter the operator (+, -, *, /):- ")
# if operator == "+":
#     print("The Sum is:- ",a + b)
# elif operator == "-":
#     print("The Difference is:- ",a - b)
# elif operator == "*":
#     print("The Product is:- ",a * b)
# elif operator == "/":
#     if b != 0:
#         print("The Quotient is:- ",a / b)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operator. Please use (+, -, *, or /).")
    