# phone_number_cleaner.py

# Example:
# Input  : +49 (176) 123-4567
# Output : 00491761234567

# This function cleans the phone number
def clean_number(number):
    # Step 1: Replace '+' with '00'
    number = number.replace("+", "00")

    # Step 2: Remove all spaces
    number = number.replace(" ", "")

    # Step 3: Remove brackets '(' and ')'
    number = number.replace("(", "")
    number = number.replace(")", "")

    # Step 4: Remove dash '-'
    number = number.replace("-", "")

    # Return cleaned number
    return number


# Main function (program starts here)
def main():
    # Take input from user
    number = input("Enter phone number: ")

    # Check if input is empty
    if number == "":
        print("Input cannot be empty!")
        return

    print("\n--- Result ---")

    # Show original number
    print("Before:", number)

    # Call function to clean number
    cleaned = clean_number(number)

    # Show cleaned number
    print("After :", cleaned)


# This line ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()