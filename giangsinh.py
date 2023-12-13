import turtle as t
from turtle import *
import random as r
import time

t.title("moclai03")
n = 100.0
speed("fastest")
screensize( bg='black')
left(90)
t.color("dark red", "red")
t.write("moclai03", align="center", font=("Comic Sans MS", 10, "bold"))  
forward(2.5 * n)
color("red", "yellow")
begin_fill()
left(126)
for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)

def drawlight():
    if r.randint(0, 20) == 0:
        color("red")
        begin_fill()  # Bắt đầu đổ màu
        circle(6)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 2:
        color('yellow')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 4:
        color('yellow')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 1:
        color('green')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu\
    elif r.randint(0, 20) == 3:
        color('green')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    else:
        color('dark green')

color("dark green")
backward(n * 4.8)

def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)

tree(15, n)
backward(n / 2)

for i in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    begin_fill()  # Bắt đầu đổ màu
    circle(3)
    end_fill()  # Kết thúc đổ màu
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red")
t.write("Merry Christmas <3", align="center", font=("Comic Sans MS", 40, "bold"))

def drawsnow():
    t.ht()
    t.pensize(2)
    for i in range(200):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-500, 500))
        t.sety(r.randint(-500, 500))
        t.pd()
        dens = 6
        snowsize = r.randint(1, 10)
        for j in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360 / dens))

drawsnow()
t.done()