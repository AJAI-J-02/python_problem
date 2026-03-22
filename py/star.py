from turtle import Turtle
t=Turtle()
t.fillcolor("blue")
t.begin_fill()

for i in range(5):
    t.forward(100)
    t.left(60)
    
t.end_fill()    
t.exitonclick()