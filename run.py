##.pppppcreats Loop that runs the app
task = []

## Function for user to add task
def add_task(new_task):
    task = input('please enter a task: ')
    tasks.append(task)
    print("Task added successfully.")


def list_tasks():
    """
    View tasks in the list
    """
if len(tasks) == 0:
	print('no tasks.')
else:
    print("List of tasks .")
for i, task in enumerate(task):
    print(f'{i+1}. {task}')

def delete_tasks():
    """
    Delete task from the list
    """
    if len(Tasks) == 0:
        print('no tasks to delete.')
    for i, task in enumerate(tasks):

def delete_tasks        
    """
    Delete task from the To-do list
    """
    if len(Tasks) == 0:
        print('no tasks to delete.')
    else:
        print('Tasks')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {tast')
        choice = int(input('Enter task number to delete:'))  

    if 0 < choice <= len(Tasks):
        del Tasks[choice-1]
        print('Task deleted successfully. ')
        else:
            print('Inalid task number. ')

def main():
    """
    Funtion that calls all the Functions to run in the command-line To-do list
    """
###  This creates an infinite loop
while true:

###  This will print an empty line in each iteration of the loop
print('\n-------To-Do-List Application------')

###  Menu options 
print('1. Add a new task')
print('2. list a task')
print('3. Delete a task')
print('4. Quit')

## This calls all the function to perform as they should
choice = int(input("Enter your choice:")) 
if choice == 1:
    add_task()
    elif choice == 2:
         list_tasks()

    elif choice == 3:
        delete a task()

    elif choice == 4:  
        print(Good Luck for using the To-Do-List Application. ') 
        break
    else:
        print('wrong choice. Please try again. ')

if __name__ == '__main__':