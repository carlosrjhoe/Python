from turtle import Turtle

def desenho_quadrado():
    caneta = Turtle()
    for i in range(4):
        caneta.fd(100)
        caneta.lt(90)

if __name__ == '__main__':
    desenho_quadrado()