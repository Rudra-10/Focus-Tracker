import json

def read_tasks():
    try:
        return json.load(open("data/tasks.json"))
    except:
        return []
