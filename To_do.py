from asyncio import tasks
from collections import namedtuple
import json

# Task data structure
Task = namedtuple("Task", ["description", "priority", "completed", "deadline"])

# Load data from JSON file
def load_data():
    try:
        with open("todo.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save data to JSON file
def save_data(tasks):
    with open("todo.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Print all tasks
def list_tasks(tasks):
    for i, task in enumerate(tasks):
        marker = "*" if task.completed else " "
        priority = "**HIGH**" if task.priority == "high" else (
            "**MEDIUM**" if task.priority == "medium" else "**LOW**"
        )
        deadline = f" (due {task.deadline})" if task.deadline else ""
        print(f"{i+1}. {marker} {priority} {task.description}{deadline}")

# Add a new task
def add_task():
    description = input("Enter task description: ")
    priority = input("Enter priority (high, medium, low): ").lower()
    deadline = input("Enter deadline (optional): ")
    task = Task(description, priority, False, deadline)
    tasks.append(task)
    save_data(tasks)

# Edit a task
def edit_task():
    try:
        task_id = int(input("Enter task ID to edit: ")) - 1
        task = tasks[task_id]
        new_description = input("Enter new description (optional): ") or task.description
        new_priority = input("Enter new priority (optional): ") or task.priority
        new_deadline = input("Enter new deadline (optional): ") or task.deadline
        task = Task(new_description, new_priority, task.completed, new_deadline)
        tasks[task_id] = task
        save_data(tasks)
    except (IndexError, ValueError):
        print("Invalid task ID.")

# Mark a task as complete
def complete_task():
    try:
        task_id = int(input("Enter task ID to mark complete: ")) - 1
        task = tasks[task_id]
        task = Task(task.description, task.priority, True, task.deadline)
        tasks[task_id] = task
        save_data(tasks)
    except (IndexError, ValueError):
        print("Invalid task ID.")

# Delete a task
def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: ")) - 1
        del tasks[task_id]
        save_data(tasks)
    except (IndexError, ValueError):
        print("Invalid task ID.")

# Main menu
def main():
    print("Welcome to your To-Do List!")
    tasks = load_data()
    while True:
        print("\nOptions:")
        print("1. List tasks")
        print("2. Add a task")
        print("3. Edit a task")
        print("4. Mark a task complete")
        print("5. Delete a task")
        print("6. Quit")
        choice = input("> ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
