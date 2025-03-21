import tkinter as tk
from multiprocessing.managers import Value


class Appplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label = None
        self.numberEntry = None
        self.convertButton = None
        self.output = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="Converter")
        self.numberEntry = tk.Entry()
        self.convertButton = tk.Button(text="Convert", command=self.convert)
        self.output = tk.Label()
        self.label.pack(side="left")
        self.numberEntry.pack(side="left")
        self.convertButton.pack(side="left")
        self.output.pack(side="left")

    def convert(self):
        entry = self.numberEntry.get()
        try:
            value = float(entry)
            result = round(value * 1.95583, 2)
            self.output.config(text=str(value) + " BGN = " + str(result) + " EUR", bg="green", fg="white")
        #bg = background color
        #fg = text color
        except ValueError:
            self.output.config(text="That's not a number!", bg="red", fg="black")

# create application
app = Appplication()
app.master.title("BGN_to_EUR_converter")
# start the program
app.mainloop()
