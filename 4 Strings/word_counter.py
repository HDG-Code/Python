# word_counter.py

# This function counts words in a sentence
def count_words(text):
    words = text.split()  # split sentence into words
    return len(words), words


# Main program
def main():
    text = input("Enter a sentence: ").strip()

    # Check empty input
    if text == "":
        print("Input cannot be empty!")
        return

    total, word_list = count_words(text)

    print("\n--- Result ---")
    print("Sentence     :", text)
    print("Total Words  :", total)
    print("Word List    :", word_list)


# Run program
if __name__ == "__main__":
    main()