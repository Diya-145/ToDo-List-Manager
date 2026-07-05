from colorama import Fore, init
from storage import load_tasks
from task_manager import (
    add_task,
    view_tasks,
    mark_completed,
    delete_task,
    search_task,
    show_statistics,
    export_csv
)

init(autoreset=True)

tasks = load_tasks()

while True:

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.GREEN + "        TO-DO LIST MANAGER")
    print(Fore.CYAN + "=" * 45)

    print(Fore.YELLOW + "1. Add Task")
    print(Fore.YELLOW + "2. View Tasks")
    print(Fore.YELLOW + "3. Search Task")
    print(Fore.YELLOW + "4. Mark Task Completed")
    print(Fore.YELLOW + "5. Delete Task")
    print(Fore.YELLOW + "6. Statistics")
    print(Fore.YELLOW + "7. Export Tasks to CSV")
    print(Fore.YELLOW + "8. Exit")

    print(Fore.CYAN + "=" * 45)

    choice = input(Fore.WHITE + "Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        search_task(tasks)

    elif choice == "4":
        mark_completed(tasks)

    elif choice == "5":
        delete_task(tasks)

    elif choice == "6":
        show_statistics(tasks)

    elif choice == "7":
        export_csv(tasks)

    elif choice == "8":
        print(Fore.MAGENTA + "\n👋 Thank you for using To-Do List Manager!")
        break

    else:
        print(Fore.RED + "\n❌ Invalid Choice! Please try again.")