from math import sin, cos, tan, sqrt, log2, log10, log, pi


class Integrate:
    def __init__(self, a, b, e, func, method):
        self.a = a
        self.b = b
        self.e = e
        self.func = func
        self.method = method
        self.x, self.y = [], []

    def f(self, x):
        try:
            return eval(self.func)
        except:
            print("Incorrect input!", self.func, sep="\n")
            quit()

    def rect_l(self):
        x, s = self.a, 0
        while x < self.b:
            s += self.f(x) * self.e
            self.x.append(x)
            self.y.append(self.f(x))
            self.y.append(self.f(x))
            x += self.e
            self.x.append(x)
        self.result = s
        return s

    def rect_r(self):
        x, s = self.a, 0
        while x < self.b:
            self.x.append(x)
            x += self.e
            s += self.f(x) * self.e
            self.x.append(x)
            self.y.append(self.f(x))
            self.y.append(self.f(x))
        self.result = s
        return s

    def rect_c(self):
        x, s = self.a, 0
        while x < self.b:
            s += self.f(x + self.e / 2) * self.e
            self.x.append(x)
            self.y.append(self.f(x + self.e / 2))
            self.y.append(self.f(x + self.e / 2))
            x += self.e
            self.x.append(x)
        self.result = s
        return s

    def trapeze(self):
        x, s = self.a, 0
        self.x.append(x)
        self.y.append(self.f(x))
        while x < self.b:
            s += (self.f(x) * self.e + self.f(x + self.e) * self.e) / 2
            x += self.e
            self.x.append(x)
            self.y.append(self.f(x))
        self.result = s
        return s

    def simps(self):
        x, s = self.a, 0
        while x < self.b:
            self.get_parab(x)
            s += self.e / 6 * (self.f(x) + self.f(x + self.e) + 4 * self.f(x + self.e / 2))
            x += self.e
        self.result = s
        return s

    # Lagrange polynomial
    def parab(self, a, x):
        x1 = a
        x2 = a+self.e/2
        x3 = a+self.e
        y1 = self.f(x1)
        y2 = self.f(x2)
        y3 = self.f(x3)

        # return self.f(a)*(x-a+self.e/2)*(x-a-self.e)/((a-a+self.e/2)*(-self.e))+self.f(a+self.e/2)*(x-a)*(x-a-self.e)/(
        #                         (a+self.e/2-a)*(-self.e/2)+self.f(a+self.e)*(x-a+self.e/2)*(x-a)/((self.e/2)*(self.e)))
        return y1*(x-x2)/(x1-x2)*(x-x3)/(x1-x3)+y2*(x-x1)/(x2-x1)*(x-x3)/(x2-x3)+y3*(x-x1)/(x3-x1)*(x-x2)/(x3-x2)
    # Get parabolic coordinates in range(a, a+e)
    def get_parab(self, a):
        x = a
        while x <= a+self.e:
            self.x.append(x)
            self.y.append(self.parab(a, x))
            x += 0.001

    def integrate(self):
        if self.method == "rect_l":
            return round(self.rect_l(), 5)
        elif self.method == "rect_r":
            return round(self.rect_r(), 5)
        elif self.method == "rect_c":
            return round(self.rect_c(), 5)
        elif self.method == "trapeze":
            return round(self.trapeze(), 5)
        elif self.method == "simps":
            return round(self.simps(), 5)
        else:
            print("An error occurred!")
            quit()

def ctg(x): return cos(x)/sin(x)