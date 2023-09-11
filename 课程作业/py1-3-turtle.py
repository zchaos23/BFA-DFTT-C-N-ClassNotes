from PIL import Image
import turtle as tl

'''
2022-第二学期-计算机与网络-作业3py

本程序通过调用 Pillow 库的 Image 图像处理部分，读取 example.png 图像每个像素点的 RGBA 值，
并使用 for 循环逐行将像素点描在 Turtle 画布上，从而实现根据图片生成 Turtle 像素画。

为了解决 Turtle 画笔形状为圆形，无法绘制方形像素的问题，定义了 drawsquare 函数，
通过画笔绘制方形边框再填充的方式，实现像素画的每个像素点绘制。

为了解决 Turtle 逐个像素点绘画过慢的问题，实现了将每行颜色相同的部分一次绘画完成的逻辑。
感觉应该还有很多优化的方法，不过实现难度相比这种简单粗暴的方法大得多，就没有再去摸索。

example.png 来自在网络随便找的像素画， 链接：https://www.pixiv.net/artworks/106686536
'''

# 设置放大倍率, 可调节， 影响画布大小。
size = 5

# 打开图片
img = Image.open('example1.png')

# 获取像素数据
pixels = img.load()

# Turtle 设置
tl.setup(img.size[0] * size, img.size[1] * size)  # 设置画布大小
tl.speed(10)    # 设置绘制速度
tl.colormode(255)   # 设置颜色模式
tl.pensize(0)   # 设置画笔粗细

# 绘制矩形
def drawsquare(x, y, step, color):
    tl.penup()
    tl.goto(x * size, y * size)
    tl.color(color)
    tl.begin_fill()
    tl.pendown()
    tl.forward(step * size)
    tl.right(90)
    tl.forward(size)
    tl.right(90)
    tl.forward(step * size)
    tl.right(90)
    tl.forward(size)
    tl.right(90)
    tl.fillcolor(color)
    tl.end_fill()
    tl.penup()

# 初始化移动步数
step = 1

# 循环将像素点描在画布上
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if x != 0 and x != img.size[1] - 1:
            if pixels[x,y] == pixels[x-1,y]:
                step += 1
            else:
                color = list(pixels[x-1,y])
                del color[-1]
                xPos = x - step - img.size[0]/2
                yPos = - img.size[1]/2 + y
                print('Drawing {} steps at line {}, X: {}, Y: {}, RGB color: {}'.format(step, y, x, y, color))
                drawsquare(xPos, -yPos, step, color)
                step = 1
        elif x == img.size[1] - 1:
            color = list(pixels[x, y])
            del color[-1]
            xPos = x - step - img.size[0]/2
            yPos = - img.size[1]/2 + y
            print('Drawing {} steps at line {}, X: {}, Y: {}, RGB color: {}'.format(step, y, x, y, color))
            print('Finished drawing line {}, proceed {}/{}'.format(y, y, img.size[1]))
            drawsquare(xPos, -yPos, step, color)
            step = 1
        else:
            step += 1

tl.done()
