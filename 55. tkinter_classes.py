import tkinter as tk
import tkinter.messagebox as messagebox


class CustomForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        button = tk.Button(
            self, text="Click Me", command=lambda: self.show_text(button)
        )
        # button.config(command=lambda: self.show_text(button))
        button.pack()
        self.mainloop()

    def show_text(self, btn):
        messagebox.showinfo("Showing", btn["text"])


my_form = CustomForm()
