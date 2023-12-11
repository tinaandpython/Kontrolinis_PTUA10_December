from datetime import datetime

tasks = []
dates = []

def add_task():
    task = input("Enter a task: \n")
    tasks.append(task)

    while True:
        try:
            date = input("Enter a date (YYYY-MM-DD): \n")
            valid_date = datetime.strptime(date, '%Y-%m-%d')
            dates.append(valid_date)
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'YYYY-MM-DD'.")
        else:
            break

    global task_list # indicating modification of a global variable
    task_list = dict(zip(tasks, dates))


def display_tasks():
    task_num = 0

    for key, value in task_list.items():
        task_num += 1
        print(f"{task_num}. {key} due date: {value}")


def delete_task():
    x = int(input("Enter a task number: "))
    task_list.pop(tasks[x - 1])


def edit_task():
    e = int(input("Enter a task number: \n"))
    new_task = input("Enter a new task: \n")
    # new_date = input("Enter a date (YYYY-MM-DD): \n")
    # formatted_date = datetime.strptime(new_date, '%Y-%m-%d')

    global task_list
    task_list[new_task] = task_list.pop(tasks[e - 1])
    # task_list[new_date] = task_list.pop(dates[e - 1])

    tasks[e - 1] = new_task
    # dates[e - 1] = formatted_date


def mark_task_completed():
    t = int(input("Enter a task number: "))
    completed_task = tasks[t -1]
    task_list[completed_task] = task_list[completed_task].strftime('%Y-%m-%d') + " --> COMPLETED"
    # a path from the index given by the user to the ending of the value in a dict


def search_tasks():
    task_to_find = input("Enter the name of the task: \n")

    for key, value in task_list.items():
        if key == task_to_find:
            print(f"{key} due date: {value}")
        else:
            print("Task not found")


def main():
   while True:
       print("\nTo-Do List Options:")
       print("1. Add task")
       print("2. Display tasks")
       print("3. Mark task as completed (BONUS)")
       print("4. Delete task")
       print("5. Search task (BONUS)")
       print("6. Edit task (BONUS)")
       print("7. QUIT")
       option = int(input('Enter your choice: '))
       if option == 1:
           add_task()
       elif option == 2:
           display_tasks()
       elif option == 3:
           mark_task_completed()
       elif option == 4:
           delete_task()
       elif option == 5:
           search_tasks()
       elif option == 6:
           edit_task()
       elif option == 7:
           print('Exiting task list!')
           exit()
       else:
           print('Invalid option. Please enter a number between 1 and 6.')

main()