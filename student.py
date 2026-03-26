import json

students = []

def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    if not marks.isdigit():
        print("❌ Marks must be a number")
        return
    if name.strip() == "":
        print("❌ Name cannot be empty")
        return  
    student = {
        'id': len(students) + 1,
        "name": name,
        "marks": int(marks)
    }

    students.append(student)
    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("No students found")
    else:
        for  s in enumerate(students):
            print(f"ID:{s['id']} | Name: {s['name']} | Marks: {s['marks']}")

def search_student():
    sid = int(input("Enter ID to search: "))

    for s in students:
        if s["id"] == sid:
            print(f"Found: {s}")
            return

    print("❌ Student not found")

def delete_student():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("🗑️ Student deleted")
            return

    print("❌ Student not found")

def save_to_file():
    with open("students.json", "w") as f:
        json.dump(students, f)

def load_from_file():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except:
        students = []

def menu():
    load_from_file()

    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_to_file()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice")

menu()