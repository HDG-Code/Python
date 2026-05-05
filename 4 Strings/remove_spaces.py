# remove_spaces.py

def show_strip_operations(text):
    print("\n" + "-" * 20 + " STRIP OPERATIONS " + "-" * 20)

    print(f"Original      : '{text}'")
    print(f"Left Strip    : '{text.lstrip()}'")
    print(f"Right Strip   : '{text.rstrip()}'")
    print(f"Full Strip    : '{text.strip()}'")


def main():
    text = input("Enter text with spaces: ")

    if not text:
        print("Input cannot be empty!")
        return

    show_strip_operations(text)

    print("\n" + "-" * 20 + " END " + "-" * 20)


if __name__ == "__main__":
    main()