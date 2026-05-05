# even_or_odd.py

def check_even_odd():
    try:
        no = int(input("Enter a number: "))
        if no % 2 == 0:
            print(f"{no} is Even")
        else:
            print(f"{no} is Odd")
    except ValueError:
        print("Invalid input! Enter a valid number.")

check_even_odd()