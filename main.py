from Integrate import Integrate
from GetFromUser import GetFromUser
from draw_plot import Draw
from Result import Result

class main:
    def __init__(self):
        inp = GetFromUser()
        i = Integrate(inp.a, inp.b, inp.e, inp.func, inp.method)
        result = i.integrate()
        dr = Draw(i)
        flname = 'plot.png'
        dr.get_image(flname)
        print(result)
        # Result(result, flname)

main()