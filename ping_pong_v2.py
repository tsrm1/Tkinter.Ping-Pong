from tkinter import *
import random


WIDTH, HEIGHT = 300, 200
BALL_DIAMETR = 20
BALL_X1 = WIDTH /2 - BALL_DIAMETR /2 
BALL_Y1 = HEIGHT /2 - BALL_DIAMETR /2 
BALL_DX = 5
BALL_DY = 0
ARROW_X = 1
ARROW_Y = 1
FPS = 30

c = Canvas(width=WIDTH, height=HEIGHT, bg='white')
c.focus_set()
c.pack()
ball = c.create_oval(BALL_X1, BALL_Y1, BALL_X1 + BALL_DIAMETR, BALL_Y1 + BALL_DIAMETR, fill='red')


def move_ball_auto():
    global ARROW_X, ARROW_Y, BALL_X1, BALL_Y1, BALL_DX, BALL_DY, BALL_DIAMETR
    
    # выход за левую границу
    if ARROW_X < 0:
        if BALL_X1 - BALL_DX > -1:
            BALL_X1 = BALL_X1 + BALL_DX * ARROW_X
        else:
            ARROW_X = -ARROW_X
            BALL_DY = random.randint(0, 5)
            print(f"BALL_DY = {BALL_DY}")

    # выход за правую границу
    if ARROW_X > 0:
        if BALL_X1 + BALL_DIAMETR + BALL_DX < WIDTH +1:
            BALL_X1 = BALL_X1 + BALL_DX * ARROW_X
        else:
            ARROW_X = -ARROW_X
            BALL_DY = random.randint(0, 5)
            print(f"BALL_DY = {BALL_DY}")

    # выход за верхную границу
    if ARROW_Y < 0:
        if BALL_Y1 - BALL_DY > -1:
            BALL_Y1 = BALL_Y1 + BALL_DY * ARROW_Y
        else:
            ARROW_Y = -ARROW_Y

    # выход за нижнюю границу
    if ARROW_Y > 0:
        if BALL_Y1 + BALL_DIAMETR + BALL_DY < HEIGHT +1:
            BALL_Y1 = BALL_Y1 + BALL_DY * ARROW_Y
        else:
            ARROW_Y = -ARROW_Y

    c.moveto(ball, BALL_X1, BALL_Y1)

def get_coords():
    X1, Y1, X2, Y2 = c.coords(ball)
    X1 -= 1
    Y1 -= 1
    X2 -= 1
    Y2 -= 1
    print(f'Coords: X1={X1}, Y1={Y1}, X2={X2}, Y2={Y2}')
    
    c.after(int(1000/FPS), get_coords)

def run_play():
    move_ball_auto()
    c.after(int(1000/FPS), run_play)


get_coords()
run_play()
mainloop()