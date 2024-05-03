from tkinter import *


WIDTH, HEIGHT = 300, 200
BALL_DIAMETR = 20
BALL_X1 = WIDTH /2 - BALL_DIAMETR /2 
BALL_Y1 = HEIGHT /2 - BALL_DIAMETR /2 
BALL_DX = 5
BALL_DY = 5

c = Canvas(width=WIDTH, height=HEIGHT, bg='white')
c.focus_set()
c.pack()
ball = c.create_oval(BALL_X1, BALL_Y1, BALL_X1 + BALL_DIAMETR, BALL_Y1 + BALL_DIAMETR, fill='red')


def move_ball(dx, dy):
    global BALL_X1, BALL_Y1, BALL_DX, BALL_DY, BALL_DIAMETR
    
    # выход за левую границу
    if dx < 0 and BALL_X1 - BALL_DX > -1:
        BALL_X1 = BALL_X1 + BALL_DX * dx
    # выход за правую границу
    if dx > 0 and BALL_X1 + BALL_DIAMETR + BALL_DX < WIDTH +1:
        BALL_X1 = BALL_X1 + BALL_DX * dx
    # выход за верхную границу
    if dy < 0 and BALL_Y1 - BALL_DY > -1:
        BALL_Y1 = BALL_Y1 + BALL_DY * dy
    # выход за нижнюю границу
    if dy > 0 and BALL_Y1 + BALL_DIAMETR + BALL_DY < HEIGHT +1:
        BALL_Y1 = BALL_Y1 + BALL_DY * dy

    c.moveto(ball, BALL_X1, BALL_Y1)


def control(event):
    if event.keysym == 'Left':
        move_ball(-1, 0)
    if event.keysym == 'Right':
        move_ball(1, 0)
    if event.keysym == 'Up':
        move_ball(0, -1)
    if event.keysym == 'Down':
        move_ball(0, 1)


def get_coords():
    X1, Y1, X2, Y2 = c.coords(ball)
    X1 -= 1
    Y1 -= 1
    X2 -= 1
    Y2 -= 1
    print(f'Coords: X1={X1}, Y1={Y1}, X2={X2}, Y2={Y2}')
    
    c.after(1000, get_coords)


c.bind('<Key>', control)
get_coords()

mainloop()