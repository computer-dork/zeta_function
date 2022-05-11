import mpmath
import numpy as np

from manim import *

class RiemanZetaZeroes(Scene):
    def construct(self):

        # set framerate for output
        framerate = 60


        # Build groups to hold traces
        trace_group_1 = Group()
        trace_group_2 = Group()
        trace_group_3 = Group()
        trace_group_4 = Group()

        # start iterating
        for i in np.arange(1, 100, 1):

            # build coords
            z1 = mpmath.zeta(complex((1/2), i))
            a1 = float(z1.real)
            b1 = float(z1.imag)
            c1 = i

            # build coords 1 point in the future
            zz1 = mpmath.zeta(complex((1/2), (i+rate)))
            d1 = float(zz1.real)
            e1 = float(zz1.imag)
            f1 = i + 1

            #draw this portion of the line
            rz_trace_1 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_1.add(rz_trace_1)

        for i in np.arange(1, 100, 1):

            # build coords
            z1 = mpmath.zeta(complex((1/2), .75*i))
            a1 = float(z1.real)
            b1 = float(z1.imag)
            c1 = i

            # build coords 1 point in the future
            zz1 = mpmath.zeta(complex((1/2), .75*(i+rate)))
            d1 = float(zz1.real)
            e1 = float(zz1.imag)
            f1 = i + 1

            #draw this portion of the line
            rz_trace_2 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_2.add(rz_trace_2)

        for i in np.arange(1, 100, 1):

            # build coords
            z1 = mpmath.zeta(complex((1/2), .5*i))
            a1 = float(z1.real)
            b1 = float(z1.imag)
            c1 = i

            # build coords 1 point in the future
            zz1 = mpmath.zeta(complex((1/2), .5*(i+rate)))
            d1 = float(zz1.real)
            e1 = float(zz1.imag)
            f1 = i + .1

            #draw this portion of the line
            rz_trace_3 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_3.add(rz_trace_3)

        for i in np.arange(1, 100, 1):

            # build coords
            z1 = mpmath.zeta(complex((1/2), .25*i))
            a1 = float(z1.real)
            b1 = float(z1.imag)
            c1 = i

            # build coords 1 point in the future
            zz1 = mpmath.zeta(complex((1/2), .25*(i+rate)))
            d1 = float(zz1.real)
            e1 = float(zz1.imag)
            f1 = i + .1

            #draw this portion of the line
            rz_trace_4 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_4.add(rz_trace_4)



        # add and position each trace
        self.add(trace_group_1)
        trace_group_1.shift(UP * 2, LEFT * 3).scale(.4)

        self.add(trace_group_2)
        trace_group_2.shift(UP * 2, RIGHT * 3).scale(.4)

        self.add(trace_group_3)
        trace_group_3.shift(DOWN * 2, LEFT * 3).scale(.4)

        self.add(trace_group_4)
        trace_group_4.shift(DOWN * 2, RIGHT * 4).scale(.4)

        # build latex for each resolution
        trace_1_text_string = '\\zeta(\\frac{1}{2} + it)'
        trace_1_rt_string = 'S(t) = 1, L(t) = 100, R(t) = 1'
        trace_1_text = MathTex(trace_1_text_string)
        trace_1_rt = MathTex(trace_1_rt_string)
        self.add(trace_1_text)
        trace_1_text.next_to(trace_group_1, LEFT * 4).scale(.5)
        self.add(trace_1_rt)
        trace_1_rt.next_to(trace_1_text, DOWN, buff=.1).scale(.5)

        trace_2_text_string = '\\zeta(\\frac{1}{2} + \\frac{3}{4}it)'
        trace_2_rt_string = 'S(t) = 1, L(t) = 100, R(t) = 1'
        trace_2_text = MathTex(trace_2_text_string)
        trace_2_rt = MathTex(trace_2_rt_string)
        self.add(trace_2_text)
        trace_2_text.next_to(trace_group_2, LEFT * 4).scale(.5)
        self.add(trace_2_rt)
        trace_2_rt.next_to(trace_2_text, DOWN, buff=.1).scale(.5)

        trace_3_text_string = '\\zeta(\\frac{1}{2} + \\frac{1}{2}it)'
        trace_3_rt_string = 'S(t) = 1, L(t) = 100, R(t) = 1'
        trace_3_text = MathTex(trace_3_text_string)
        trace_3_rt = MathTex(trace_3_rt_string)
        self.add(trace_3_text)
        trace_3_text.next_to(trace_group_3, LEFT * 4).scale(.5)
        self.add(trace_3_rt)
        trace_3_rt.next_to(trace_3_text, DOWN, buff=.1).scale(.5)

        trace_4_text_string = '\\zeta(\\frac{1}{2} + \\frac{1}{4}it)'
        trace_4_rt_string = 'S(t) = 1, L(t) = 100, R(t) = 1'
        trace_4_text = MathTex(trace_4_text_string)
        trace_4_rt = MathTex(trace_4_rt_string)
        self.add(trace_4_text)
        trace_4_text.next_to(trace_group_4, LEFT * 4).scale(.5)
        self.add(trace_4_rt)
        trace_4_rt.next_to(trace_4_text, DOWN, buff=.1).scale(.5)
