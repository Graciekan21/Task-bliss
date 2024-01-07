# This creates Loop that runs the app
tasks = []
def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully to the list.")
    list_tasks()  # Show the updated list to the user
def list_tasks():
    if not tasks:
        print("No tasks listed.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index + 1}: {task}")
def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_to_delete < len(tasks):
            deleted_task = tasks.pop(task_to_delete)
            print(f"Task '{deleted_task}' deleted successfully.")
            list_tasks()  # Show the updated list to the user
        else:
            print(f"Task number {task_to_delete + 1} not found.")
    'except' ValueError:
        print("Invalid input. Please enter a task number.")
def main():
    print("To-Do List Application")
    while True:
        print("\n")
        print("Available options:")
        print("=========================")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Delete a task")
        print("4. Quit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                list_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                confirm_exit = input(
                    "Are you sure you want to quit? (yes/no): ").lower()
                if confirm_exit == 'yes':
                    print("Exiting the application. Goodbye!")
                    break
                else:
                    continue
            else:
                print("Invalid choice. Please try again.")
        'except' ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
if _name_ == "_main_":
    main()
