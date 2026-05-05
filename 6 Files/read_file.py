# read_file.py

def read_file():
    try:
        with open("data.txt", "r") as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
    except FileNotFoundError:
        print("File not found!")


def main():
    read_file()


if __name__ == "__main__":
    main()