import matplotlib.pyplot as plt
from Integrate import Integrate


class Draw:
    '''Is based on the Integrate class. Designed to draw a plot and save it as an image.'''
    def __init__(self, inp):
        self.integr = Integrate(inp)
        self.integr.integrate()
        self.real_x, self.real_y = [], []
        x = self.integr.inputedValues.a-(self.integr.inputedValues.b-self.integr.inputedValues.a)*0.1
        while x <= self.integr.inputedValues.b+(self.integr.inputedValues.b-self.integr.inputedValues.a)*0.1:
            self.real_x.append(x)
            self.real_y.append(self.integr.f(x))
            x += 0.001

    def get_image(self, flname):
        '''Creates a plot image and saves it as a file'''
        j = 1
        while j >= 0:
            plt.plot(self.integr.x_values, [a*j for a in self.integr.y_values], label="line 1", color='blue', linewidth=3-j)
            j -= 0.01
        plt.plot(self.real_x, self.real_y, label="real", color='red')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.plot([self.integr.inputedValues.a, self.integr.inputedValues.a], [min(min(self.real_y), 0)-1, max(max(self.real_y), 0)+1], label="range_1", color='green', linestyle='dashed')
        plt.plot([self.integr.inputedValues.b, self.integr.inputedValues.b], [min(min(self.real_y), 0)-1, max(max(self.real_y), 0)+1], label="range_2", color='green', linestyle='dashed')
        self.integr.y_values.append(0)
        plt.axis([self.integr.inputedValues.a-(self.integr.inputedValues.b-self.integr.inputedValues.a)*0.1, self.integr.inputedValues.b+(self.integr.inputedValues.b-self.integr.inputedValues.a)*0.1, min(self.integr.y_values)-0.5, max(self.integr.y_values)+0.5])
        plt.axvline(0)
        plt.axhline(0)
        plt.title(f'f(x) = {self.integr.inputedValues.func}')
        plt.savefig(flname)
