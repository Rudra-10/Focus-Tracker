import json

def write_tasks(tasks):
    json.dump(tasks, open("data/tasks.json", "w"), indent=4)
