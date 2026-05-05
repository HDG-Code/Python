# mini_problems.py

def reverse_number():
    num = input("Enter number: ")
    print("Reversed:", num[::-1])


def sum_of_digits():
    num = input("Enter number: ")
    total = sum(int(d) for d in num)
    print("Sum of digits:", total)


def main():
    print("\n1. Reverse Number")
    print("2. Sum of Digits")

    choice = input("Choose: ")

    if choice == "1":
        reverse_number()
    elif choice == "2":
        sum_of_digits()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()