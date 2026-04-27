from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        task = {
            "title": title,
            "done": False
        }
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("Task added ✔")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. [{status}] {task['title']}")

    def complete_task(self, index):
        try:
            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            print("Task completed 🎉")
        except IndexError:
            print("Invalid task ID")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            save_tasks(self.tasks)
            print(f"Deleted: {removed['title']}")
        except IndexError:
            print("Invalid task ID")

    def show_stats(self):
        total = len(self.tasks)
        done = len([t for t in self.tasks if t["done"]])
        pending = total - done

        print("\n===== STATS =====")
        print(f"Total Tasks: {total}")
        print(f"Completed : {done}")
        print(f"Pending   : {pending}")
        if total:
            print(f"Success Rate: {round(done/total*100, 2)}%")
