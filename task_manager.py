from storage import save_tasks
from colorama import Fore


def add_task(tasks):
    task = input("Enter task: ").strip()

    if task == "":
        print(Fore.RED + "❌ Task cannot be empty!")
        return

    print("\nPriority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_choice = input("Choose priority: ")

    priority = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }.get(priority_choice, "Medium")

    due_date = input("Enter Due Date (DD/MM/YYYY): ")

    tasks.append({
        "task": task,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })

    save_tasks(tasks)

    print(Fore.GREEN + "\n✅ Task Added Successfully!")


def view_tasks(tasks):

    if not tasks:
        print(Fore.RED + "\n📌 No Tasks Found.")
        return

    print(Fore.CYAN + "\n" + "=" * 90)
    print(f"{'ID':<5}{'Status':<10}{'Priority':<10}{'Due Date':<15}Task")
    print(Fore.CYAN + "=" * 90)

    for i, task in enumerate(tasks, start=1):

        status = "✅" if task["completed"] else "❌"

        print(
            f"{i:<5}{status:<10}{task['priority']:<10}{task.get('due_date','-'):<15}{task['task']}"
        )

    print(Fore.CYAN + "=" * 90)


def mark_completed(tasks):

    if not tasks:
        print(Fore.RED + "\n📌 No Tasks Available.")
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
        print(Fore.RED + "\n📌 No Tasks Available.")
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


def search_task(tasks):

    keyword = input("\nEnter keyword: ").lower()

    found = False

    for i, task in enumerate(tasks, start=1):

        if keyword in task["task"].lower():

            status = "✅" if task["completed"] else "❌"

            print(
                f"{i}. {status} | {task['priority']} | {task.get('due_date', '-')} | {task['task']}"
            )

            found = True

    if not found:

        print(Fore.RED + "❌ No matching task found.")


def show_statistics(tasks):

    total = len(tasks)

    completed = sum(task["completed"] for task in tasks)

    pending = total - completed

    print(Fore.CYAN + "\n" + "=" * 35)
    print(Fore.GREEN + "        TASK STATISTICS")
    print(Fore.CYAN + "=" * 35)

    print(Fore.YELLOW + f"📌 Total Tasks : {total}")
    print(Fore.GREEN + f"✅ Completed   : {completed}")
    print(Fore.RED + f"❌ Pending     : {pending}")

    print(Fore.CYAN + "=" * 35)