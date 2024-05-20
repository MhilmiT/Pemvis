from tkinter import *
import tkinter.messagebox

print('===============Exercise#1=========================')
print('===Mencetak data dari Entry Widget dengan Button===')
print('==================================================')
root = Tk()
root.geometry('400x200')


def CetakData():
    teks = entry1.get()
    print(teks)
    return None


entry1 = Entry(root, width=20)
entry1.pack()
Button(root, text="Cetak Data", command=CetakData).pack()

root.mainloop()

print('===============Exercise#1=========================')
print('===Mencetak data dari Entry Widget dengan Button===')
print('==================================================')

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')

        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        frame4 = Frame(frame1)
        frame4.grid(row=2, column=1)

        self.FirstNum = StringVar()
        self.SecondNum = StringVar()

        self.lblFirstNum = Label(frame2, text='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=self.FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=self.SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.btnAdd = Button(frame3, text='Add', command=self.addNumbers)
        self.btnAdd.grid(row=0, column=0)

        self.lblResult = Label(frame4, text='Result')
        self.lblResult.grid(row=0, column=0)
        self.txtResult = Entry(frame4, state='readonly')
        self.txtResult.grid(row=0, column=1)

    def addNumbers(self):
        try:
            first_num = float(self.FirstNum.get())
            second_num = float(self.SecondNum.get())
            result = first_num + second_num
            self.txtResult.config(state='normal')
            self.txtResult.delete(0, END)
            self.txtResult.insert(0, str(result))
            self.txtResult.config(state='readonly')
        except ValueError:
            tkinter.messagebox.showerror('Invalid Input', 'Please enter valid numbers')


if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()