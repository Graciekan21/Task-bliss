"""
ToDo List App

This implements a command-line to-do list App
that is functional for tasks.

How to use:
- Follow the script to start the Todo List App.

Functions:
"""
## creats Loop that runs the app
task = []

## Function for user to add task
def add_task(new_task):
    task = input('please enter a task: ')
    tasks.appen(task)
    print(f'task '{Task}' added to the list.')

def main():
	    print('To-do list')
	    add_task('Take kids to school')
	    add_task('Bake cakes that where ordered', )
        
	    
if __name__ == '__main__':

## This creates an infinite loop
print("welcome to do list app ")
while true:

## This will print an empty line in each iteration of the loop
print('\n')
print('Select one of the options bellow')
print('-----------')

## Menu options 
print('1. Add a new task')
print('2. Delete a task')
print('3. List tasks')
print('4. Quit')
