# email_validator.py

# This function checks if email is valid
def is_valid_email(email):
    email = email.strip()  # remove extra spaces

    # Must contain @ and .
    if "@" not in email or "." not in email:
        return False

    # Split email into two parts
    parts = email.split("@")

    # There must be exactly one @
    if len(parts) != 2:
        return False

    username = parts[0]
    domain = parts[1]

    # Username and domain should not be empty
    if username == "" or domain == "":
        return False

    return True


# Main program
def main():
    email = input("Enter email: ")

    if email == "":
        print("Email cannot be empty!")
        return

    if is_valid_email(email):
        print("Valid Email ✅")
    else:
        print("Invalid Email ❌")


# Run program
if __name__ == "__main__":
    main()