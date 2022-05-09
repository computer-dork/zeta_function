import mpmath
import numpy as np

from manim import *

class RiemanZetaZeroes(Scene):
    def construct(self):

        # Build groups to hold traces
        trace_group_1 = Group()
        trace_group_2 = Group()
        trace_group_3 = Group()
        trace_group_4 = Group()

        # start iterating
        for i in np.arange(1, 100, .1):

            # build coords
            z = mpmath.zeta(complex(.5, i))
            a1 = float(z.real)
            b1 = float(z.imag)
            c1 = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, (i+.1)))
            d1 = float(zz.real)
            e1 = float(zz.imag)
            f1 = i

            #draw this portion of the line
            rz_trace_1 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_1.add(rz_trace_1)

        for i in np.arange(1, 1000, 1):

            # build coords
            z = mpmath.zeta(complex((1/2), (1/10)*i))
            a1 = float(z.real)
            b1 = float(z.imag)
            c1 = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, 1/10*(i+1)))
            d1 = float(zz.real)
            e1 = float(zz.imag)
            f1 = i

            #draw this portion of the line
            rz_trace_2 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_2.add(rz_trace_2)

        for i in np.arange(1, 10000, 10):

            # build coords
            z = mpmath.zeta(complex((1/2), (1/100)*i))
            a1 = float(z.real)
            b1 = float(z.imag)
            c1 = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, (1/100)*(i+10)))
            d1 = float(zz.real)
            e1 = float(zz.imag)
            f1 = i

            #draw this portion of the line
            rz_trace_3 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_3.add(rz_trace_3)

        for i in np.arange(1, 100000, 100):

            # build coords
            z = mpmath.zeta(complex((1/2), (1/1000) * i))
            a1 = float(z.real)
            b1 = float(z.imag)
            c1 = i

            # build coords 1 point in the future
            zz = mpmath.zeta(complex(.5, (1/1000)*(i+100)))
            d1 = float(zz.real)
            e1 = float(zz.imag)
            f1 = i

            #draw this portion of the line
            rz_trace_4 = Line(start=[a1,b1,c1],end=[d1,e1,f1],color=BLUE_D,stroke_width=2)
            trace_group_4.add(rz_trace_4)



        # add and position each trace
        self.add(trace_group_1)
        trace_group_1.shift(UP * 2, LEFT * 3.5).scale(.4)

        self.add(trace_group_2)
        trace_group_2.shift(UP * 2, RIGHT * 3.5).scale(.4)

        self.add(trace_group_3)
        trace_group_3.shift(DOWN * 2, LEFT * 3.2).scale(.4)

        self.add(trace_group_4)
        trace_group_4.shift(DOWN * 2, RIGHT * 3.7).scale(.4)

        # build latex for each resolution
        trace_1_text_string = '\\zeta(\\frac{1}{2} + it)'
        trace_1_rt_string = 'S(t) = 1, L(t) = 100, R(t) = 0.1'
        trace_1_text = MathTex(trace_1_text_string)
        trace_1_rt = MathTex(trace_1_rt_string)
        self.add(trace_1_text)
        trace_1_text.next_to(trace_group_1, LEFT * 4).scale(.5)
        self.add(trace_1_rt)
        trace_1_rt.next_to(trace_1_text, DOWN, buff=.1).scale(.5)

        trace_2_text_string = '\\zeta(\\frac{1}{2} + \\frac{1}{10}it)'
        trace_2_rt_string = 'S(t) = 1, L(t) = 1000, R(t) = 1'
        trace_2_text = MathTex(trace_2_text_string)
        trace_2_rt = MathTex(trace_2_rt_string)
        self.add(trace_2_text)
        trace_2_text.next_to(trace_group_2, LEFT * 4).scale(.5)
        self.add(trace_2_rt)
        trace_2_rt.next_to(trace_2_text, DOWN, buff=.1).scale(.5)

        trace_3_text_string = '\\zeta(\\frac{1}{2} + \\frac{1}{100}it)'
        trace_3_rt_string = 'S(t) = 1, L(t) = 10000, R(t) = 10'
        trace_3_text = MathTex(trace_3_text_string)
        trace_3_rt = MathTex(trace_3_rt_string)
        self.add(trace_3_text)
        trace_3_text.next_to(trace_group_3, LEFT * 3.5).scale(.5)
        self.add(trace_3_rt)
        trace_3_rt.next_to(trace_3_text, DOWN, buff=.1).scale(.5)

        trace_4_text_string = '\\zeta(\\frac{1}{2} + \\frac{1}{1000}it)'
        trace_4_rt_string = 'S(t) = 1, L(t) = 100000, R(t) = 100'
        trace_4_text = MathTex(trace_4_text_string)
        trace_4_rt = MathTex(trace_4_rt_string)
        self.add(trace_4_text)
        trace_4_text.next_to(trace_group_4, LEFT * 3.5).scale(.5)
        self.add(trace_4_rt)
        trace_4_rt.next_to(trace_4_text, DOWN, buff=.1).scale(.5)

        # start iterating
        # for i in np.arange(1, 44.1, .1):
        #
        #     # build coords
        #     z2 = mpmath.zeta(complex((49/100), (51/100)*i))
        #     a2 = float(z2.real)
        #     b2 = float(z2.imag)
        #     c2 = i
        #
        #     # build coords 1 point in the future
        #     zz2 = mpmath.zeta(complex((49/100), (51/100)*(i+.1)))
        #     d2 = float(zz2.real)
        #     e2 = float(zz2.imag)
        #     f2 = i + .1
        #
        #     #draw this portion of the line
        #     rz_trace_2 = Line(start=[a2,b2,c2],end=[d2,e2,f2],color=YELLOW_C,stroke_width=2)
        #     self.add(rz_trace_2)
        #
        # # start iterating
        # for i in np.arange(1, 45, .1):
        #
        #     # build coords
        #     z3 = mpmath.zeta(complex((1/2), (1)*i))
        #     a3 = float(z3.real)
        #     b3 = float(z3.imag)
        #     c3 = i
        #
        #     # build coords 1 point in the future
        #     zz3 = mpmath.zeta(complex((1/2), (1)*(i+.1)))
        #     d3 = float(zz3.real)
        #     e3 = float(zz3.imag)
        #     f3 = i + .1
        #
        #     #draw this portion of the line
        #     rz_trace_3 = Line(start=[a3,b3,c3],end=[d3,e3,f3],color=TEAL_D,stroke_width=2)
        #     self.add(rz_trace_3)
