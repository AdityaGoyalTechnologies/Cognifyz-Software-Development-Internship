# ==========================================
# Task Management Console Application
# ==========================================

class Task:
    """Represents a single task with an ID, title, description, and status."""
    
    def __init__(self, task_id, title, description):
        # The constructor initializes the task's attributes
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"  # Default status for a new task

    def display(self):
        """Prints the task details in a readable, formatted way."""
        print(f"[{self.task_id}] {self.title} | Status: {self.status}")
        print(f"    Description: {self.description}")


class TaskManager:
    """Handles the CRUD operations for a list of Task objects."""
    
    def __init__(self):
        self.tasks = []      # List to store Task objects
        self.next_id = 1     # Automatically increments to assign unique IDs

    def create_task(self, title, description):
        """Creates a new task and adds it to the list."""
        new_task = Task(self.next_id, title, description)
        self.tasks.append(new_task)
        print(f"\nSuccess: Task '{title}' added with ID {self.next_id}.")
        self.next_id += 1

    def read_tasks(self):
        """Displays all tasks. Shows a message if the list is empty."""
        if not self.tasks:
            print("\nNo tasks available. Your to-do list is empty!")
            return
        
        print("\n--- Current Tasks ---")
        for task in self.tasks:
            task.display()
            print("-" * 21)

    def get_task_by_id(self, task_id):
        """Helper method to find a task by its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None # Returns None if the ID doesn't exist

    def update_task(self, task_id):
        """Updates an existing task's attributes."""
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
            elif new_status != "":
                print("Invalid status entered. Status remains unchanged.")
                
            print(f"Success: Task [{task.task_id}] has been updated.")
        else:
            print(f"\nError: Task with ID {task_id} does not exist.")

    def delete_task(self, task_id):
        """Removes a task from the list using its ID."""
        task = self.get_task_by_id(task_id)
        
        if task:
            self.tasks.remove(task)
            print(f"\nSuccess: Task [{task_id}] has been deleted.")
        else:
            print(f"\nError: Task with ID {task_id} does not exist.")


def main():
    """Main function to run the console menu."""
    manager = TaskManager()

    while True:
        print("\n=== Task Manager Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            desc = input("Enter task description: ").strip()
            if title: # Ensure the title isn't completely empty
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

# This ensures the program runs automatically when executed directly
if __name__ == "__main__":
    main()