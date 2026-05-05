# phone_number_replace.py

# This program replaces part of a phone number based on user input

def replace_number_part(number, old_part, new_part):
    return number.replace(old_part, new_part)


def main():
    # Take phone number input
    number = input("Enter the phone number: ").strip()

    # Check empty input
    if number == "":
        print("Phone number cannot be empty!")
        return

    print("\nBefore Number :", number)

    # Ask what to replace
    old_part = input("Enter the part you want to replace: ").strip()
    new_part = input("Enter the new value: ").strip()

    # Check empty replace value
    if old_part == "":
        print("Replace value cannot be empty!")
        return

    # Replace operation
    updated_number = replace_number_part(number, old_part, new_part)

    print("After Number  :", updated_number)


# Run program
if __name__ == "__main__":
    main()