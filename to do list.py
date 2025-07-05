tasks = []

def show_menu():

    print("\n--- To-Do List Menu --")
    print('1. Add tasks')
    print('2. View Tasks')
    print('3. Delete Tasks')
    print('4. Exit\n\n')

def add():
    task = input('Enter the task: ')
    tasks.append(task)
    print('task added')

def view():
    if not tasks:
        print('No tasks in the list.')
    else:
        print('\n Your Tasks')
        for i, task in enumerate(tasks, start = 1):
            print(f'{i}. {task}')

def delete():
    view()
    if tasks:
        num = int(input('Enter task no: '))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: '{removed}'")
        else:
            print("Invalid task no.")


while True:
    show_menu()
    choice = int(input('Choose an option (1-4): '))

    if choice == 1:
        add()

    elif choice == 2:
        view()
    elif choice == 3:
        delete()
    elif choice == 4:
        print('Exiting, GoodBye!')
        break
    else:
        print('Invalid choice. Please try again')