# To-Do List Application that we can update
#   3 Functions:
#       Add a task
#       Remove a task
#       Show all tasks in queue

# String list to keep track of our tasks
tasks = []

# ADD A TASK
def add_task():
    task = input("Enter task to add: ")
    tasks.append(task)
    print("Task added succcessfully!")

# REMOVE A TASK
def rem_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found.")

# SHOW TASK QUEUE
def display_tasks():
    if tasks:                                           # Check if the tasks list has content
        print("Your to-do list")
        for index, task in enumerate(tasks, start=1):   # we create a for loop, have an index enumerate through each task in tasks, starting at the 1st entry
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty")

# SHOW USER OPTIONS
def get_display_choice():
    return input("Enter 'A' to add a task, 'R' to remove a task, or 'D' to display all tasks").upper()


# MAIN FUNCTION
def main():
    while True:
        choice = get_display_choice()
        if choice == 'A':
            add_task()
        elif choice == 'R':
            rem_task()
        elif choice == 'D':
            display_tasks()
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
