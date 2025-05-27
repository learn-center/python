import tkinter as tk
import tkinter.messagebox as messagebox


def on_item_select(event):
    messagebox.showinfo("Selection", listbox.get(listbox.curselection()[0]))


def on_multiple_select(event):
    selected = listbox.curselection()
    if selected:
        items_text = [listbox.get(i) for i in selected]
        messagebox.showinfo("Selected Items", f"You selected: {', '.join(items_text)}")


root = tk.Tk()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=10, width=30)
listbox.config(selectmode=tk.MULTIPLE)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)

items = [f"Item {i}" for i in range(1, 21)]
for item in items:
    listbox.insert(tk.END, item)

# listbox.bind("<<ListboxSelect>>", on_item_select)
listbox.bind("<<ListboxSelect>>", on_multiple_select)

root.mainloop()
