import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PlotApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Plot 3D with Tkinter")

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.plot_sphere()

        self.color_label = ttk.Label(self.root, text="Pilih Warna:")
        self.color_label.pack()
        self.color_var = tk.StringVar()
        self.color_var.set("blue")
        self.color_combobox = ttk.Combobox(self.root, textvariable=self.color_var, values=["blue", "red", "green"])
        self.color_combobox.pack()
        self.color_combobox.bind("<<ComboboxSelected>>", self.change_color)

    def plot_sphere(self):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = 10 * np.outer(np.cos(u), np.sin(v))
        y = 10 * np.outer(np.sin(u), np.sin(v))
        z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

        self.surf = self.ax.plot_surface(x, y, z, alpha=0.6, color='blue')
        self.ax.set_aspect('equal')

    def change_color(self, event):
        color = self.color_var.get()
        self.surf.set_facecolor(color)
        self.canvas.draw()

if _name_ == "_main_":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()