print('====================Exercise #2===================')
print('===Mengambil Data dan Menampilkan Data (Part2)=====')
print('===================================================')

from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')

        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=1, column=0)

        frame4 = Frame(frame1)
        frame4.grid(row=2, column=0)

        self.FirstNum = StringVar()
        self.SecondNum = StringVar()
        self.Hasil = StringVar()

        self.lblFirstNum = Label(frame2, text='Masukkan bilangan pertama')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=self.FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Masukkan bilangan kedua')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=self.SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2, textvariable=self.Hasil)
        self.txtHasil.grid(row=2, column=1)

        self.btnJumlahkan = Button(frame3, text='Jumlahkan', command=self.JUMLAHKAN)
        self.btnJumlahkan.grid(row=0, column=0)

        self.btnReset = Button(frame3, text='Reset', command=self.RESET)
        self.btnReset.grid(row=0, column=1)

        self.btnKeluar = Button(frame3, text='Keluar', command=self.KELUAR)
        self.btnKeluar.grid(row=0, column=2)

    def JUMLAHKAN(self):
        try:
            pertama = float(self.FirstNum.get())
            kedua = float(self.SecondNum.get())
            hasil = pertama + kedua
            self.Hasil.set(hasil)
        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter valid numbers")

    def RESET(self):
        self.FirstNum.set("")
        self.SecondNum.set("")
        self.Hasil.set("")

    def KELUAR(self):
        self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()