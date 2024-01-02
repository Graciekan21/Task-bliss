##.This creats Loop that runs the app
tasks = []

## Function for user to add task
def add_task():
    new_task = input('please enter a task: ')
    tasks.append(new_task)
    print("Task added successfully.")


def list_tasks():
    """
    View tasks in the list
    """
if len(tasks) == 0:
	print('=====To-Do List=====')
else:
    print("List of tasks:")
for i, task in enumerate(tasks):
    print(f'{i+1}. {task}')

## Delete task from the To-do list

def delete_task(): 
    list_tasks() 
    try:
        taskToDelete = int(input('Enter the number to delete: '))
    if taskToDelete >=0 and taskToDelete < len(tasks):
        tasks.pop(taskToDelete)
    
        print(f'Task {taskToDelete} deleted successfully. ')
    else:
        print(f'Task number{task} not found.')    
    except:
        print('lnvalid input.')

def main():
    """
    Funtion that calls all the Functions to run in the command-line To-do list
    """

###  This creates an infinite loop

while True:
    print('1. Add a new task')
    print('2. List a task')
    print('3. Delete a task')
    print('4. Quit')
    ## This calls all the function to perform as they should
    choice = int(input("Enter your choice: ")) 

    if choice == 1:
        add_task()
    elif choice == 2:
        list_tasks()

    elif choice == 3:
        
        delete_task()

    elif choice == 4: 
        print('Good Luck using the To-Do-List Application.')


    else:
        print('Invalid choice. Please try again. ')

if __name__ == '__main__':
    main()