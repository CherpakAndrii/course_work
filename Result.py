import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os


class Result:   # Creates the form and puts results in
    def __init__(self, result, flname):
        root = tk.Tk()
        root.config(bg='#cdcdcd')
        root.title("Результати обчислення")
        frame = tk.Frame(root, width=640, height=480, background='white')
        label1 = tk.Label(frame, image=ImageTk.PhotoImage(Image.open(flname)))
        label1.pack()
        frame.pack()
        label2 = tk.Label(root, text=f"Result: S = {result}", bg='#cdcdcd', fg='blue', font="Arial 15")
        label2.pack(padx=10, pady=10)

        def end():
            os.remove(flname)
            root.destroy()
            quit()

        button_end = tk.Button(root, text="Завершити", command=end, width=10, heigh=2, font="Arial 10 bold italic", bg='#94E851', fg='white')
        button_end.pack(padx=10, pady=10)

        root.mainloop()


class Error:    # Is used in case of error. Shows message end finishes the program.
    def __init__(self, name, text):
        messagebox.showinfo(name, text)
        quit()
