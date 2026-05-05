# email_validator.py

# email = input("Enter email: ")

# if "@" in email and "." in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")  


def is_valid_email(email):
    email = email.strip()

    # Basic structure checks
    if "@" not in email or "." not in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    # Check username and domain are not empty
    if not username or not domain:
        return False

    # Domain must contain dot and not start/end with dot
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True


def main():
    email = input("Enter email: ")

    if is_valid_email(email):
        print("Valid Email ✅")
    else:
        print("Invalid Email ❌")


if __name__ == "__main__":
    main()