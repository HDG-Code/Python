# student_list_system.py

def student_system():
    students = []

    while True:
        print("\n1. Add Student")
        print("2. Show Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            students.append(name)
            print("Student added!")

        elif choice == "2":
            print("\nStudent List:")
            for s in students:
                print("-", s)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


def main():
    student_system()


if __name__ == "__main__":
    main()