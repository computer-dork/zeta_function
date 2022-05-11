import mpmath
import numpy as np

from manim import *

class RiemanZetaZeroes(Scene):
    def construct(self):

        plane = ComplexPlane(
                    x_range=[-10, 10, 1],
                    y_range=[-10, 10, 1],
                    background_line_style={
                        "stroke_color": TEAL,
                        "stroke_width": 4,
                        "stroke_opacity": 0.6
                        }
                    )
        self.add(plane.add_coordinates())

        line_0 = Line(start=(0,8,0),end=(0,-8,0),color=BLUE_D)
        line_1 = Line(start=(1,8,0),end=(1,-8,0),color=BLUE_D)
        critical_strip = DashedLine(start=(.5,8,0),end=(.5,-8,0),color=MAROON_C,stroke_width=1)
        self.add(line_0)
        self.add(line_1)
        self.add(critical_strip)
