# ==========================================
# Persistent Task Management Application
# ==========================================

import os

class Task:
    """Represents a single task with an ID, title, description, and status."""
    
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = int(task_id)
        self.title = title
        self.description = description
        self.status = status

    def display(self):
        """Prints the task details neatly."""
        print(f"[{self.task_id}] {self.title} | Status: {self.status}")
        print(f"    Description: {self.description}")

    def to_file_string(self):
        """Formats the task as a single line for the text file."""
        # We use a pipe (|) as a delimiter instead of a comma to avoid 
        # breaking if the user types a comma in their description.
        return f"{self.task_id}|{self.title}|{self.description}|{self.status}\n"


class TaskManager:
    """Handles CRUD operations and File I/O for tasks."""
    
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        
        # Automatically load tasks when the manager is created
        self.load_tasks()

    def load_tasks(self):
        """Reads tasks from the text file into the tasks list."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    # Remove the newline character and split by our delimiter
                    parts = line.strip().split('|')
                    
                    # Ensure the line has exactly 4 parts to avoid corrupted data
                    if len(parts) == 4:
                        task_id, title, desc, status = parts
                        task = Task(task_id, title, desc, status)
                        self.tasks.append(task)
                        
                        # Ensure the next_id is always higher than the highest loaded ID
                        if task.task_id >= self.next_id:
                            self.next_id = task.task_id + 1
                            
            print(f"--- Successfully loaded {len(self.tasks)} tasks from {self.filename} ---")
            
        except FileNotFoundError:
            # It's perfectly fine if the file doesn't exist yet (e.g., first run)
            print(f"--- No existing {self.filename} found. Starting fresh! ---")
        except PermissionError:
            print(f"--- Error: Permission denied to read {self.filename}. ---")
        except Exception as e:
            print(f"--- Error loading file: Corrupted data or unknown issue ({e}) ---")

    def save_tasks(self):
        """Writes all current tasks back to the text file."""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task.to_file_string())
        except PermissionError:
            print(f"\nCritical Error: Permission denied to save to {self.filename}.")
        except Exception as e:
            print(f"\nCritical Error saving tasks: {e}")

    def create_task(self, title, description):
        """Creates a new task, adds it, and saves to the file."""
        new_task = Task(self.next_id, title, description)
        self.tasks.append(new_task)
        print(f"\nSuccess: Task '{title}' added with ID {self.next_id}.")
        self.next_id += 1
        self.save_tasks() # Trigger save

    def read_tasks(self):
        """Displays all tasks."""
        if not self.tasks:
            print("\nNo tasks available. Your to-do list is empty!")
            return
        
        print("\n--- Current Tasks ---")
        for task in self.tasks:
            task.display()
            print("-" * 21)

    def get_task_by_id(self, task_id):
        """Helper method to find a task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task(self, task_id):
        """Updates a task and saves changes to the file."""
        task = self.get_task_by_id(task_id)
        
        if task:
            print(f"\nUpdating Task [{task.task_id}] (Leave blank to keep current value)")
            
            new_title = input(f"New Title ({task.title}): ").strip()
            if new_title:
                task.title = new_title
                
            new_desc = input(f"New Description ({task.description}): ").strip()
            if new_desc:
                task.description = new_desc
                
            new_status = input(f"New Status ({task.status}) [Pending/Completed]: ").strip().capitalize()
            if new_status in ["Pending", "Completed"]:
                task.status = new_status
                
            print(f"Success: Task [{task.task_id}] has been updated.")
            self.save_tasks() # Trigger save
        else:
            print(f"\nError: Task with ID {task_id} does not exist.")

    def delete_task(self, task_id):
        """Removes a task and updates the file."""
        task = self.get_task_by_id(task_id)
        
        if task:
            self.tasks.remove(task)
            print(f"\nSuccess: Task [{task_id}] has been deleted.")
            self.save_tasks() # Trigger save
        else:
            print(f"\nError: Task with ID {task_id} does not exist.")


def main():
    manager = TaskManager()

    while True:
        print("\n=== Persistent Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            desc = input("Enter task description: ").strip()
            if title:
                manager.create_task(title, desc)
            else:
                print("\nError: Task title cannot be empty.")
        elif choice == '2':
            manager.read_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter the ID of the task to update: "))
                manager.update_task(task_id)
            except ValueError:
                print("\nError: Please enter a valid numeric ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter the ID of the task to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("\nError: Please enter a valid numeric ID.")
        elif choice == '5':
            print("\nExiting Task Manager. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()