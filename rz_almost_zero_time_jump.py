import mpmath
import numpy as np

from manim import *

class RiemannZeta(Scene):
    def construct(self):
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

        # set a rate to iterate the zeta function at
        # using 1 because conditions are extremely temperamental here
        rate = 1

        # start iterating the multiplier
        # in this setup we get a weird show when ~.1 < k < 1
        # and infinite zeroes when 0 < k < ~.1
        for k in np.arange(1.25, -1.25,-.001):
            # group to add all the lines in the next loop to
            lg = Group()
            # start iterating the zeta function
            for i in np.arange(1, 500, rate):
                # build coords
                z1 = mpmath.zeta(complex((1)*(k**17*3.14), i * (k**17*3.14)))
                a1 = float(z1.real)
                b1 = float(z1.imag)
                c1 = i

                # build coords 1 point in the future
                zz1 = mpmath.zeta(complex((1)*(k**17*3.14), i * (k**17*3.14))+rate)
                d1 = float(zz1.real)
                e1 = float(zz1.imag)
                f1 = i + rate

                #draw this portion of the line
                rz_trace_1 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_C,stroke_width=.1)
                #rz_trace_2 = Line(start=[-a1,-b1,-c1],end=[-d1,-e1,-f1],color=TEAL_C,stroke_width=1)
                lg.add(rz_trace_1)
                #lg.add(rz_trace_2)

            # add and hold the zeta trace for 1 frame
            self.add(lg)
            self.wait(1/framerate)
            self.remove(lg)
