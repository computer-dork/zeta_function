import mpmath
import numpy as np

from manim import *

class RiemanZetaZeroes(Scene):
    def construct(self):

        # build latex
        text_1 = '\\zeta(\\frac{1}{2} + it)'
        time_text_1 = 'S(t) = 1, L(t) = 100, R(t) = .1'
        values_1 = MathTex(text_1,color=BLUE_D)
        times_1 = MathTex(time_text_1,color=BLUE_D)

        text_2 = '\\zeta(\\frac{1}{2} + \\frac{1}{10}it)'
        time_text_2 = 'S(t) = 1, L(t) = 1000, R(t) = 1'
        values_2 = MathTex(text_2,color=PURPLE_A)
        times_2 = MathTex(time_text_2,color=PURPLE_A)

        text_3 = '\\zeta(\\frac{1}{2} + \\frac{1}{100}it)'
        time_text_3 = 'S(t) = 1, L(t) = 10000, R(t) = 10'
        values_3 = MathTex(text_3,color=YELLOW_D)
        times_3 = MathTex(time_text_3, color=YELLOW_D)

        text_4 = '\\zeta(\\frac{1}{2} + \\frac{1}{1000}it)'
        time_text_4 = 'S(t) = 1, L(t) = 100000, R(t) = 100'
        values_4 = MathTex(text_4,color=ORANGE)
        times_4 = MathTex(time_text_4, color = ORANGE)

        values_group = VGroup(
            values_1,
            times_1,
            values_2,
            times_2,
            values_3,
            times_3,
            values_4,
            times_4
        ).arrange(DOWN, aligned_edge=LEFT)

        self.add(values_group)
        values_group.to_corner(UL).shift(UP*2.4,LEFT*1).scale(.5)

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

        # iterator for each step
        for i in np.arange(1, 100, .1):

            # build coords
            z = mpmath.zeta(complex(.5, i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, (i+.1)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + .1

            # draw this portion of the line
            rz_trace_1 = Line(start=[a,b,c],end=[d,e,f],color=BLUE_D,stroke_width=2)

            self.add(rz_trace_1)
            self.wait(1/framerate)

        for i in np.arange(1, 1000, 1):

            # build coords
            z = mpmath.zeta(complex(.5, (1/10)*i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, 1/10*(i+1)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + 1

            # draw this portion of the line
            rz_trace_2 = Line(start=[a,b,c],end=[d,e,f],color=PURPLE_D,stroke_width=2)

            self.add(rz_trace_2)
            self.wait(1/framerate)

        for i in np.arange(1, 10000, 10):

            # build coords
            z = mpmath.zeta(complex(.5, (1/100)*i))
            a = float(z.real)
            b = float(z.imag)
            c = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, (1/100)*(i+10)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + 10

            # draw this portion of the line
            rz_trace_3 = Line(start=[a,b,c],end=[d,e,f],color=YELLOW_D,stroke_width=2)

            self.add(rz_trace_3)
            self.wait(1/framerate)

        for i in np.arange(1, 100000, 100):

            # build coords
            z = mpmath.zeta(complex(.5, (1/1000)*i))
            a = float(z.real)
            b = float(z.imag)
            c = i
            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, (1/1000)*(i+100)))
            d = float(zz.real)
            e = float(zz.imag)
            f = i + 100
            # draw this portion of the line
            rz_trace_4 = Line(start=[a,b,c],end=[d,e,f],color=ORANGE,stroke_width=2)

            self.add(rz_trace_4)
            self.wait(1/framerate)
