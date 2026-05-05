# tuple_set_dict.py

def show_data_structures():
    # Tuple (immutable)
    my_tuple = (1, 2, 3)
    print("\nTuple :", my_tuple)

    # Set (no duplicates)
    my_set = {1, 2, 2, 3}
    print("Set   :", my_set)

    # Dictionary (key-value)
    my_dict = {
        "name": "Hit",
        "age": 18,
        "city": "Surat"
    }

    print("Dictionary :", my_dict)
    print("Name       :", my_dict["name"])


def main():
    show_data_structures()


if __name__ == "__main__":
    main()