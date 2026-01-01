from tasks.reader import read_tasks
from tasks.writer import write_tasks

def add_task(task):
    tasks = read_tasks()
    tasks.append({"task": task, "done": False})
    write_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks found.")
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} - {status}")

def mark_task_done(index):
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        write_tasks(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        write_tasks(tasks)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    while True:
        print("\nFocus Tracker CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(input("Enter task: "))
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            num = int(input("Enter task number to mark done: ")) - 1
            mark_task_done(num)
        elif choice == "4":
            view_tasks()
            num = int(input("Enter task number to delete: ")) - 1
            delete_task(num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
