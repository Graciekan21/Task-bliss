# creats Loop that runs the app
task = []

# function user to add task
def add_task(new_task):
    task = input('please enter a task: ')
    print(f'task added: {new_task}')

if __name__ == '__main__':

# This creates an infinite loop
print("welcome to do list app !")
while true:

# This will print an empty line in each iteration of the loop
print('\n')
print('Select one of the options bellow')
print('-----------')

## Menu options 
print('1. Add a new task')
print('2. Delete a task')
print('3. List tasks')
print('4. Quit')
