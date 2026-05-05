# string_operations.py

def print_section(title):
    print("\n" + "-" * 25 + f" {title} " + "-" * 25)


def display_text(text):
    print_section("About Me")
    print(text.strip())


def analyze_text(text, keyword="My"):
    print_section("Analysis")

    print(f"Count of '{keyword}' : {text.count(keyword)}")
    print(f"Total length         : {len(text)}")


def apply_string_methods(text):
    print_section("String Methods")

    print(f"Split Words   : {text.split()}")
    print(f"\nReplaced Text:\n{text.replace('My', 'Your')}")
    print(f"\nUppercase:\n{text.upper()}")
    print(f"\nLowercase:\n{text.lower()}")


def center_example(word="hello"):
    print_section("Center Example")

    print(f"Original : {word}")
    print(f"Centered : {word.center(30)}")


def strip_example(text="   Hello World!   "):
    print_section("Strip Example")

    print(f"Before : '{text}'")
    print(f"After  : '{text.strip()}'")


def main():
    text = """
My name is Hit Galani.
I am 18 years old.
I live in Surat.
I study in class F.Y.B.C.A (AI & DS).
My father name is DipakBhai Galani.
My mother name is HetalBan Galani.
"""

    display_text(text)
    analyze_text(text)
    apply_string_methods(text)
    center_example()
    strip_example()

    print_section("End")


if __name__ == "__main__":
    main()