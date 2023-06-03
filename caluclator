rom tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = Entry(master)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 1, 0
        for button in buttons:
            if button == '=':
                btn = Button(master, text=button, width=8, command=self.calculate)
                btn.grid(row=row, column=col)
            else:
                btn = Button(master, text=button, width=8, command=lambda btn=button: self.insert(btn))
                btn.grid(row=row, column=col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

    def insert(self, value):
        self.entry.insert(END, value)

    def calculate(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.entry.delete(0, END)
            self.entry.insert(END, str(result))
        except:
            self.entry.delete(0, END)
            self.entry.insert(END, "Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()
