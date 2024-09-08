# To-Do List Application that we can update
#   3 Functions:
#       Add a task
#       Remove a task
#       Show all tasks in queue

#TODO: Create a database to hold tasks for when user quits

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
        for index, task in enumerate(tasks, start=1):   # we create a for loop for tasks with an index starting at 1 that increases with each loop
            print(f"{index}. {task}")                   # Print each task with the format of index number followed by task name
    else:
        print("Your to-do list is empty")               # Print if the tasks list has no content

# SHOW USER OPTIONS
def get_display_choice():
    return input("Enter 'A' to add a task, 'R' to remove a task, 'D' to display all tasks, or 'Q' to quit:  ").upper() # upper() changes it so the input will always be uppercase


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
        elif choice == 'Q':
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
