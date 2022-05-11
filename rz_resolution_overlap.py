import mpmath
import numpy as np

from manim import *

class RiemanZetaZeroes(Scene):
    def construct(self):

        # build latex
        time_text = 'S(t) = 1, L(t) = 100, R(t) = 1'
        timing = MathTex(time_text)

        text_1 = '\\zeta(\\frac{1}{2} + it)'
        values_1 = MathTex(text_1,color=BLUE_D)

        text_2 = '\\zeta(\\frac{1}{2} + \\frac{3}{4}it)'
        values_2 = MathTex(text_2,color=PURPLE_A)

        text_3 = '\\zeta(\\frac{1}{2} + \\frac{1}{2}it)'
        values_3 = MathTex(text_3,color=YELLOW_D)

        text_4 = '\\zeta(\\frac{1}{2} + \\frac{1}{4}it)'
        values_4 = MathTex(text_4,color=ORANGE)

        values_group = VGroup(
            timing,
            values_1,
            values_2,
            values_3,
            values_4
        ).arrange(DOWN, aligned_edge=LEFT)

        self.add(values_group)
        values_group.to_corner(UL).shift(RIGHT*.35,UP*.8).scale(.5)


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

        rz_group = Group()

        # start iterating each step
        for i in np.arange(start, top, rate):

            # build coords
            z = mpmath.zeta(complex(.5, 1*i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, 1*(i+rate)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + rate

            # draw this portion of the line
            rz_trace_1 = Line(start=[a,b,c],end=[d,e,f],color=BLUE_D,stroke_width=2)

            rz_group.add(rz_trace_1)

        for i in np.arange(start, top, rate):

            # build coords
            z = mpmath.zeta(complex(.5, .75*i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, .75*(i+rate)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + rate

            # draw this portion of the line
            rz_trace_2 = Line(start=[a,b,c],end=[d,e,f],color=PURPLE_D,stroke_width=2)

            rz_group.add(rz_trace_2)

        for i in np.arange(start, top, rate):

            # build coords
            z = mpmath.zeta(complex(.5, .5*i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, .5*(i+rate)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + rate

            # draw this portion of the line
            rz_trace_3 = Line(start=[a,b,c],end=[d,e,f],color=YELLOW_D,stroke_width=2)

            rz_group.add(rz_trace_3)

        for i in np.arange(start, top, rate):

            # build coords
            z = mpmath.zeta(complex(.5, .25*i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, .25*(i+rate)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + rate

            # draw this portion of the line
            rz_trace_4 = Line(start=[a,b,c],end=[d,e,f],color=ORANGE,stroke_width=2)

            rz_group.add(rz_trace_4)

        self.add(rz_group)
