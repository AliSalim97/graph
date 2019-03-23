import turtle
fp=turtle.Turtle()
fp.color("red")
fp.pensize(width=3)

def f():
    for i in range(10):
        fp.left(227/10)
        fp.circle(90,50)
        fp.left(130)
        fp.circle(90,50)
f()
turtle.done()
