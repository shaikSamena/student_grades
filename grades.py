def add_student(students):
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists.")
        return
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return
    students[name] = marks
    print(f"{name} added successfully.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    print("\nName\t\tMarks")
    print("-" * 20)
    for name, marks in students.items():
        print(f"{name}\t\t{marks}")

def update_student(students):
    name = input("Enter student name to update: ").strip()
    if name not in students:
        print("Student not found.")
        return
    try:
        marks = float(input("Enter new marks: "))
    except ValueError:
        print("Invalid marks.")
        return
    students[name] = marks
    print(f"{name}'s marks updated.")

def delete_student(students):
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        print(f"{name} deleted.")
    else:
        print("Student not found.")

def calculate_average(students):
    if not students:
        print("No students to calculate average.")
        return
    avg = sum(students.values()) / len(students)
    print(f"Class Average: {avg:.2f}")
