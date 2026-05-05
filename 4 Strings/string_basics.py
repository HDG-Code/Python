# string_basics.py

def string_basics(text, number):
    print("\n--- STRING BASICS ---\n")

    print(f"Text value      : {text}")
    print(f"Number value    : {number}")

    # Concatenation
    print("\nConcatenation:")
    print("Hello " + text)
    print("Hello " + str(number))

    # String operations
    print("\nString Methods:")
    print(f"Uppercase       : {text.upper()}")
    print(f"Lowercase       : {text.lower()}")
    print(f"Length          : {len(text)}")


def main():
    text = input("Enter text: ").strip()
    number_input = input("Enter a number: ").strip()

    if not text:
        print("Text cannot be empty!")
        return

    if not number_input.isdigit():
        print("Invalid number input!")
        return

    number = int(number_input)

    string_basics(text, number)


if __name__ == "__main__":
    main()