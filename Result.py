import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os


class Result:
    '''A part of GUI. Creates the form and puts results in.'''
    @staticmethod
    def  output_result(result, flname):
        root = tk.Tk()
        root.config(bg='#cdcdcd')
        root.title("Результати обчислення")
        frame = tk.Frame(root, width=640, height=480, background='white')
        img = Image.open(flname)
        r_img = ImageTk.PhotoImage(img, master=root)
        label1 = tk.Label(frame, image=r_img)
        label1.pack()
        frame.pack()
        label2 = tk.Label(root, text=f"Result: S = {round(result, 3)}", bg='#cdcdcd', fg='blue', font="Arial 15")
        label2.pack(padx=10, pady=10)

        def end():
            '''Just a command for an End button. Deletes an image, closes the window and quites the code'''
            root.destroy()
            img.close()
            os.remove(flname)
            quit()

        button_end = tk.Button(root, text="Завершити", command=end, width=10, heigh=2, font="Arial 10 bold italic", bg='#94E851', fg='white')
        button_end.pack(padx=10, pady=10)

        root.mainloop()

    @staticmethod
    def get_error(name, text):
        '''Is used in case of error. Shows message end finishes the program.'''
        messagebox.showinfo(name, text)
        quit()
