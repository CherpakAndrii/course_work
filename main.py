from Integrate import Integrate
from GetFromUser import GetFromUser
from draw_plot import Draw
from Result import Result


class Main:
    '''My program should be fully object oriented, so I decide to create this class.

    The main class, similar to "Program" in C#'''

    def __init__(self):
        inp = GetFromUser()
        i = Integrate(inp.a, inp.b, inp.e, inp.func, inp.method)
        i.integrate()
        dr = Draw(i)
        flname = 'plot.png' # Filename for temporary plot image
        dr.get_image(flname)
        Result(i.result, flname)


Main()
