# text_analysis.py

def get_text():
    return input("Enter any text:\n> ")


def get_word():
    return input("Enter a word to search:\n> ")


def analyze_text(text, word):
    print("\n" + "-" * 25 + " TEXT ANALYSIS " + "-" * 25)

    print(f"Length of text : {len(text)}")
    print(f"Occurrences of '{word}' : {text.count(word)}")


def main():
    text = get_text()
    word = get_word()

    if word.strip() == "":
        print("Invalid input! Word cannot be empty.")
        return

    analyze_text(text, word)


if __name__ == "__main__":
    main()