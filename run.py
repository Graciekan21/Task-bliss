# This creates Loop that runs the app

from datetime import datetime

tasks = []
# Enter task and the date you want the task to be done
def add_task():
    task = input("Please enter a task: ")
    due_date_str = input("Please enter a due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        tasks.append({"task": task, "due_date": due_date, "completed": False})
        print(f"Task '{task}' added successfully to the list with due date {due_date.strftime('%Y-%m-%d')}.")
        list_tasks()

            list_tasks()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        add_task()

def list_tasks(filter_status=None):
    if not tasks:
        print("No tasks listed.")
        return
    #If the task is not completed it will pend
    if filter_status == "completed":
        filtered_tasks = [task for task in tasks if task["completed"]]
    elif filter_status == "pending":
        filtered_tasks = [task for task in tasks if not task["completed"]]
    else:
        filtered_tasks = tasks
         if not filtered_tasks:
        print("No tasks found for the selected filter.")
        return
    
    print("Current Tasks:")
    for index, task in enumerate(filtered_tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"Task #{index + 1}: {task['task']} (Due: {task['due_date'].strftime('%Y-%m-%d')}, Status: {status})")

#This handals task delete if task number is enter 
        def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_to_delete < len(tasks):
            deleted_task = tasks.pop(task_to_delete)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
            list_tasks()
             else:
            print(f"Task number {task_to_delete + 1} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def edit_task():
    list_tasks()
    try:
         task_to_edit = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_to_edit < len(tasks):
            new_task = input("Please enter the new task: ")
            new_due_date_str = input("Please enter the new due date (YYYY-MM-DD): ")
            try:

new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d")
                tasks[task_to_edit].update({"task": new_task, "due_date": new_due_date})
                print(f"Task #{task_to_edit + 1} updated successfully.")
list_tasks()
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                edit_task()
        else:
            print(f"Task number {task_to_edit + 1} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def mark_task_completed():
    list_tasks()
    try:
        task_to_mark = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_to_mark < len(tasks):
            tasks[task_to_mark]["completed"] = True
            print(f"Task '{tasks[task_to_mark]['task']}' marked as completed.")
            list_tasks()
        else:
            print(f"Task number {task_to_mark + 1} not 

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
        task_to_delete = int(input("Enter the task number to delete: \n")) - 1
        if 0 <= task_to_delete < len(tasks):
            deleted_task = tasks.pop(task_to_delete)
            print(f"Task '{deleted_task}' deleted successfully.")
            list_tasks()  # Show the updated list to the user
        else:
            print(f"Task number {task_to_delete + 1} not found.")
    except ValueError:
        print("Invalid input. Please enter a task number.\n")

        found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
#Options Available for the To-Do List
def main():
    print("To-Do List Application")
    while True:
        print("\nAvailable options:")
        print("=========================")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. List completed tasks")
        print("4. List pending tasks")
        print("5. Delete a task")
        print("6. Edit a task")
        print("7. Mark task as completed")
        print("8. Quit")
        try:

            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                list_tasks()
            elif choice == 3:
                list_tasks(filter_status="completed")
            elif choice == 4:
                list_tasks(filter_status="pending")
            elif choice == 5:
                delete_task()
            elif choice == 6:
                edit_task()
            elif choice == 7:
                mark_task_completed()
            elif choice == 8:
                confirm_exit = input("Are you sure you want to quit? (yes/no): ").lower()
                if confirm_exit == "yes":
                    print("Exiting the application. Goodbye!")
                        break
                else:
                    continue
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")

if _name_ == "_main_":
    main()
