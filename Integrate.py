from math import sin, cos, tan, sqrt, log2, log10, log, pi
from Result import Result


class Integrate:
    '''The main logic of the program; a class designed to calculate integrals'''
    def __init__(self, inp):
        self.inputedValues = inp
        self.x_values, self.y_values, self.result = [], [], None  # Coordinates for a plot and result

    def f(self, x):
        '''A function to integrate'''
        try:
            return eval(self.inputedValues.func)
        except:
            Result.get_error("Помилка обчислень", "Схоже, щось пішло не так...\nМожливо, було введено некоректну функцію або межі. Спробуйте інакше.")

    def rect_l(self):
        '''The left rectangles method'''
        x, s = self.inputedValues.a, 0
        while x < self.inputedValues.b:
            s += self.f(x) * self.inputedValues.e
            self.x_values.append(x)
            self.y_values.append(self.f(x))
            self.y_values.append(self.f(x))
            x += self.inputedValues.e
            self.x_values.append(x)
        self.result = s

    def rect_r(self):
        '''The right rectangles method'''
        x, s = self.inputedValues.a, 0
        while x < self.inputedValues.b:
            self.x_values.append(x)
            x += self.inputedValues.e
            s += self.f(x) * self.inputedValues.e
            self.x_values.append(x)
            self.y_values.append(self.f(x))
            self.y_values.append(self.f(x))
        self.result = s

    def rect_c(self):
        '''The central rectangles method'''
        x, s = self.inputedValues.a, 0
        while x < self.inputedValues.b:
            s += self.f(x + self.inputedValues.e / 2) * self.inputedValues.e
            self.x_values.append(x)
            self.y_values.append(self.f(x + self.inputedValues.e / 2))
            self.y_values.append(self.f(x + self.inputedValues.e / 2))
            x += self.inputedValues.e
            self.x_values.append(x)
        self.result = s

    def trapeze(self):
        '''A trapeze method, obviously...'''
        x, s = self.inputedValues.a, 0
        self.x_values.append(x)
        self.y_values.append(self.f(x))
        while x < self.inputedValues.b:
            s += (self.f(x) * self.inputedValues.e + self.f(x + self.inputedValues.e) * self.inputedValues.e) / 2
            x += self.inputedValues.e
            self.x_values.append(x)
            self.y_values.append(self.f(x))
        self.result = s

    def simps(self):
        '''The Simpson`s method'''
        x, s = self.inputedValues.a, 0
        while x < self.inputedValues.b:
            self.get_parabola(x)
            s += self.inputedValues.e / 6 * (self.f(x) + self.f(x + self.inputedValues.e) + 4 * self.f(x + self.inputedValues.e / 2))
            x += self.inputedValues.e
        self.result = s

    def parabola(self, a, x):
        '''Lagrange polynomial'''
        x1 = a
        x2 = a+self.inputedValues.e/2
        x3 = a+self.inputedValues.e
        y1 = self.f(x1)
        y2 = self.f(x2)
        y3 = self.f(x3)
        return y1*(x-x2)/(x1-x2)*(x-x3)/(x1-x3)+y2*(x-x1)/(x2-x1)*(x-x3)/(x2-x3)+y3*(x-x1)/(x3-x1)*(x-x2)/(x3-x2)

    def get_parabola(self, a):
        '''Get parabolic coordinates in range(a, a+e) using Lagrange polynomial'''
        x = a
        while x <= a+self.inputedValues.e:
            self.x_values.append(x)
            self.y_values.append(self.parabola(a, x))
            x += 0.001

    def integrate(self):
        '''The main function of the Integrate class. It chooses an integration method and uses it.'''
        if self.inputedValues.method == "rect_l": self.rect_l()
        elif self.inputedValues.method == "rect_r": self.rect_r()
        elif self.inputedValues.method == "rect_c": self.rect_c()
        elif self.inputedValues.method == "trapeze": self.trapeze()
        elif self.inputedValues.method == "simps": self.simps()
        else: Result.get_error("Помилка", "Сталася помилка!")


def ctg(x): return cos(x)/sin(x)    # Really?? Is there no method for cotangent in "math"?..
