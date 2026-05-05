# list_operations.py

# This function shows basic list operations
def list_operations():
    numbers = [1, 2, 3, 4, 5]

    print("\n--- LIST OPERATIONS ---")
    print("Original List :", numbers)

    # Add element
    numbers.append(6)
    print("After Append  :", numbers)

    # Remove element
    numbers.remove(3)
    print("After Remove  :", numbers)

    # Access element
    print("First Element :", numbers[0])

    # Length
    print("Length        :", len(numbers))


def main():
    list_operations()


if __name__ == "__main__":
    main()