import mpmath
import numpy as np

from manim import *

class RiemannZeta(Scene):
    def construct(self):

        # how to iterate
        start = 1
        top = 1000
        rate = 1

        # build latex
        text = '\\zeta(\\frac{1}{100}^{17\\pi} + \\frac{1}{100}^{17\\pi}it)'
        time_text = 'S(t) = 1, L(t) = 1000, R(t) = 1'
        eq_values = MathTex(text)
        time_text = MathTex(time_text)
        text_group = VGroup(eq_values,time_text).arrange(DOWN, buff=.1, aligned_edge=LEFT)
        self.add(text_group)
        text_group.to_corner(UL).scale(.7)

        # set framerate for output
        framerate = 60

        # add a complex plane
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

        # start iterating
        for i in np.arange(start, top, rate):

            # build coords
            z = mpmath.zeta(complex(1*(.01**17*3.14), i * (.01**17*3.14)))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(1*(.01**17*3.14), i * (.01**17*3.14)) + rate)
            d = float(zz.real)
            e = float(zz.imag)
            f = i + rate

            # draw this portion of the line
            rz_trace = Line(start=[a,b,c],end=[d,e,f],color=BLUE_D,stroke_width=1)

            self.add(rz_trace)
            self.wait(1/framerate)
