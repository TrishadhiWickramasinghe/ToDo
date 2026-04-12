def save_tasks(listbox):
    with open("data/tasks.txt", "w") as file:
        tasks = listbox.get(0, "end")
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    tasks = []
    try:
        with open("data/tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks