# prime_number.py

def check_prime():
    num = int(input("Enter number: "))

    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return

    print("Prime Number")


if __name__ == "__main__":
    check_prime()