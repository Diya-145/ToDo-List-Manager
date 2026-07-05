from colorama import Fore, Style, init
from storage import load_tasks
from task_manager import (
    add_task,
    view_tasks,
    mark_completed,
    delete_task
)

# Initialize Colorama
init(autoreset=True)

# Load tasks from JSON
tasks = load_tasks()

while True:

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.GREEN + "        TO-DO LIST MANAGER")
    print(Fore.CYAN + "=" * 45)

    print(Fore.YELLOW + "1. Add Task")
    print(Fore.YELLOW + "2. View Tasks")
    print(Fore.YELLOW + "3. Mark Task Completed")
    print(Fore.YELLOW + "4. Delete Task")
    print(Fore.YELLOW + "5. Exit")

    print(Fore.CYAN + "=" * 45)

    choice = input(Fore.WHITE + "Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        mark_completed(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print(Fore.MAGENTA + "\n👋 Thank you for using To-Do List Manager!")
        break

    else:
        print(Fore.RED + "\n❌ Invalid Choice! Please try again.")