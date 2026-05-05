# string_formatting.py

def format_with_concatenation(name, age, city):
    return "My name is " + name + ", I am " + str(age) + " years old and I live in " + city + "."


def format_with_fstring(name, age, city):
    return f"My name is {name}, I am {age} years old and I live in {city}."


def format_with_format(name, age, city):
    return "My name is {}, I am {} years old and I live in {}.".format(name, age, city)


def main():
    name = "Hit Galani"
    age = 18
    city = "Surat"

    print("\n--- String Formatting Examples ---\n")

    print("Concatenation:")
    print(format_with_concatenation(name, age, city))

    print("\nF-String (Recommended):")
    print(format_with_fstring(name, age, city))

    print("\nFormat Method:")
    print(format_with_format(name, age, city))


if __name__ == "__main__":
    main()