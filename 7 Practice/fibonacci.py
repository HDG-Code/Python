# fibonacci.py

def fibonacci_series():
    n = int(input("Enter number of terms: "))

    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    fibonacci_series()