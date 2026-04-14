import tkinter as tk
from backend.task_manager import add_task, delete_task, toggle_task, update_task, load_tasks_into_list

def setup_widgets(root):
    # Top Frame
    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    # Middle Frame
    middle_frame = tk.Frame(root)
    middle_frame.pack()

    # Bottom Frame
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(pady=10)

    # Entry
    task_entry = tk.Entry(top_frame, width=20)
    task_entry.pack(side=tk.LEFT, padx=5)

    # Priority Dropdown
    priority_var = tk.StringVar()
    priority_var.set("MEDIUM")

    priority_menu = tk.OptionMenu(top_frame, priority_var, "HIGH", "MEDIUM", "LOW")
    priority_menu.pack(side=tk.LEFT)

    # Add Button
    add_btn = tk.Button(
        top_frame,
        text="Add",
        command=lambda: add_task(task_entry, task_list, priority_var)
    )
    add_btn.pack(side=tk.LEFT, padx=5)

    # Scrollbar + Listbox
    scrollbar = tk.Scrollbar(middle_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    task_list = tk.Listbox(
        middle_frame,
        width=40,
        height=15,
        yscrollcommand=scrollbar.set
    )
    task_list.pack()

    scrollbar.config(command=task_list.yview)

    # Buttons
    delete_btn = tk.Button(bottom_frame, text="Delete", command=lambda: delete_task(task_list))
    delete_btn.pack(side=tk.LEFT, padx=5)

    complete_btn = tk.Button(bottom_frame, text="Complete", command=lambda: toggle_task(task_list))
    complete_btn.pack(side=tk.LEFT, padx=5)

    edit_btn = tk.Button(bottom_frame, text="Edit", command=lambda: load_selected_task(task_entry, task_list))
    edit_btn.pack(side=tk.LEFT, padx=5)

    update_btn = tk.Button(bottom_frame, text="Update", command=lambda: update_task(task_entry, task_list))
    update_btn.pack(side=tk.LEFT, padx=5)

    # Load existing tasks
    load_tasks_into_list(task_list)


def load_selected_task(entry, listbox):
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected[0])
        entry.delete(0, tk.END)
        entry.insert(0, task)