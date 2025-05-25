import tkinter as tk
import tkinter.messagebox as messagebox


class ButtonsForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.row = 0
        self.column = 0
        self.buttons = list()
        self.geometry("300x300")

    def create_buttons(self):
        for i in range(25):
            btn = tk.Button(self, width=5, height=2, text=str(i + 1))
            btn.config(command=lambda i=i: self.show_text(i))
            if i % 5 == 0:
                self.row += 1
                self.column = 0
            else:
                self.column += 1

            btn.grid(row=self.row, column=self.column)
            self.buttons.append(btn)

    def show_text(self, i):
        messagebox.showinfo("Showing", self.buttons[i]["text"])


buttons_form = ButtonsForm()
buttons_form.create_buttons()
buttons_form.mainloop()
