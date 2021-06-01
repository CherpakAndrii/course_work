from GetFromUser import GetFromUser
from draw_plot import Draw
from Result import Result
import sys


class Main:
    '''My program should be fully object oriented, so I decide to create this class.

    The main class, similar to "Program" in C#'''

    def __init__(self):
        inp = GetFromUser()
        if len(sys.argv)>5: inp.get_from_console(sys.argv)
        else: inp.get_from_user()
        dr = Draw(inp)
        flname = 'plot.png' # Filename for temporary plot image
        dr.get_image(flname)
        Result.output_result(dr.integr.result, flname)


Main()
