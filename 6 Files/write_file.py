# write_file.py

def write_file():
    text = input("Enter text to write in file: ")

    with open("data.txt", "w") as file:
        file.write(text)

    print("Data written successfully!")


def main():
    write_file()


if __name__ == "__main__":
    main()