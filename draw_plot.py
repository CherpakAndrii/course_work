import matplotlib.pyplot as plt


class Draw:
    '''Is based on the Integrate class. Designed to draw a plot and save it as an image.'''
    def __init__(self, integr):
        self.a, self.b, self.x, self.y, self.e, self.func, self.result = integr.a, integr.b, integr.x, integr.y, integr.e, integr.func, integr.result
        self.f = integr.f
        self.real_x, self.real_y = [], []
        x = self.a-(self.b-self.a)*0.1
        while x <= self.b+(self.b-self.a)*0.1:
            self.real_x.append(x)
            self.real_y.append(self.f(x))
            x += 0.001

    def get_image(self, flname):
        '''Creates a plot image and saves it as a file'''
        j = 1
        while j >= 0:
            plt.plot(self.x, [a*j for a in self.y], label="line 1", color='blue', linewidth=3-j)
            j -= 0.01
        plt.plot(self.real_x, self.real_y, label="real", color='red')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.plot([self.a, self.a], [min(min(self.real_y), 0)-1, max(max(self.real_y), 0)+1], label="range_1", color='green', linestyle='dashed')
        plt.plot([self.b, self.b], [min(min(self.real_y), 0)-1, max(max(self.real_y), 0)+1], label="range_2", color='green', linestyle='dashed')
        self.y.append(0)
        plt.axis([self.a-(self.b-self.a)*0.1, self.b+(self.b-self.a)*0.1, min(self.y)-0.5, max(self.y)+0.5])
        plt.axvline(0)
        plt.axhline(0)
        plt.title(f'f(x) = {self.func}')
        plt.savefig(flname)
