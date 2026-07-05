from storage import load_tasks
from task_manager import (
    add_task,
    view_tasks,
    mark_completed,
    delete_task
)

tasks = load_tasks()

while True:

    print("\n" + "=" * 40)
    print("      TO-DO LIST MANAGER")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 40)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        mark_completed(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("\nThank you for using To-Do List Manager!")
        break

    else:
        print("\nInvalid Choice! Please try again.")