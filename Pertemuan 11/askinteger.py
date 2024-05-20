from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

top = Tk()

top.geometry("100x100")

def show():
    num = simpledialog.askinteger("Input", "Input An Integer")
    messagebox.showinfo("Result", f"You entered: {num}")

B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()