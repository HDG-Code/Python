# add_two_numbers.py

def add_numbers():
    try:
        no1 = int(input("Enter the first number: "))
        no2 = int(input("Enter the second number: "))
        result = no1 + no2
        print(f"Sum is: {result}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

add_numbers()   