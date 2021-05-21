from Integrate import Integrate
from GetFromUser import GetFromUser
from draw_plot import Draw
from Result import Result


class Main:
    def __init__(self):
        inp = GetFromUser()
        i = Integrate(inp.a, inp.b, inp.e, inp.func, inp.method)
        i.integrate()
        dr = Draw(i)
        flname = 'plot.png' # Filename for temporary plot image
        dr.get_image(flname)
        Result(i.result, flname)


Main()
