import sqlite3
from tabulate import tabulate

# ---------------------------
# Database Setup
# ---------------------------
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    deadline TEXT,
    status TEXT DEFAULT 'Pending'
)
""")
conn.commit()


# ---------------------------
# Functions
# ---------------------------
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO tasks (title, description, deadline) VALUES (?, ?, ?)",
        (title, description, deadline)
    )
    conn.commit()
    print("✅ Task added successfully!")


def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    if rows:
        print(tabulate(rows, headers=["ID", "Title", "Description", "Deadline", "Status"], tablefmt="grid"))
    else:
        print("⚠️ No tasks found.")


def update_task():
    task_id = input("Enter task ID to update: ")
    new_title = input("Enter new title: ")
    new_description = input("Enter new description: ")
    new_deadline = input("Enter new deadline (YYYY-MM-DD): ")

    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, deadline = ? WHERE id = ?",
        (new_title, new_description, new_deadline, task_id)
    )
    conn.commit()
    print("✅ Task updated successfully!")


def mark_completed():
    task_id = input("Enter task ID to mark as completed: ")
    cursor.execute("UPDATE tasks SET status = 'Done' WHERE id = ?", (task_id,))
    conn.commit()
    print("✅ Task marked as completed!")


def delete_task():
    task_id = input("Enter task ID to delete: ")
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("🗑️ Task deleted successfully!")


# ---------------------------
# Main Menu
# ---------------------------
while True:
    print("\n====== Task Manager ======")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("👋 Exiting Task Manager. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter a number from 1 to 6.")
