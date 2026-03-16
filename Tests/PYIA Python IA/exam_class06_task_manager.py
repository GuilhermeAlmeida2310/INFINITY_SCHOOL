tasks = []

def add_task(tasks, task_name):
    task = {
        "task": task_name,
        "status": False
    }
    tasks.append(task)
    print(f'{task_name} was added in your list!')

def look_tasks(tasks):
    print('==== LIST OF TASKS =====')

    for i, task in enumerate(tasks, start=1):
        status = 'X' if task["status"] else " "
        task_name = task["task"]
        print(f'{i}. [{status}] {task_name}')

def task_update(tasks, index_task, update_name):
    adjusted_task_index = index_task - 1

    if adjusted_task_index >= 0 and adjusted_task_index < len(tasks):
        tasks[adjusted_task_index]["task"] = update_name
        print(f'{index_task} was swapped for {update_name}')

    else:
        print('The index is invalid!')

def finish_task(tasks, index_task):
    adjusted_task_index = index_task - 1

    if adjusted_task_index >= 0 and adjusted_task_index < len(tasks):
        tasks[adjusted_task_index]["status"] = True
        print(f'The task: {index_task} was completed!')
    
    else:
        print('The index is invalid!')

def del_completed_task(tasks):
    for task in tasks:

        if task["status"] == True:
            tasks.remove(task)

    print('Were deleted from your task list!')


def menu():
    while True:
        print('==== MENU ====')
        print('1. Add Task')
        print('2. Look Task')
        print('3. Update Task')
        print('4. Conclude Task')
        print('5. Delete Completed Task')
        print('6. Exit')

        option = int(input('Choose an option: '))

        if option == 1:
            task_name = input('Insert the task name: ')
            add_task(tasks, task_name)

        elif option == 2:
            look_tasks(tasks)

        elif option == 3:
            look_tasks(tasks)
            index_task = int(input('Insert the task number than you want update: '))
            update_name = input('Insert the new task name: ')
            task_update(tasks, index_task, update_name)

        elif option == 4:
            look_tasks(tasks)
            index_task = int(input('Insert the number of task than you completed: '))
            finish_task(tasks, index_task)

        elif option == 5:
            del_completed_task(tasks)
            look_tasks(tasks)

        elif option == 6:
            print('Exiting program...')
            break

        else:
            print('Insert a valid option please!')
            continue

menu()