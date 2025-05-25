import tkinter as tk
import tkinter.messagebox as messagebox


def show_text():
    messagebox.showinfo("Showing", text_box.get(1.0, tk.END))


def child_form():
    second_form = tk.Tk()
    child_button = tk.Button(
        second_form, text="Close", command=lambda: second_form.destroy()
    )
    child_button.pack()


form = tk.Tk()

text_box = tk.Text()
text_box.grid(row=0)
# text_box.pack()

button = tk.Button(text="Click Me!", command=show_text).grid(row=1)
# button.pack()

second_button = tk.Button(text="Child Form", command=child_form).grid(row=1, column=1)
# second_button.pack()

form.mainloop()
