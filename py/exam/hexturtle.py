from turtle import Turtle
t=Turtle()

def hex(t):
    for i in range(6):
        t.forward(100)
        t.left(60)
    
t.fillcolor("red")
t.begin_fill()

hex(t)
    
t.end_fill()
Turtle.done()
    