from storage import save_tasks


def add_task(tasks):
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty!")
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

    tasks.append({
        "task": task,
        "priority": priority,
        "completed": False
    })

    save_tasks(tasks)

    print("\n✅ Task Added Successfully!\n")


def view_tasks(tasks):

    if not tasks:
        print("\n📌 No Tasks Found.\n")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<5}{'Status':<10}{'Priority':<10}Task")
    print("=" * 60)

    for index, task in enumerate(tasks, start=1):

        status = "✅" if task["completed"] else "❌"

        print(
            f"{index:<5}{status:<10}{task['priority']:<10}{task['task']}"
        )

    print("=" * 60)


def mark_completed(tasks):

    if not tasks:
        print("\n📌 No Tasks Available.\n")
        return

    view_tasks(tasks)

    try:

        num = int(input("\nEnter task number to mark as completed: "))

        if 1 <= num <= len(tasks):

            tasks[num - 1]["completed"] = True

            save_tasks(tasks)

            print("\n✅ Task Marked as Completed!")

        else:

            print("\n❌ Invalid Task Number.")

    except ValueError:

        print("\n❌ Please enter a valid number.")


def delete_task(tasks):

    if not tasks:
        print("\n📌 No Tasks Available.\n")
        return

    view_tasks(tasks)

    try:

        num = int(input("\nEnter task number to delete: "))

        if 1 <= num <= len(tasks):

            removed = tasks.pop(num - 1)

            save_tasks(tasks)

            print(f"\n🗑️ '{removed['task']}' deleted successfully!")

        else:

            print("\n❌ Invalid Task Number.")

    except ValueError:

        print("\n❌ Please enter a valid number.")