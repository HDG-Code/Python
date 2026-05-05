# factorial.py

def factorial():
    num = int(input("Enter number: "))
    result = 1

    for i in range(1, num + 1):
        result *= i

    print("Factorial:", result)


if __name__ == "__main__":
    factorial()