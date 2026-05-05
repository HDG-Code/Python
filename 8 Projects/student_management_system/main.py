# student_management_system/main.py

students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added!")

def view_students():
    print("\n--- Students ---")
    for s in students:
        print("-", s)

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()