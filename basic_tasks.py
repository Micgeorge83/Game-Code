#Define a list to store tasks.
tasks = []
#Create a function to add a task to the list.
def add_task(tasks):
    task = input("Enter a task to add: ")
    tasks.append(task)

#Create a function to delete a task from the list.
def delete_task(tasks):
    task_to_delete = input("Enter task to delete: ")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
    else:
        print("task not found")

#Create a function to view all tasks in the list.   
def display_menu():
    print("1. Add a task")
    print("2. View task")
    print("3. Delete a task")
    print("4. Exit")
    choice = input("Select an option from menu: ")
    return choice 

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")


#Create a loop to keep the application running until the user chooses to exit.
while True:
    choice = display_menu()

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Exiting......see yas!")
        break
    else:
        print("None of that was valid, put the bong down and try again")
