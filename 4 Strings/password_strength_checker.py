

# password = input("Enter password: ")

# if len(password) >= 8:
#     print("Strong Password")
# else:
#     print("Weak Password")


# password_strength_checker.py

import string


def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password ❌ (Minimum 8 characters required)"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password ✅"
    else:
        return "Medium Password ⚠️ (Add uppercase, numbers, or special characters)"


def main():
    password = input("Enter password: ").strip()

    if not password:
        print("Password cannot be empty!")
        return

    result = check_password_strength(password)
    print(result)


if __name__ == "__main__":
    main()