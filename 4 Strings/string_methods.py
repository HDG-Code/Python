# string_methods.py

def string_methods(text):
    print("\n--- String Methods Output ---\n")

    print(f"Original Text : {text}")
    print(f"Uppercase     : {text.upper()}")
    print(f"Lowercase     : {text.lower()}")
    print(f"Title Case    : {text.title()}")
    print(f"Replaced Text : {text.replace('python', 'Java')}")
    print(f"Split Words   : {text.split()}")


def main():
    text = input("Enter a sentence: ").strip()

    if not text:
        print("Input cannot be empty!")
        return

    string_methods(text)


if __name__ == "__main__":
    main()