'''
实现上传资料中Hanoi.exe(Windows系统运行)的效果：
（1）实现控制台显示部分
（2）实现turtle部分
本次作业满分300，第二步200分为选做（提交日期可适当
延长）。
对于Mac系统，不必封装为exe
'''

import sys
import turtle as tl


def hanoi(n, src, dst, mid):
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        turtle_draw(n, src, dst)
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        turtle_draw(n, src, dst)
        hanoi(n-1, mid, dst, src)


def press_to_exit():
    input("Program finished, please press any key to exit.")
    sys.exit()


def turtle_initialization(n):
    tl.speed(1000)
    tl.colormode(255)
    tl.pensize(0)
    tl.setup(600, n * 60 + 120)
    tl.hideturtle()

    for i in range(1, n+1):
        turtle_draw(i, 'A', 'A')

    hanoi(n, 'A', 'C', 'B')

    turtle_endfill(n)


def turtle_draw(n, src, dst):
    n -= 1

    width = (n + 1) * 20

    axis = {
        'A': 100,
        'B': 300,
        'C': 500
    }

    xclear = axis[src] - width/2 - 315
    yclear = - (n * 30 - 45)
    xdraw = axis[dst] - width/2 - 300
    ydraw = - (n * 30 - 45)

    color = [
        (116, 209, 234),
        (234, 39, 194),
        (0, 170, 218),
        (0, 183, 150),
        (234, 39, 194),
        (180, 232, 69),
        (180, 117, 59),
        (219, 42, 213)
    ]

    tl.penup()

    tl.goto(xclear, yclear)
    tl.color(255, 255, 255)
    tl.begin_fill()
    tl.pendown()
    for i in range(2):
        tl.fd(width+30)
        tl.left(90)
        tl.fd(30)
        tl.left(90)
    tl.fillcolor(255, 255, 255)
    tl.end_fill()
    tl.penup()

    tl.goto(xdraw, ydraw)
    tl.color(color[n])
    tl.begin_fill()
    tl.pendown()
    for i in range(2):
        tl.fd(width-2)
        tl.circle(2, 90)
        tl.fd(26)
        tl.circle(2, 90)
    tl.fillcolor(color[n])
    tl.end_fill()
    tl.penup()


def turtle_endfill(n):
    xdraw = 200
    ydraw = - (n * 30 - 30)

    tl.goto(xdraw, ydraw)
    tl.color(0, 0, 0)
    tl.write("@zfm 赵方铭 221112013", align="center", font=("黑体", 10, "italic"))



try:
    n = int(input("Pls input the disk number (less than 9): "))
    turtle_initialization(n)
except Exception as e:
    print("An error occurred, pls restart")
    print("Exception: ", e)


press_to_exit()
