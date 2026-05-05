# quiz_game/main.py

def quiz():
    score = 0

    print("Q1: What is 2+2?")
    if input("Answer: ") == "4":
        score += 1

    print("Q2: Capital of India?")
    if input("Answer: ").lower() == "delhi":
        score += 1

    print("\nYour Score:", score)


if __name__ == "__main__":
    quiz()