import tkinter as tk

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# Input field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Listbox (shows tasks)
task_list = tk.Listbox(root, width=40, height=15)
task_list.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task")
delete_button.pack(pady=5)

root.mainloop()