import json

def read_tasks():
    try:
        return json.load(open("tasks.json"))
    except:
        return []
    
def write_tasks(tasks):
    json.dump(tasks, open("tasks.json", "w"), indent=4)

def add_task(task): 
    tasks = read_tasks()
    tasks.append({"task": task, "done": False})
    write_tasks(tasks)
    print("Task added!")

def view_tasks():
    for i,t in enumerate(read_tasks()):
        print(f"{i+1}. {t['task']} - {'Done' if t['done'] else 'Pending'}")

if __name__ == "__main__":
    print("Focus Tracker CLI")
    print("1. Add Task")
    print("2. View Tasks")

    choice = input("Choose an option: ")
    
    if choice == "1":
        add_task(input("Enter task: "))
    else:
        view_tasks()