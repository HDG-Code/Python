# append_file.py

def append_file():
    text = input("Enter text to add: ")

    with open("data.txt", "a") as file:
        file.write("\n" + text)

    print("Data appended successfully!")


def main():
    append_file()


if __name__ == "__main__":
    main()