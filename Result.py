import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class Result:
    def __init__(self, result, flname):
        root = tk.Tk()
        root.config(bg='#cdcdcd')
        root.title("Результати обчислення")
        root.geometry('450x550')
        frame = tk.Frame(root, width=450, height=550, background='white')
        frame.pack()
        label1 = tk.Label(frame, image=ImageTk.PhotoImage(Image.open(flname)))
        label1.place(anchor="center", relx = 0.5, rely = 0.5)
        root.mainloop()