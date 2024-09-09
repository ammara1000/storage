import turtle
import time
#forward()
#left()
#home()
#backward()
#right()
#color()
#width()
#up()
#down()
#pos()
#clearscreen()
#fillcolor()
#begin_fill()
#end_fill()
s = turtle.Screen()
s.bgcolor("#000000")
s.title("lol")
t = turtle.Turtle()
t.color("#66FF66")
t.width(3)
t.fillcolor("#909000")


def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)
def triangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)
def star(size):
    for i in range(5):
        t.forward(size/2)
        t.left(144)
        t.forward(size/2)
        t.right(72)
def circle(size,quality):
    for i in range(quality):
        t.forward(10*size/quality)
        t.left(360/quality)
def rosa(size,num):
    fast()
    t.width(0.5)
    for i in range(num):
        circle(size/4,50)
        circle(size/20,50)
        circle(size/2,50)
        t.left(360/num)
    slow()
    t.width(3)
def rosa_triangle(size,num):
    fast()
    t.width(0.5)
    for i in range(num):
        triangle(size/4)
        triangle(size/20)
        triangle(size/2)
        t.left(360/num)
    slow()
    t.width(3)
def rosa_square(size,num):
    fast()
    t.width(0.5)
    for i in range(num):
        square(size/4)
        square(size/20)
        square(size/2)
        t.left(360/num)
    slow()
    t.width(3)
def rosa_mega():
    rosa_triangle(350,32)
    rosa(400,32)
    rosa_triangle(800,32)
def rosa_square_mega(num):
    for i in range(num):
        rosa_square(200*(2^i),32)
def cls():
    s.clearscreen()
    s.bgcolor("#000000")
    s.title("lol")
    t.color("#66FF66")
    t.width(3)
    t.fillcolor("#909000")
    t.home()
def fast():
    t.speed(0)
def slow():
    t.speed(6)
def full(cmd,color="#909000"):
    t.fillcolor(color)
    t.begin_fill()
    eval(cmd)
    t.end_fill()
def spiral(num,size):
    fast()
    for i in range(num):
        t.forward(i*size)
        t.backward(i*size)
        t.left(360/num)
    slow()
def cube(size):
    for i in range(4):
        t.forward(size)
        if i==0 or i==2:
            t.left(90*i+45)
            t.forward(size/2)
            t.backward(size/2)
            t.right(90*i+45)
        if i==1:
            t.right(45)
            t.forward(size/2)
            t.backward(size/2)
            t.left(45)
        t.left(90)
    t.left(45)
    t.forward(size/2)
    t.right(45)
    square(size)