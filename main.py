from grades import add_student, view_students, update_student, delete_student, calculate_average

students = {}

while True:
    print("\n--- Student Grade Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Calculate Average")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        update_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        calculate_average(students)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
