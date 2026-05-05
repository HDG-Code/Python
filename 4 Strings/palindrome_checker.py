# palindrome_checker.py

# word = input("Enter word: ")

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


def is_palindrome(text):
    # Normalize: remove spaces and make lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def main():
    word = input("Enter word or sentence: ").strip()

    if not word:
        print("Input cannot be empty!")
        return

    if is_palindrome(word):
        print("Palindrome ✅")
    else:
        print("Not Palindrome ❌")


if __name__ == "__main__":
    main()