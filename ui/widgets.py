import tkinter as tk
from backend.task_manager import add_task, delete_task, toggle_task, update_task, load_tasks_into_list


def setup_widgets(root):
    colors = {
        "bg": "#121212",
        "card": "#1B1B1B",
        "card_border": "#2A2A2A",
        "text": "#F2E9D8",
        "muted": "#B7AFA2",
        "accent": "#C9A227",
        "accent_dark": "#A8831D",
        "accent_soft": "#2D2415",
        "teal": "#0B0B0B",
        "teal_soft": "#3A3A3A",
    }

    fonts = {
        "title": ("Garamond", 26, "bold"),
        "subtitle": ("Segoe UI", 11),
        "label": ("Segoe UI Semibold", 10),
        "body": ("Segoe UI", 10),
        "button": ("Segoe UI Semibold", 10),
    }

    root.configure(bg=colors["bg"])

    header_canvas = tk.Canvas(root, height=110, bg=colors["bg"], highlightthickness=0)
    header_canvas.pack(fill=tk.X)

    title_id = header_canvas.create_text(
        20,
        38,
        anchor="w",
        text="TODOS",
        fill="#FFFFFF",
        font=fonts["title"],
    )
    subtitle_id = header_canvas.create_text(
        20,
        72,
        anchor="w",
        text="Organize, prioritize, and finish with focus",
        fill=colors["accent"],
        font=fonts["subtitle"],
    )

    def draw_gradient():
        header_canvas.delete("gradient")
        width = header_canvas.winfo_width()
        height = header_canvas.winfo_height()
        if width <= 1 or height <= 1:
            return

        r1, g1, b1 = header_canvas.winfo_rgb(colors["teal"])
        r2, g2, b2 = header_canvas.winfo_rgb(colors["accent"])
        for i in range(height):
            ratio = i / max(height - 1, 1)
            r = int(r1 + (r2 - r1) * ratio) // 256
            g = int(g1 + (g2 - g1) * ratio) // 256
            b = int(b1 + (b2 - b1) * ratio) // 256
            color = f"#{r:02x}{g:02x}{b:02x}"
            header_canvas.create_line(0, i, width, i, fill=color, tags="gradient")

        header_canvas.tag_lower("gradient")
        header_canvas.lift(title_id)
        header_canvas.lift(subtitle_id)

    header_canvas.bind("<Configure>", lambda event: draw_gradient())

    content = tk.Frame(root, bg=colors["bg"])
    content.pack(fill=tk.BOTH, expand=True, padx=18, pady=14)

    top_frame = tk.Frame(content, bg=colors["bg"])
    top_frame.pack(fill=tk.X, pady=(0, 12))

    top_frame.columnconfigure(0, weight=1)

    input_label = tk.Label(
        top_frame,
        text="Add a new task",
        bg=colors["bg"],
        fg=colors["muted"],
        font=fonts["label"],
    )
    input_label.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 6))

    task_entry = tk.Entry(
        top_frame,
        font=fonts["body"],
        bg=colors["card"],
        fg=colors["text"],
        highlightthickness=1,
        highlightbackground=colors["card_border"],
        relief="flat",
    )
    task_entry.grid(row=1, column=0, sticky="ew", padx=(0, 8))

    priority_var = tk.StringVar(value="MEDIUM")
    priority_menu = tk.OptionMenu(top_frame, priority_var, "HIGH", "MEDIUM", "LOW")
    priority_menu.config(
        font=fonts["body"],
        bg=colors["card"],
        fg=colors["text"],
        activebackground=colors["accent_soft"],
        activeforeground=colors["text"],
        highlightthickness=1,
        highlightbackground=colors["card_border"],
        relief="flat",
        padx=8,
        pady=2,
    )
    priority_menu.grid(row=1, column=1, padx=(0, 8))

    priority_menu["menu"].config(
        bg=colors["card"],
        fg=colors["text"],
        activebackground=colors["accent_soft"],
        activeforeground=colors["text"],
    )

    list_label = tk.Label(
        content,
        text="Tasks",
        bg=colors["bg"],
        fg=colors["muted"],
        font=fonts["label"],
    )
    list_label.pack(anchor="w")

    list_frame = tk.Frame(
        content,
        bg=colors["card"],
        highlightthickness=1,
        highlightbackground=colors["card_border"],
    )
    list_frame.pack(fill=tk.BOTH, expand=True, pady=(6, 12))

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    task_list = tk.Listbox(
        list_frame,
        height=14,
        yscrollcommand=scrollbar.set,
        bg=colors["card"],
        fg=colors["text"],
        selectbackground=colors["accent"],
        selectforeground="#FFFFFF",
        font=fonts["body"],
        activestyle="none",
        relief="flat",
        highlightthickness=0,
    )
    task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8, pady=8)

    scrollbar.config(command=task_list.yview)

    stats_label = tk.Label(
        content,
        text="No tasks yet",
        bg=colors["bg"],
        fg=colors["muted"],
        font=fonts["subtitle"],
    )
    stats_label.pack(anchor="w", pady=(0, 12))

    bottom_frame = tk.Frame(content, bg=colors["bg"])
    bottom_frame.pack(fill=tk.X)

    button_frame = tk.Frame(bottom_frame, bg=colors["bg"])
    button_frame.pack(side=tk.RIGHT)

    def update_stats():
        total = task_list.size()
        done = sum(1 for item in task_list.get(0, "end") if item.startswith("✔ "))
        if total == 0:
            stats_label.config(text="No tasks yet")
        else:
            stats_label.config(text=f"Done: {done} | Total: {total}")

    def add_task_ui():
        add_task(task_entry, task_list, priority_var)
        update_stats()

    def delete_task_ui():
        delete_task(task_list)
        update_stats()

    def toggle_task_ui():
        toggle_task(task_list)
        update_stats()

    def update_task_ui():
        update_task(task_entry, task_list)
        update_stats()

    def make_button(parent, text, command, style="primary"):
        if style == "primary":
            bg = colors["accent"]
            active_bg = colors["accent_dark"]
            fg = "#FFFFFF"
        else:
            bg = colors["card"]
            active_bg = colors["accent_soft"]
            fg = colors["text"]

        return tk.Button(
            parent,
            text=text,
            command=command,
            font=fonts["button"],
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=fg,
            relief="flat",
            padx=12,
            pady=6,
            highlightthickness=1,
            highlightbackground=colors["card_border"],
        )

    add_btn = make_button(top_frame, "Add Task", add_task_ui, style="primary")
    add_btn.grid(row=1, column=2, sticky="e")

    delete_btn = make_button(button_frame, "Delete", delete_task_ui, style="ghost")
    delete_btn.pack(side=tk.LEFT, padx=(0, 8))

    complete_btn = make_button(button_frame, "Complete", toggle_task_ui, style="primary")
    complete_btn.pack(side=tk.LEFT, padx=(0, 8))

    edit_btn = make_button(
        button_frame,
        "Edit",
        lambda: load_selected_task(task_entry, task_list),
        style="ghost",
    )
    edit_btn.pack(side=tk.LEFT, padx=(0, 8))

    update_btn = make_button(button_frame, "Update", update_task_ui, style="primary")
    update_btn.pack(side=tk.LEFT)

    load_tasks_into_list(task_list)
    update_stats()


def load_selected_task(entry, listbox):
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected[0])
        entry.delete(0, tk.END)
        entry.insert(0, task)