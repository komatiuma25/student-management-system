import json
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------- DATA ----------------
students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file)

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []

# ---------------- FUNCTIONS ----------------

def refresh_table(data=None):
    for row in tree.get_children():
        tree.delete(row)

    display_data = data if data else students

    for s in display_data:
        tree.insert("", tk.END, values=(s["id"], s["name"], s["marks"]))


def add_student():
    name = name_entry.get()
    marks = marks_entry.get()

    if name == "" or not marks.isdigit():
        messagebox.showerror("Error", "Enter valid data")
        return

    student = {
        "id": len(students) + 1,
        "name": name,
        "marks": int(marks)
    }

    students.append(student)
    save_students()
    refresh_table()

    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


def delete_student():
    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    item = tree.item(selected[0])
    student_id = item["values"][0]

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            break

    save_students()
    refresh_table()


def update_student():
    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    item = tree.item(selected[0])
    student_id = item["values"][0]

    for s in students:
        if s["id"] == student_id:
            student = s
            break

    # Popup
    win = tk.Toplevel(root)
    win.title("Edit Student")
    win.geometry("300x200")
    win.configure(bg="#2c3e50")

    tk.Label(win, text="Name", bg="#2c3e50", fg="white").pack(pady=5)
    name_edit = tk.Entry(win)
    name_edit.pack()
    name_edit.insert(0, student["name"])

    tk.Label(win, text="Marks", bg="#2c3e50", fg="white").pack(pady=5)
    marks_edit = tk.Entry(win)
    marks_edit.pack()
    marks_edit.insert(0, student["marks"])

    def save_changes():
        name = name_edit.get()
        marks = marks_edit.get()

        if name == "" or not marks.isdigit():
            messagebox.showerror("Error", "Invalid input")
            return

        student["name"] = name
        student["marks"] = int(marks)

        save_students()
        refresh_table()
        win.destroy()

    tk.Button(win, text="Save", bg="#27ae60", fg="white",
              command=save_changes).pack(pady=10)


def search_student():
    keyword = search_entry.get().lower()

    filtered = [s for s in students if keyword in s["name"].lower()]
    refresh_table(filtered)

# ---------------- GUI ----------------

load_students()

root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")
root.configure(bg="#ecf0f1")

# -------- Title --------
tk.Label(root, text="Student Management System",
         font=("Arial", 16, "bold"),
         bg="#ecf0f1").pack(pady=10)

# -------- Input Frame --------
frame = tk.Frame(root, bg="#ecf0f1")
frame.pack(pady=10)

tk.Label(frame, text="Name", bg="#ecf0f1").grid(row=0, column=0, padx=10)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Marks", bg="#ecf0f1").grid(row=1, column=0, padx=10)
marks_entry = tk.Entry(frame)
marks_entry.grid(row=1, column=1)

tk.Label(frame, text="Search", bg="#ecf0f1").grid(row=2, column=0, padx=10)
search_entry = tk.Entry(frame)
search_entry.grid(row=2, column=1)

tk.Button(frame, text="Search", bg="#3498db", fg="white",
          command=search_student).grid(row=3, column=0, columnspan=2, pady=5)

# -------- Buttons --------
btn_frame = tk.Frame(root, bg="#ecf0f1")
btn_frame.pack()

tk.Button(btn_frame, text="Add", width=10, bg="#2ecc71", fg="white",
          command=add_student).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Update", width=10, bg="#f39c12", fg="white",
          command=update_student).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=10, bg="#e74c3c", fg="white",
          command=delete_student).grid(row=0, column=2, padx=5)

# -------- Table --------
columns = ("ID", "Name", "Marks")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(pady=10, fill="both", expand=True)

refresh_table()

root.mainloop()