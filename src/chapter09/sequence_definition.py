from manim import *
from math import ceil,floor

colorlist = ['#005a94', '#196a9e', '#327aa9', '#4c8bb4', '#669cbe', '#7facc9', '#99bdd4', 
'#b2cdde', '#ccdee9', '#e5eef4','#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff',
'#ffffff', '#ffffff']

BODY_FONT = 'Inter'
PAUSE = 2.0
COLOR_BG = '#2b2b2b' # '#484949'
EMPH = '#E60000'

def is_square(n):
    if n % 2 == 0:
        return True
    else:
        return False


def compute_shape(n):
    width = 4 * 2 ** (-ceil(n / 2))
    height = 4 * 2 ** (-floor(n / 2))
    return width, height


def compute_start_position(n):
    
    left = -6.0
    bottom = -1.5

    w,h = compute_shape(n)
    return  left + w/2, bottom + h/2


class Motivation(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{mlmodern}')
        myTemplate.add_to_preamble(r'\usepackage[sfdefault, scaled=0.85]{inter}')
        myTemplate.add_to_preamble(r"\usepackage{xfrac}")


        self.camera.background_color = COLOR_BG

        x0 = -4.0
        y0 = 0.5

        # source box
        source = Square(side_length=4)
        source.move_to([x0,y0,0])

        # annotation of the start box
        bottom_brace = Brace(source)
        bottom_brace_text = MathTex("1").next_to(bottom_brace, DOWN)
        left_brace = Brace(source, direction=LEFT)
        left_brace_text = MathTex("1").next_to(left_brace, LEFT)

        # animation of the annotated square
        annotated_square = Group(source, bottom_brace, bottom_brace_text, left_brace, left_brace_text)
        self.play(Create(source))
        self.play(FadeIn(bottom_brace))
        self.play(FadeIn(bottom_brace_text))
        self.play(FadeIn(left_brace))
        self.play(FadeIn(left_brace_text))
        self.play(Wait(PAUSE))  

        # start rectangle
        w,h = compute_shape(0)
        start_rectangle = Rectangle(height=h, width=w)
        start_rectangle.set_fill(ManimColor(colorlist[0]), opacity=1.0)
        start_rectangle.move_to([x0,y0,0])
        self.play(FadeIn(start_rectangle))

        text = Text("Fläche", font=BODY_FONT, font_size=36, color=ManimColor('#FFFFFF'))
        text.move_to([x0,y0+0.5,0])
        self.play(AddTextLetterByLetter(text))

        term = MathTex('a_1 = 1')
        term.next_to(text, 2*DOWN)
        self.play(AddTextLetterByLetter(term))
        self.wait(PAUSE)

        # transform to next rectangle
        N = len(colorlist)

        vdots_left = MathTex(r'\rule{30pt}{1pt}', color=COLOR_BG)
        vdots_right = MathTex(r'\vdots')
        vdots = VGroup(vdots_left, vdots_right)

        group = VGroup(MathTex('a_1 = 1'),
        MathTex('a_2 = \sfrac{1}{2}', tex_template=myTemplate),
        MathTex('a_3 = \sfrac{1}{4}', tex_template=myTemplate),
        MathTex('a_4 = \sfrac{1}{8}', tex_template=myTemplate),
        MathTex('a_5 = \sfrac{1}{16}', tex_template=myTemplate),
        vdots,     
        )
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        group.move_to([2,0,0])

        self.play(ReplacementTransform(term, group[0]))
        self.play(FadeOut(text))

        for i in range(1,5):

            # next rectangle
            w,h = compute_shape(i)
            next_rectangle = Rectangle(height=h, width=w)
            next_rectangle.set_fill(ManimColor(colorlist[i]), opacity=1.0)
            x,y = compute_start_position(i)
            next_rectangle.move_to([x,y,0])
            self.play(Transform(start_rectangle, next_rectangle))
            
            # annotation
            term = group[i].copy()
            term.next_to(next_rectangle)
            self.play(AddTextLetterByLetter(term))
            self.wait(PAUSE)
            self.play(ReplacementTransform(term, group[i]))

        for i in range(5,11):

            # next rectangle
            w,h = compute_shape(i)
            next_rectangle = Rectangle(height=h, width=w)
            next_rectangle.set_fill(ManimColor(colorlist[i]), opacity=1.0)
            x,y = compute_start_position(i)
            next_rectangle.move_to([x,y,0])
            self.play(Transform(start_rectangle, next_rectangle))
        
        self.play(Create(group[5]))
        self.wait(PAUSE)

        self.play(FadeOut(annotated_square), FadeOut(start_rectangle))
        group.generate_target()
        group.target.move_to([-5,0,0], aligned_edge=LEFT)
        self.play(MoveToTarget(group))


class InformalDefinition(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{mlmodern}')
        myTemplate.add_to_preamble(r'\usepackage[sfdefault, scaled=0.9]{inter}')
        myTemplate.add_to_preamble(r"\usepackage{xfrac}")

        self.camera.background_color = COLOR_BG

        # group with sequence elements
        vdots_left  = MathTex(r'\rule{30pt}{1pt}', color=COLOR_BG)
        vdots_right = MathTex(r'\vdots')
        vdots = VGroup(vdots_left, vdots_right)

        a1  = MathTex('a_{{1}} = 1')
        a2  = MathTex('a_{{2}} = \sfrac{1}{2}', tex_template=myTemplate)
        a3  = MathTex('a_{{3}} = \sfrac{1}{4}', tex_template=myTemplate)
        a4  = MathTex('a_{{4}} = \sfrac{1}{8}', tex_template=myTemplate)
        a5  = MathTex('a_{{5}} = \sfrac{1}{16}', tex_template=myTemplate)
        group = VGroup(a1, a2, a3, a4, a5, vdots).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        group.move_to([-5,0,0], aligned_edge=LEFT)

        self.add(group)
        self.wait(PAUSE)

        arrow = Arrow(start=group.get_top()+2*RIGHT+UP, end=group.get_bottom()+2*RIGHT+DOWN)
        self.play(Create(arrow))
        self.wait(PAUSE)

        text01 =  Text('Folge =', font='Inter', font_size=32)
        text02 = Text('unendliche Aufzählung von Zahlen', font='Inter', font_size=32)
        text03 = Text('mit durchnummerierten Positionen', font='Inter', font_size=32)
        text04 = Tex(r'$\sfrac{1}{8}$ ist das 4. ',r'Folgenglied', tex_template=myTemplate)
        text05 = Tex(r'Folgenglied $\sfrac{1}{16}$ hat den ', 'Index', ' 5', tex_template=myTemplate)
        text = VGroup(text01, text02, text03, text04, text05).arrange(DOWN, buff=0.35)
        text.move_to([2.5, 0, 0]).align_to(group, UP)

        for t in text[:3]:
            self.play(FadeIn(t))
            self.wait(PAUSE)

        self.play(Circumscribe(a4))
        self.play(FadeIn(text04))
        self.wait(PAUSE)
        self.play(Indicate(a5[1]))
        self.play(FadeIn(text05))
        self.wait(PAUSE)

        # indicate Fachbegriffe
        self.play(Indicate(text01[0:5]))
        self.wait()
        self.play(Indicate(text04[1]))
        self.wait()
        self.play(Indicate(text05[1]))
        self.wait()


class Definition(Scene):
    def construct(self):
        myTemplate = TexTemplate(documentclass='\\documentclass[preview, varwidth=240px]{standalone}')
        myTemplate.add_to_preamble(r'\usepackage{microtype, mlmodern}')
        myTemplate.add_to_preamble(r'\usepackage[sfdefault, scaled=0.85]{inter}')
        myTemplate.add_to_preamble(r'\usepackage[bb=ncmbbk, bfbb]{mathalpha}')       
        myTemplate.add_to_preamble(r"\usepackage{xfrac}")
        #myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        #myTemplate.add_to_preamble(r'\usepackage[onehalfspacing]{setspace} ')

        self.camera.background_color = COLOR_BG

        MY_BLUE = '#CCDEE9'
        
        heading_text = Text('Was ist eine Folge?', font='Inter', color=MY_BLUE)
        underline = Line(LEFT, RIGHT, color=MY_BLUE).scale_to_fit_width(0.9*config.frame_width)
        heading = VGroup(heading_text, underline).arrange(DOWN)
        text01 = Tex(r'Eine Folge ist eine Aufzählung von unendlich vielen Zahlen $a_i$ und wird mit runden Klammern geschrieben: \[(a_i)_{i\in\mathbb{N}}.\]', tex_template=myTemplate)
        text01[0][4:9].set_color('#FFEC7F')
        text02 = Tex(r'Eine einzelne Zahl der Folge wird Folgenglied genannt.', tex_template=myTemplate)
        text02[0][28:39].set_color('#FFEC7F')
        text03 = Tex(r'Die Position eines Folgenglieds innerhalb der Folge wird Index genannt.', tex_template=myTemplate)
        text03[0][49:54].set_color('#FFEC7F')
        text = VGroup(text01, text02, text03).arrange(DOWN, buff=0.5, center=False, aligned_edge=LEFT)
        together = VGroup(heading, text).arrange(DOWN, buff=0.5)

        #.scale_to_fit_width(0.9*config.frame_width)

        self.play(FadeIn(heading))
        self.wait(PAUSE)
        self.play(FadeIn(text01))
        self.wait(PAUSE)
        self.play(FadeIn(text02))
        self.wait(PAUSE)
        self.play(FadeIn(text03))
        self.wait(PAUSE)


class Test(Scene):
    def construct(self):
        myTemplate = TexTemplate(documentclass='\\documentclass[preview, varwidth=240px]{standalone}')
        myTemplate.add_to_preamble(r'\usepackage{microtype, mlmodern}')
        myTemplate.add_to_preamble(r'\usepackage[sfdefault, scaled=0.85]{inter}')
        myTemplate.add_to_preamble(r'\usepackage[bb=ncmbbk, bfbb]{mathalpha}')       
        #myTemplate.add_to_preamble(r"\usepackage{xfrac}")
        #myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        myTemplate.add_to_preamble(r'\usepackage[onehalfspacing]{setspace} ')

        self.camera.background_color = COLOR_BG

        MY_BLUE = '#CCDEE9'
        
        text01 = Tex(r'Eine Folge ist eine Aufzählung von unendlich vielen Zahlen $a_i$ und wird mit runden Klammern geschrieben: \[(a_i)_{i\in\mathbb{N}}.\]', tex_template=myTemplate)
        self.add(text01)


class IntroPicture(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG
        myTemplate = TexTemplate(documentclass='\\documentclass[preview, varwidth=240px]{standalone}')
        myTemplate.add_to_preamble(r'\usepackage{microtype, mlmodern}')
        myTemplate.add_to_preamble(r'\usepackage[sfdefault, scaled=0.85]{inter}')
        myTemplate.add_to_preamble(r'\usepackage[bb=ncmbbk, bfbb]{mathalpha}')       
        myTemplate.add_to_preamble(r"\usepackage{xfrac}")
        rectangles_list = []
        for i in range(5):
            w,h = compute_shape(i)
            rect = Rectangle(height=h, width=w).set_fill(ManimColor(colorlist[i]), opacity=1.0)
            rectangles_list.append(rect)
        rectangles = VGroup(rectangles_list).arrange(RIGHT, buff=0.7, center=True, aligned_edge=DOWN).shift(0.5*DOWN)
        self.add(rectangles)
        for i in range(5):
            if i == 0:
                string = r'1'
            else:
                string = r'\sfrac{1}{' + str(2**i) + '}'
            text = MathTex(string, tex_template=myTemplate)
            text.next_to(rectangles_list[i], DOWN)
            self.add(text)
        title = Text('Was ist eine Folge?', font='Inter').shift(2.5*UP)
        self.add(title)
