# even_odd.py

def check_even_odd():
    num = int(input("Enter number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    check_even_odd()