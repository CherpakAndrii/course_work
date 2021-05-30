from math import sin, cos, tan, sqrt, log2, log10, log, pi, e
from Result import Error


class Integrate:
    '''The main logic of the program; a class designed to calculate integrals'''
    def __init__(self, a, b, e, func, method):
        self.a = a  # Left border of the range
        self.b = b  # Right border of the range
        self.e = e  # Step
        self.func = func    # Function to integrate in string
        self.method = method    # Integration method
        self.x, self.y, self.result = [], [], None  # Coordinates for a plot and result

    def f(self, x):
        '''A function to integrate'''
        try:
            return eval(self.func)
        except:
            Error("Помилка обчислень", "Схоже, щось пішло не так...\nМожливо, було введено некоректну функцію або межі. Спробуйте інакше.")

    def rect_l(self):
        '''The left rectangles method'''
        x, s = self.a, 0
        while x < self.b:
            s += self.f(x) * self.e
            self.x.append(x)
            self.y.append(self.f(x))
            self.y.append(self.f(x))
            x += self.e
            self.x.append(x)
        self.result = s

    def rect_r(self):
        '''The right rectangles method'''
        x, s = self.a, 0
        while x < self.b:
            self.x.append(x)
            x += self.e
            s += self.f(x) * self.e
            self.x.append(x)
            self.y.append(self.f(x))
            self.y.append(self.f(x))
        self.result = s

    def rect_c(self):
        '''The central rectangles method'''
        x, s = self.a, 0
        while x < self.b:
            s += self.f(x + self.e / 2) * self.e
            self.x.append(x)
            self.y.append(self.f(x + self.e / 2))
            self.y.append(self.f(x + self.e / 2))
            x += self.e
            self.x.append(x)
        self.result = s

    def trapeze(self):
        '''A trapeze method, obviously...'''
        x, s = self.a, 0
        self.x.append(x)
        self.y.append(self.f(x))
        while x < self.b:
            s += (self.f(x) * self.e + self.f(x + self.e) * self.e) / 2
            x += self.e
            self.x.append(x)
            self.y.append(self.f(x))
        self.result = s

    def simps(self):
        '''The Simpson`s method'''
        x, s = self.a, 0
        while x < self.b:
            self.get_parabola(x)
            s += self.e / 6 * (self.f(x) + self.f(x + self.e) + 4 * self.f(x + self.e / 2))
            x += self.e
        self.result = s

    def parabola(self, a, x):
        '''Lagrange polynomial'''
        x1 = a
        x2 = a+self.e/2
        x3 = a+self.e
        y1 = self.f(x1)
        y2 = self.f(x2)
        y3 = self.f(x3)
        return y1*(x-x2)/(x1-x2)*(x-x3)/(x1-x3)+y2*(x-x1)/(x2-x1)*(x-x3)/(x2-x3)+y3*(x-x1)/(x3-x1)*(x-x2)/(x3-x2)

    def get_parabola(self, a):
        '''Get parabolic coordinates in range(a, a+e) using Lagrange polynomial'''
        x = a
        while x <= a+self.e:
            self.x.append(x)
            self.y.append(self.parabola(a, x))
            x += 0.001

    def integrate(self):
        '''The main function of the Integrate class. It chooses an integration method and uses it.'''
        if self.method == "rect_l": self.rect_l()
        elif self.method == "rect_r": self.rect_r()
        elif self.method == "rect_c": self.rect_c()
        elif self.method == "trapeze": self.trapeze()
        elif self.method == "simps": self.simps()
        else: Error("Помилка", "Сталася помилка!")


def ctg(x): return cos(x)/sin(x)    # Really?? Is there no method for cotangent in "math"?..
