from turtle import *
t = Turtle()
t.shape('circle')
t.width(3)
t.speed(0)
def draw (x,y):
    t.goto(x,y)
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def StepRight():
    t.goto(t.xcor()+5,t.ycor())
def StepLeft():
    t.goto(t.xcor()-5,t.ycor())
def StepDown():
    t.goto(t.xcor(),t.ycor()-5)
def StepUp():
    t.goto(t.xcor(),t.ycor()+5)
def Red():
    t.color('Red')
def Green():
    t.color('Green')
def Black():
    t.color('Black')
def White():
    t.color('White')
def Begin_Fill():
    t.begin_fill()
def End_Fill():
    t.end_fill()

t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()

scr.onkey(StepUp,'Up')
scr.onkey(StepDown,'Down')
scr.onkey(StepLeft,'Left')
scr.onkey(StepRight,'Right')
scr.onkey(StepRight,'Right')

scr.onkey(Red,'R')
scr.onkey(Green,'G')
scr.onkey(Black,'B')
scr.onkey(White,'W')

scr.onkey(Begin_Fill,'S')
scr.onkey(End_Fill,'F')
