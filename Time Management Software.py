import json
import datetime
import os

TASKS_FILE = "tasks.json"

# Task Class to represent a single task
class Task:
    def __init__(self, title, description, due_date, priority, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date  # Format: 'YYYY-MM-DD'
        self.priority = priority  # 1 (High), 2 (Medium), 3 (Low)
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["description"],
            data["due_date"],
            data["priority"],
            data["completed"],
        )

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return (
            f"{status} | Title: {self.title} | Due: {self.due_date} | "
            f"Priority: {self.priority} | Description: {self.description}"
        )


# TaskManager Class to manage the list of tasks
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks_data]

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def list_tasks(self, sort_by="due_date"):
        if not self.tasks:
            print("No tasks available.")
            return

        if sort_by == "due_date":
            self.tasks.sort(key=lambda t: t.due_date)
        elif sort_by == "priority":
            self.tasks.sort(key=lambda t: t.priority)

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{deleted_task.title}' deleted successfully!")
        else:
            print("Invalid task number.")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Time Management System ---")
        print("1. Add Task")
        print("2. List Tasks (by due date)")
        print("3. List Tasks (by priority)")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            due_date = input("Due Date (YYYY-MM-DD): ").strip()
            priority = int(input("Priority (1-High, 2-Medium, 3-Low): ").strip())
            manager.add_task(title, description, due_date, priority)

        elif choice == "2":
            manager.list_tasks(sort_by="due_date")

        elif choice == "3":
            manager.list_tasks(sort_by="priority")

        elif choice == "4":
            manager.list_tasks()
            task_number = int(input("Enter the task number to mark as completed: ").strip())
            manager.mark_task_completed(task_number)

        elif choice == "5":
            manager.list_tasks()
            task_number = int(input("Enter the task number to delete: ").strip())
            manager.delete_task(task_number)

        elif choice == "6":
            print("Exiting the Time Management System. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
