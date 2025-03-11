import tkinter as tk
import random


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winLabel = tk.Label()
        self.catchButton = tk.Button(text="Catch me", command=self.on_click)

        self.winLabel.place(x=200, y=30)
        self.catchButton.pack()

        self.catchButton.bind("<Enter>", self.on_enter)
        self.catchButton.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        self.catchButton.pack(side="right", padx=x, pady=y)

    def on_leave(self, event):
        self.winLabel.config(text="")

    def on_click(self):
        self.winLabel.config(text="You win!")



app = Application()
app.master.title("Catch the Button")
app.master.minsize(width=500, height=500)

app.mainloop()
