from storage import save_tasks
from colorama import Fore


def add_task(tasks):
    task = input("Enter task: ").strip()

    if task == "":
        print(Fore.RED + "❌ Task cannot be empty!")
        return

    print(Fore.CYAN + "\nSelect Priority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_choice = input("Choose priority: ")

    priority = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }.get(priority_choice, "Medium")

    tasks.append({
        "task": task,
        "priority": priority,
        "completed": False
    })

    save_tasks(tasks)

    print(Fore.GREEN + "\n✅ Task Added Successfully!\n")


def view_tasks(tasks):

    if not tasks:
        print(Fore.RED + "\n📌 No Tasks Found.\n")
        return

    print(Fore.CYAN + "\n" + "=" * 65)
    print(f"{'ID':<5}{'Status':<10}{'Priority':<12}Task")
    print("=" * 65)

    for index, task in enumerate(tasks, start=1):

        status = "✅" if task["completed"] else "❌"

        print(
            f"{index:<5}{status:<10}{task['priority']:<12}{task['task']}"
        )

    print(Fore.CYAN + "=" * 65)


def mark_completed(tasks):

    if not tasks:
        print(Fore.RED + "\n📌 No Tasks Available.\n")
        return

    view_tasks(tasks)

    try:
        num = int(input("\nEnter task number to mark as completed: "))

        if 1 <= num <= len(tasks):

            tasks[num - 1]["completed"] = True
            save_tasks(tasks)

            print(Fore.GREEN + "\n✅ Task Marked as Completed!")

        else:
            print(Fore.RED + "\n❌ Invalid Task Number.")

    except ValueError:
        print(Fore.RED + "\n❌ Please enter a valid number.")


def delete_task(tasks):

    if not tasks:
        print(Fore.RED + "\n📌 No Tasks Available.\n")
        return

    view_tasks(tasks)

    try:
        num = int(input("\nEnter task number to delete: "))

        if 1 <= num <= len(tasks):

            removed = tasks.pop(num - 1)
            save_tasks(tasks)

            print(Fore.GREEN + f"\n🗑️ '{removed['task']}' deleted successfully!")

        else:
            print(Fore.RED + "\n❌ Invalid Task Number.")

    except ValueError:
        print(Fore.RED + "\n❌ Please enter a valid number.")