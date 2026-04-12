def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected)

        add_button.config(command=add_task)
delete_button.config(command=delete_task)