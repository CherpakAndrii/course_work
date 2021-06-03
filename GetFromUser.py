import tkinter as tk
from tkinter import messagebox
import re
from math import pi, e
from Result import Result


class GetFromUser:
    '''The class, designed to get the integral function, range and method from user, using GUI'''
    func, a, b, e, method, n = None, 0, 0, 0, None, 0

    def __init__(self): pass

    # main logic of ths class
    def get_from_user(self):
        self.get_func()
        if self.func:
            self.get_range()
            if not self.a == self.b == self.e == 0:
                self.get_method()
                if not self.method: Result.get_error("Завершення", "Здається, роботу програму було передчасно завершено на етапі вибору методу. Прощавайте!")
            else: Result.get_error("Завершення", "Здається, роботу програму було передчасно завершено на етапі визначення меж. Прощавайте!")
        else: Result.get_error("Завершення", "Здається, роботу програму було передчасно завершено на етапі введення функції. Прощавайте!")

    def func_isvalid(self): #checking for invalid function input
        self.func = self.func.replace(',', '.')
        for_check = self.func   # just a copy to replace and ignore some trigonometrical functions
        for f in ['sin(', 'cos(', 'tan(', 'ctg(', 'ln(', 'log(', 'log2(', 'log10(', 'sqrt(']:
            for_check = for_check.replace(f, '(')
        self.func = self.func.replace('ln(', 'log(')
        for_check = for_check.replace('pi', 'x').replace('e', 'x')
        allowed_chars = "0123456789x(.+-*/:^) "
        for ch in for_check:
            if ch not in allowed_chars:
                return False
        count = 0
        for ch in for_check:
            if ch == '(': count += 1
            elif ch == ')': count -= 1
            if count < 0: return False
        if count != 0: return False
        self.func = self.func.replace(' ', '')
        for_check = for_check.replace(' ', '')
        for i in range(len(for_check)-1):
            if for_check[i] == for_check[i+1] == '*': continue
            if for_check[i] in allowed_chars[11:19] and for_check[i+1] in allowed_chars[12:20]:
                return False
        self.func = self.func.replace(':', '/')
        for i in range(len(self.func)-1):
            if self.func[i] not in allowed_chars[11:20] and self.func[i+1] == 'x' or self.func[i] == 'x' and \
                     self.func[i+1] not in allowed_chars[11:21] or self.func[i] == ')' and self.func[i+1] == '(':
                self.func = self.func[:i+1]+"*"+self.func[i+1:]
        self.func = self.func.replace('^', '**')
        return True

    # user's input of the integral function, its validation
    def get_func(self):
        root = tk.Tk()
        root.config(bg='#cdcdcd')
        root.title("Чисельне обчислення інтегралів")
        root.geometry('450x150')

        label1 = tk.Label(root, fg='blue', bg='#cdcdcd', text="Введіть функцію для інтегрування:", font="Arial 14 bold italic")
        label2 = tk.Label(root, text="f(x) = ", bg='#cdcdcd', font="Arial 12")
        inp_func = tk.StringVar()
        func_entry = tk.Entry(root, width=40, textvariable=inp_func)

        #just a function for info button
        def get_info():
            messagebox.showinfo("Дані про межі та крок", '''Введіть функцію для інтегрування, використовуючи цифри, змінну х, оператори "+", "-", "*", ":" aбо "/", "^" aбо "**" та функції sin(), cos(), tan(), ctg(), ln(), log(), log2(), log10() чи sqrt(). Інші оператори не приймаються.\nВи також можете використовувати будь-яку кількість пробілів, вони ніяк не вплинуть на результат.\n \nНаприклад: f(x) = x^2 + 4/x + 2x + 1''')

        #closes the current window and going to the next stage
        def next1():
            self.func = inp_func.get()
            if len(self.func) > 0 and self.func_isvalid():
                root.destroy()
            elif len(self.func) == 0:
                messagebox.showinfo("Помилка вводу", "Функція не може бути порожньою!")
            else:
                messagebox.showinfo("Помилка вводу", "Введено некоректну функцію!\nБудь ласка, використовуйте лише змінну х, цілі або дробові числа, записані через роздільник '.', або функції sin(), cos(), tan(), ctg(), ln(), log(), log2(), log10() чи sqrt().")
                func_entry.delete(0, tk.END)

        button_next = tk.Button(root, text="Далі", command=next1, font="Arial 10 bold italic", width=10, heigh = 2, bg='#94E851', fg='white')
        button_info = tk.Button(root, text="?", command=get_info, font="Arial 10 bold italic", width=2, heigh=1, bg='#909090', fg='white')

        label1.place(anchor='center', relx=0.5, rely=0.25)
        label2.place(anchor='center', relx=0.18, rely=0.5)
        func_entry.place(anchor='center', relx=0.5, rely=0.5)
        button_next.place(anchor='center', relx=0.5, rely=0.8)
        button_info.place(anchor='ne', relx=1, rely=0)

        root.mainloop()

    # user's input of the integral function, its validation
    def get_range(self):
        root = tk.Tk()
        root.config(bg='#cdcdcd')
        root.title("Чисельне обчислення інтегралів")
        root.geometry('470x250')

        label1 = tk.Label(root, fg='blue', bg='#cdcdcd', text="Введіть межі та точність інтегрування:", font="Arial 14 bold italic")
        label2 = tk.Label(root, text="Від: ", bg='#cdcdcd', font="Arial 10")
        inp_a = tk.StringVar()
        a_entry = tk.Entry(root, width=40, textvariable=inp_a)
        label3 = tk.Label(root, text="До: ", bg='#cdcdcd', font="Arial 10")
        inp_b = tk.StringVar()
        b_entry = tk.Entry(root, width=40, textvariable=inp_b)
        label4 = tk.Label(root, text="Кількість частин: ", bg='#cdcdcd', font="Arial 10")
        inp_part_num = tk.StringVar(value="1000")
        part_num_entry = tk.Entry(root, width=40, textvariable=inp_part_num)

        #just a function for info button
        def get_info2():
            messagebox.showinfo("Дані про межі та крок", "На даному етапі вам необхідно ввести межі інтегрування (мінімальне та максимальне значення Х на проміжку) та кількість частин, на які буде розбито проміжок. Значення кількості частин повинно знаходитися в межах від 1 до 10000 включно.")

        # closes the current window and going to the next stage
        def next2():
            def is_invalid():
                if len(inp_a.get()) == 0 or len(inp_b.get()) == 0 or len(inp_part_num.get()) == 0: return -1
                if not re.match(r"^-?[0-9]+\.?[0-9]*$", inp_a.get().replace('pi', '1').replace('e', '1')): return 1
                if not re.match(r"^-?[0-9]+\.?[0-9]*$", inp_b.get().replace('pi', '1').replace('e', '1')): return 2
                if not inp_part_num.get().isdigit(): return 3
                if abs(float(inp_a.get())-float(inp_b.get()))<0.0001: return 4
                if int(inp_part_num.get())<1 or int(inp_part_num.get())>10000: return 5
                return 0
            valid = is_invalid()
            if valid == -1:
                messagebox.showinfo("Введені дані", "Заповніть всі поля!")
            elif valid == 1:
                messagebox.showinfo("Введені дані", "Некоректний ввід:\na = "+inp_a.get() +
                                    "\nНе задовольняє вимогу: a - дробове число, записане через роздільник '.'")
                a_entry.delete(0, tk.END)
            elif valid == 2:
                messagebox.showinfo("Введені дані", "Некоректний ввід:\nb = "+inp_b.get() +
                                    "\nНе задовольняє вимогу: b - дробове число, записане через роздільник '.'")
                b_entry.delete(0, tk.END)
            elif valid == 3:
                messagebox.showinfo("Введені дані", "Некоректний ввід:\ne = "+inp_part_num.get() +
                                    "\nКількість кроків має бути цілим додатнім числом!")
                part_num_entry.delete(0, tk.END)
            elif valid == 4:
                messagebox.showinfo("Введені дані", "Некоректний ввід:\na = " + inp_a.get() + ", b = " + inp_b.get() +
                                    "\nНе задовольняє вимогу: розмір проміжку має перевищувати 0.0001!")
                a_entry.delete(0, tk.END)
                b_entry.delete(0, tk.END)
            elif valid == 5:
                messagebox.showinfo("Введені дані", "Некоректний ввід:\nn = " + inp_part_num.get() +
                                    "\nНе задовольняє вимогу: значення кількості частин повинно знаходитися в межах від 1 до 10000 включно.")
                part_num_entry.delete(0, tk.END)
            else:
                try:
                    self.a = float(inp_a.get())
                    self.b = float(inp_b.get())
                    self.n = int(inp_part_num.get())
                except:
                    messagebox.showinfo("Введені дані", "Помилка")
                    quit()
                if self.a > self.b: self.a, self.b = self.b, self.a
                self.e = (self.b - self.a) / self.n
                root.destroy()

        button_next = tk.Button(root, text="Далі", command=next2, font="Arial 10 bold italic", width=10, heigh = 2, bg='#94E851', fg='white')
        button_info = tk.Button(root, text="?", command=get_info2, font="Arial 10 bold italic", width=2, heigh=1, bg='#909090', fg='white')
        label1.place(anchor='center', relx=0.5, rely=0.15)
        label2.place(anchor='center', relx=0.2, rely=0.35)
        a_entry.place(anchor='center', relx=0.5, rely=0.35)
        label3.place(anchor='center', relx=0.2, rely=0.5)
        b_entry.place(anchor='center', relx=0.5, rely=0.5)
        label4.place(anchor='e', relx=0.25, rely=0.65)
        part_num_entry.place(anchor='center', relx=0.5, rely=0.65)
        button_next.place(anchor='center', relx=0.5, rely=0.85)
        button_info.place(anchor='ne', relx=1, rely=0)

        root.mainloop()

    # user's input of the integral function, its validation
    def get_method(self):
        root = tk.Tk()
        root.config(bg='#cdcdcd')
        root.title("Чисельне обчислення інтегралів")
        root.geometry('350x300')

        label1 = tk.Label(root, fg='blue', bg='#cdcdcd', text="Оберіть метод інтегрування:", font="Arial 14 bold italic")
        method = tk.StringVar(value="trapeze")
        rb1 = tk.Radiobutton(root, text="Метод лівих прямокутників", bg='#cdcdcd',variable=method, value="rect_l")
        rb2 = tk.Radiobutton(root, text="Метод правих прямокутників", bg='#cdcdcd',variable=method, value="rect_r")
        rb3 = tk.Radiobutton(root, text="Метод центральних прямокутників", bg='#cdcdcd',variable=method, value="rect_c")
        rb4 = tk.Radiobutton(root, text="Метод трапецій", variable=method, bg='#cdcdcd',value="trapeze")
        rb5 = tk.Radiobutton(root, text="Метод Сімпсона", variable=method, bg='#cdcdcd',value="simps")

        #just a function for info button
        def get_info3():
            messagebox.showinfo("Дані про методи", "Всі ці методи передбачають розбиття проміжку на смужечки мінімально можливої товщини. Значення інтегралу обчислюється, як сума площ цих смужечок.\n - Метод лівих прямокутників використовує при розрахунках значення функції на початку проміжку, центральних прямокутників - в його центрі, а правих - на кінці;\n - Метод трапецій використовує середнє між значенням на початку та на кінці;\n - Метод Сімпсона сприймає криву як частинку параболи і шукає площу за відповідними формулами.")

        # closes the current window and going to the next stage
        def end():
            self.method = method.get()
            root.destroy()

        button_info = tk.Button(root, text="?", command=get_info3, width=2, heigh = 1, font="Arial 10 bold italic", bg='#909090', fg='white')
        button_end = tk.Button(root, text="Обчислити", command=end, width=10, heigh = 2, font="Arial 10 bold italic", bg='#94E851', fg='white')

        label1.place(anchor='center', relx=0.5, rely=0.12)
        button_info.place(anchor='ne', relx=1, rely=0)
        rb1.place(anchor='w', relx=0.15, rely=0.27)
        rb2.place(anchor='w', relx=0.15, rely=0.39)
        rb3.place(anchor='w', relx=0.15, rely=0.51)
        rb4.place(anchor='w', relx=0.15, rely=0.63)
        rb5.place(anchor='w', relx=0.15, rely=0.75)
        button_end.place(anchor='center', relx=0.5, rely=0.87)

        root.mainloop()

    def get_from_console(self, args):
        self.func = args[1]
        if not self.func_isvalid():
            print("Введено некоректну функцію!\nБудь ласка, використовуйте лише змінну х, цілі або дробові числа, записані через роздільник '.' або функції sin(), cos(), tan(), ctg(), ln(), log(), log2(), log10() чи sqrt().")
            self.get_from_user()
            return
        if not re.match(r"^-?[0-9]+\.?[0-9]*$", args[2].replace('pi', '1').replace('e', '1')):
            print("Введені дані", "Некоректний ввід:\na = "+args[2] +
                                    "\nНе задовольняє вимогу: a - дробове число, записане через роздільник '.'")
            self.get_from_user()
            return
        if not re.match(r"^-?[0-9]+\.?[0-9]*$", args[3].replace('pi', '1').replace('e', '1')):
            print("Введені дані", "Некоректний ввід:\nb = "+args[3] +
                                    "\nНе задовольняє вимогу: b - дробове число, записане через роздільник '.'")
            self.get_from_user()
            return
        if not args[4].isdigit():
            print("Введені дані", "Некоректний ввід:\ne = "+args[4] +
                                    "\nКількість кроків має бути цілим додатнім числом!")
            self.get_from_user()
            return
        if abs(float(args[2]) - float(args[3])) < 0.0001:
            print("Введені дані", "Некоректний ввід:\na = " + args[2] + ", b = " + args[3] +
                                    "\nНе задовольняє вимогу: розмір проміжку має перевищувати 0.0001!")
            self.get_from_user()
            return
        if int(args[4]) < 1 or int(args[4]) > 10000:
            print("Введені дані", "Некоректний ввід:\nn = " + args[4] +
                                    "\nНе задовольняє вимогу: значення кількості частин повинно знаходитися в межах від 1 до 10000 включно.")
            self.get_from_user()
            return

        if args[5] not in ["rect_l", "rect_r", "rect_c", "trapeze", "simps"]:
            print("Введені дані", "Некоректний ввід:\nmethod = " + args[5] +
                  "\nНе задовольняє вимогу: оберіть метод серед rect_l, rect_r, rect_c, trapeze, simps")
            self.get_from_user()
            return

        try:
            self.a = float(args[2])
            self.b = float(args[3])
            self.method = args[5]
        except:
            messagebox.showinfo("Введені дані", "Помилка")
            quit()
        if self.a > self.b: self.a, self.b = self.b, self.a
        self.n = int(args[4])
        self.e = (self.b - self.a) / self.n
