from turtle import Turtle

def draw_square(length, angulate):
    pencil = Turtle()
    for i in range(4):
        pencil.fd(length)
        pencil.lt(angulate)

def draw_polygon(length, side, angulate):
    pencil = Turtle()
    pencil.speed(1)
    for _ in range(side):
        pencil.fd(length)
        pencil.forward(length)
        pencil.lt(angulate)

if __name__ == '__main__':
    length = 10
    side = 5
    angulate = side / 36
    draw_polygon(length, side, angulate)