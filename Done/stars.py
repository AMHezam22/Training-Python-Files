import turtle
a = turtle.Turtle()

a.penup()
a.goto(-200, 100)
a.pendown()


def star(mouse, size, speed, col="yellow", bg="black"):
    a.speed(speed)
    a.color(col)
    a.getscreen().bgcolor(bg)
    if size<=10:
        return
    else:
        mouse.begin_fill()
        for i in range(5):
            mouse.forward(size)
            star(mouse, size / 3, speed, col, bg)
            mouse.__left(216)
            mouse.end_fill()


star(a, int(input("input the size: ")), int(input("input the speed: ")), input("input the mouse color: "),
     input("input the background color: "))
turtle.done()
