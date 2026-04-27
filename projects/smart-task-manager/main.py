from task_manager import TaskManager

def menu():
    print("\n===== SMART TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Show Stats")
    print("6. Exit")

def main():
    tm = TaskManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task title: ")
            tm.add_task(title)

        elif choice == "2":
            tm.show_tasks()

        elif choice == "3":
            tm.show_tasks()
            idx = int(input("Task ID to complete: "))
            tm.complete_task(idx)

        elif choice == "4":
            tm.show_tasks()
            idx = int(input("Task ID to delete: "))
            tm.delete_task(idx)

        elif choice == "5":
            tm.show_stats()

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
