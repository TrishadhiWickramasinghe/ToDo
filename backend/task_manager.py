from utils.file_handler import save_tasks, load_tasks

def add_task(entry, listbox, priority_var):
    task = entry.get()
    priority = priority_var.get()

    if task:
        if priority == "HIGH":
            task = "🔴 [HIGH] " + task
        elif priority == "MEDIUM":
            task = "🟡 [MEDIUM] " + task
        else:
            task = "🟢 [LOW] " + task

        listbox.insert("end", task)
        entry.delete(0, "end")
        save_tasks(listbox)


def delete_task(listbox):
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks(listbox)


def toggle_task(listbox):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)

        if task.startswith("✔ "):
            task = task.replace("✔ ", "")
        else:
            task = "✔ " + task

        listbox.delete(index)
        listbox.insert(index, task)
        save_tasks(listbox)


def update_task(entry, listbox):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_task = entry.get()

        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
            entry.delete(0, "end")
            save_tasks(listbox)


def load_tasks_into_list(listbox):
    tasks = load_tasks()
    for task in tasks:
        listbox.insert("end", task)