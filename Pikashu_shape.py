import turtle


def getPosition(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)


class Pikachu:

    def __init__(self):
        self.pik = turtle.Turtle()
        pik = self.pik
        pik.pensize(1)
        pik.speed(20)
        pik.ondrag(getPosition)

    def noTrace_goto(self, x, y):
        self.pik.penup()
        self.pik.goto(x, y)
        self.pik.pendown()

    def leftEye(self, x, y):
        self.noTrace_goto(x, y)
        pik = self.pik
        pik.seth(0)
        pik.fillcolor('#333333')
        pik.begin_fill()
        pik.circle(22)
        pik.end_fill()

        self.noTrace_goto(x, y + 10)
        pik.fillcolor('#000000')
        pik.begin_fill()
        pik.circle(10)
        pik.end_fill()

        self.noTrace_goto(x + 6, y + 22)
        pik.fillcolor('#ffffff')
        pik.begin_fill()
        pik.circle(10)
        pik.end_fill()

    def rightEye(self, x, y):
        self.noTrace_goto(x, y)
        pik = self.pik
        pik.seth(0)
        pik.fillcolor('#333333')
        pik.begin_fill()
        pik.circle(22)
        pik.end_fill()

        self.noTrace_goto(x, y + 10)
        pik.fillcolor('#000000')
        pik.begin_fill()
        pik.circle(10)
        pik.end_fill()

        self.noTrace_goto(x - 6, y + 22)
        pik.fillcolor('#ffffff')
        pik.begin_fill()
        pik.circle(10)
        pik.end_fill()

    def mouth(self, x, y):
        self.noTrace_goto(x, y)
        pik = self.pik

        pik.fillcolor('#88141D')
        pik.begin_fill()

        # Lower Lip
        l1 = []
        l2 = []
        pik.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            pik.right(3)
            pik.fd(a)
            l1.append(pik.position())

        self.noTrace_goto(x, y)

        pik.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            pik.left(3)
            pik.fd(a)
            l2.append(pik.position())

        # Upper Lip
        pik.seth(10)
        pik.circle(50, 15)
        pik.left(180)
        pik.circle(-50, 15)

        pik.circle(-50, 40)
        pik.seth(233)
        pik.circle(-50, 55)
        pik.left(180)
        pik.circle(50, 12.1)
        pik.end_fill()

        # Tongue
        self.noTrace_goto(17, 54)
        pik.fillcolor('#DD716F')
        pik.begin_fill()
        pik.seth(145)
        pik.circle(40, 86)
        pik.penup()
        for pos in reversed(l1[:20]):
            pik.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            pik.goto(pos[0], pos[1] + 1.5)
        pik.pendown()
        pik.end_fill()

        # Nose
        self.noTrace_goto(-17, 94)
        pik.seth(8)
        pik.fd(4)
        pik.back(8)

    # Red Cheeks
    def leftCheek(self, x, y):
        turtle.tracer(False)
        pik = self.pik
        self.noTrace_goto(x, y)
        pik.seth(300)
        pik.fillcolor('#DD4D28')
        pik.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                pik.lt(3)
                pik.fd(a)
            else:
                a += 0.05
                pik.lt(3)
                pik.fd(a)
        pik.end_fill()
        turtle.tracer(True)

    def rightCheek(self, x, y):
        pik = self.pik
        turtle.tracer(False)
        self.noTrace_goto(x, y)
        pik.seth(60)
        pik.fillcolor('#DD4D28')
        pik.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                pik.lt(3)
                pik.fd(a)
            else:
                a += 0.05
                pik.lt(3)
                pik.fd(a)
        pik.end_fill()
        turtle.tracer(True)

    def colorLeftEar(self, x, y):
        pik = self.pik
        self.noTrace_goto(x, y)
        pik.fillcolor('#000000')
        pik.begin_fill()
        pik.seth(330)
        pik.circle(100, 35)
        pik.seth(219)
        pik.circle(-300, 19)
        pik.seth(110)
        pik.circle(-30, 50)
        pik.circle(-300, 10)
        pik.end_fill()

    def colorRightEar(self, x, y):
        pik = self.pik
        self.noTrace_goto(x, y)
        pik.fillcolor('#000000')
        pik.begin_fill()
        pik.seth(300)
        pik.circle(-100, 30)
        pik.seth(35)
        pik.circle(300, 15)
        pik.circle(30, 50)
        pik.seth(190)
        pik.circle(300, 17)
        pik.end_fill()

    def body(self):
        pik = self.pik

        pik.fillcolor('#F0DD1F')
        pik.begin_fill()
        # Right face contour
        pik.penup()
        pik.circle(130, 40)
        pik.pendown()
        pik.circle(100, 105)
        pik.left(180)
        pik.circle(-100, 5)

        # Right ear
        pik.seth(20)
        pik.circle(300, 30)
        pik.circle(30, 50)
        pik.seth(190)
        pik.circle(300, 36)

        # Upper profile
        pik.seth(150)
        pik.circle(150, 70)

        # Left ear
        pik.seth(200)
        pik.circle(300, 40)
        pik.circle(30, 50)
        pik.seth(20)
        pik.circle(300, 35)
        #print(t.pos())

        # Left face contour
        pik.seth(240)
        pik.circle(105, 95)
        pik.left(180)
        pik.circle(-105, 5)

        # Left hand
        pik.seth(210)
        pik.circle(500, 18)
        pik.seth(200)
        pik.fd(10)
        pik.seth(280)
        pik.fd(7)
        pik.seth(210)
        pik.fd(10)
        pik.seth(300)
        pik.circle(10, 80)
        pik.seth(220)
        pik.fd(10)
        pik.seth(300)
        pik.circle(10, 80)
        pik.seth(240)
        pik.fd(12)
        pik.seth(0)
        pik.fd(13)
        pik.seth(240)
        pik.circle(10, 70)
        pik.seth(10)
        pik.circle(10, 70)
        pik.seth(10)
        pik.circle(300, 18)

        pik.seth(75)
        pik.circle(500, 8)
        pik.left(180)
        pik.circle(-500, 15)
        pik.seth(250)
        pik.circle(100, 65)

        # Left foot
        pik.seth(320)
        pik.circle(100, 5)
        pik.left(180)
        pik.circle(-100, 5)
        pik.seth(220)
        pik.circle(200, 20)
        pik.circle(20, 70)

        pik.seth(60)
        pik.circle(-100, 20)
        pik.left(180)
        pik.circle(100, 20)
        pik.seth(300)
        pik.circle(10, 70)

        pik.seth(60)
        pik.circle(-100, 20)
        pik.left(180)
        pik.circle(100, 20)
        pik.seth(10)
        pik.circle(100, 60)

        # Horizontal
        pik.seth(180)
        pik.circle(-100, 10)
        pik.left(180)
        pik.circle(100, 10)
        pik.seth(5)
        pik.circle(100, 10)
        pik.circle(-100, 40)
        pik.circle(100, 35)
        pik.left(180)
        pik.circle(-100, 10)
        # Right foot
        pik.seth(290)
        pik.circle(100, 55)
        pik.circle(10, 50)

        pik.seth(120)
        pik.circle(100, 20)
        pik.left(180)
        pik.circle(-100, 20)

        pik.seth(0)
        pik.circle(10, 50)

        pik.seth(110)
        pik.circle(100, 20)
        pik.left(180)
        pik.circle(-100, 20)

        pik.seth(30)
        pik.circle(20, 50)

        pik.seth(100)
        pik.circle(100, 40)

        # Right body contour
        pik.seth(200)
        pik.circle(-100, 5)
        pik.left(180)
        pik.circle(100, 5)
        pik.left(30)
        pik.circle(100, 75)
        pik.right(15)
        pik.circle(-300, 21)
        pik.left(180)
        pik.circle(300, 3)

        # Right hand
        pik.seth(43)
        pik.circle(200, 60)

        pik.right(10)
        pik.fd(10)

        pik.circle(5, 160)
        pik.seth(90)
        pik.circle(5, 160)
        pik.seth(90)

        pik.fd(10)
        pik.seth(90)
        pik.circle(5, 180)
        pik.fd(10)

        pik.left(180)
        pik.left(20)
        pik.fd(10)
        pik.circle(5, 170)
        pik.fd(10)
        pik.seth(240)
        pik.circle(50, 30)

        pik.end_fill()
        self.noTrace_goto(130, 125)
        pik.seth(-20)
        pik.fd(5)
        pik.circle(-5, 160)
        pik.fd(5)

        # Fingers
        self.noTrace_goto(166, 130)
        pik.seth(-90)
        pik.fd(3)
        pik.circle(-4, 180)
        pik.fd(3)
        pik.seth(-90)
        pik.fd(3)
        pik.circle(-4, 180)
        pik.fd(3)

        # Tail
        self.noTrace_goto(168, 134)
        pik.fillcolor('#F0DD1F')
        pik.begin_fill()
        pik.seth(40)
        pik.fd(200)
        pik.seth(-80)
        pik.fd(150)
        pik.seth(210)
        pik.fd(150)
        pik.left(90)
        pik.fd(100)
        pik.right(95)
        pik.fd(100)
        pik.left(110)
        pik.fd(70)
        pik.right(110)
        pik.fd(80)
        pik.left(110)
        pik.fd(30)
        pik.right(110)
        pik.fd(32)

        pik.right(106)
        pik.circle(100, 25)
        pik.right(15)
        pik.circle(-300, 2)
        #print(pik.pos())
        pik.seth(30)
        pik.fd(40)
        pik.left(100)
        pik.fd(70)
        pik.right(100)
        pik.fd(80)
        pik.left(100)
        pik.fd(46)
        pik.seth(66)
        pik.circle(200, 38)
        pik.right(10)
        pik.fd(10)
        pik.end_fill()

        # Tail Pattern
        pik.fillcolor('#923E24')
        self.noTrace_goto(126.82, -156.84)
        pik.begin_fill()

        pik.seth(30)
        pik.fd(40)
        pik.left(100)
        pik.fd(40)
        pik.pencolor('#923e24')
        pik.seth(-30)
        pik.fd(30)
        pik.left(140)
        pik.fd(20)
        pik.right(150)
        pik.fd(20)
        pik.left(150)
        pik.fd(20)
        pik.right(150)
        pik.fd(20)
        pik.left(130)
        pik.fd(18)
        pik.pencolor('#000000')
        pik.seth(-45)
        pik.fd(67)
        pik.right(110)
        pik.fd(80)
        pik.left(110)
        pik.fd(30)
        pik.right(110)
        pik.fd(32)
        pik.right(106)
        pik.circle(100, 25)
        pik.right(15)
        pik.circle(-300, 2)
        pik.end_fill()

        # Hat, Eye, Mouth, Cheek
        self.cap(-134.07, 147.81)
        self.mouth(-5, 25)
        self.leftCheek(-126, 32)
        self.rightCheek(107, 63)
        self.colorLeftEar(-250, 100)
        self.colorRightEar(140, 270)
        self.leftEye(-85, 90)
        self.rightEye(50, 110)
        pik.hideturtle()

    def cap(self, x, y):
        self.noTrace_goto(x, y)
        pik = self.pik
        pik.fillcolor('#CD0000')
        pik.begin_fill()
        pik.seth(200)
        pik.circle(400, 7)
        pik.left(180)
        pik.circle(-400, 30)
        pik.circle(30, 60)
        pik.fd(50)
        pik.circle(30, 45)
        pik.fd(60)
        pik.left(5)
        pik.circle(30, 70)
        pik.right(20)
        pik.circle(200, 70)
        pik.circle(30, 60)
        pik.fd(70)
        #print(t.pos())
        pik.right(35)
        pik.fd(50)
        pik.circle(8, 100)
        pik.end_fill()
        self.noTrace_goto(-168.47, 185.52)
        pik.seth(36)
        pik.circle(-270, 54)
        pik.left(180)
        pik.circle(270, 27)
        pik.circle(-80, 98)

        pik.fillcolor('#444444')
        pik.begin_fill()
        pik.left(180)
        pik.circle(80, 197)
        pik.left(58)
        pik.circle(200, 45)
        pik.end_fill()

        self.noTrace_goto(-58, 270)
        pik.pencolor('#228B22')
        pik.dot(35)

        self.noTrace_goto(-30, 280)
        pik.fillcolor('#228B22')
        pik.begin_fill()
        pik.seth(100)
        pik.circle(30, 180)
        pik.seth(190)
        pik.fd(15)
        pik.seth(100)
        pik.circle(-45, 180)
        pik.right(90)
        pik.fd(15)
        pik.end_fill()
        pik.pencolor('#000000')

    def start(self):
        self.body()


def main():
    print(' Start Painting ............ ')
    wn = turtle.Screen()
    wn.setup(width=800, height=800)
    pikachu = Pikachu()
    pikachu.start()
    turtle.mainloop()


if __name__ == '__main__':
    main()






