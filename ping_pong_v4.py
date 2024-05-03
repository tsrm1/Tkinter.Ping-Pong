from tkinter import *
import random
import pygame
import os

WIDTH, HEIGHT = 1600, 800
BALL_DIAMETR = 40
BALL_X1 = WIDTH /2 - BALL_DIAMETR /2 
BALL_Y1 = HEIGHT /2 - BALL_DIAMETR /2 
BALL_DX = 10
BALL_DY = 0
ARROW_X = 1
ARROW_Y = 1
PAD_W = 10
PAD_H = 100
PAD_DY = 50
FPS = 30
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0


c = Canvas(width=WIDTH, height=HEIGHT, bg='#008B8B')
c.focus_set()
c.pack()
ball = c.create_oval(BALL_X1, BALL_Y1, BALL_X1 + BALL_DIAMETR, BALL_Y1 + BALL_DIAMETR, fill='red')

# link BORDER
c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill='white')

# right BORDER
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill='white')

# middle line
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill='white')

# PADS
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill='#DA70D6' )
RIGHT_PAD = c.create_line(WIDTH - PAD_W/2 + 2, 0, WIDTH - PAD_W/2 + 2, PAD_H, width=PAD_W, fill='#DA70D6' )

# SCORE
p_1_text = c.create_text(WIDTH / 6, PAD_H / 3, text=PLAYER_1_SCORE, font='Arial 20', fill='aqua')
p_2_text = c.create_text(WIDTH - WIDTH / 6, PAD_H / 3, text=PLAYER_2_SCORE, font='Arial 20', fill='aqua')

mixer = pygame.mixer.init()
sound_effect = pygame.mixer.Sound('./ping_pong_v4.wav')

def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == 1:
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


def restart(player_start=1):
    global BALL_X1, BALL_Y1, BALL_DX, BALL_DY, ARROW_X, ARROW_Y
    BALL_X1 = WIDTH /2 - BALL_DIAMETR /2 
    BALL_Y1 = HEIGHT /2 - BALL_DIAMETR /2 
    BALL_DX = 10
    BALL_DY = 0
    ARROW_Y = 1
    if player_start == 1:
        ARROW_X = 1
    else:
        ARROW_X = -1


def ball_speed_up():
    global BALL_DX
    BALL_DX += 0.5
    # print(f"Ball speed: {BALL_DX}")


def move_right_pad(dy):
    X1, Y1, X2, Y2 = c.coords(RIGHT_PAD)
    # print(f'Coords: dy={dy}, X1={X1}, Y1={Y1}, X2={X2}, Y2={Y2}')
    if dy < 0:
        if Y1 - PAD_DY > -1:
            c.move(RIGHT_PAD, 0, PAD_DY*dy)
    if dy > 0:
        if Y2 + PAD_DY < HEIGHT + 1:
            c.move(RIGHT_PAD, 0, PAD_DY*dy)


def move_left_pad(dy):
    X1, Y1, X2, Y2 = c.coords(LEFT_PAD)
    # print(f'Coords: dy={dy}, X1={X1}, Y1={Y1}, X2={X2}, Y2={Y2}')
    if dy < 0:
        if Y1 - PAD_DY > -1:
            c.move(LEFT_PAD, 0, PAD_DY*dy)
    if dy > 0:
        if Y2 + PAD_DY < HEIGHT + 1:
            c.move(LEFT_PAD, 0, PAD_DY*dy)


def control(event):
    if event.keysym == 'w':
        move_left_pad(-1)
    if event.keysym == 's':
        move_left_pad(1)
    if event.keysym == 'Up':
        move_right_pad(-1)
    if event.keysym == 'Down':
        move_right_pad(1)


def move_ball_auto():
    global ARROW_X, ARROW_Y, BALL_X1, BALL_Y1, BALL_DX, BALL_DY, BALL_DIAMETR
    
    # выход за левую границу
    if ARROW_X < 0:
        if BALL_X1 - BALL_DX > -1:
            BALL_X1 = BALL_X1 + BALL_DX * ARROW_X
        else:
            X1, Y1, X2, Y2 = c.coords(LEFT_PAD)
            if Y1-BALL_DIAMETR/3 < BALL_Y1+BALL_DIAMETR/2 and BALL_Y1+BALL_DIAMETR/2 < Y2+BALL_DIAMETR/3:
                ARROW_X = -ARROW_X
                sound_effect.play()
                BALL_DY = random.randint(2, 10)
                ball_speed_up()
            else:
                update_score(2)
                restart(1)

    # выход за правую границу
    if ARROW_X > 0:
        if BALL_X1 + BALL_DIAMETR + BALL_DX < WIDTH +1:
            BALL_X1 = BALL_X1 + BALL_DX * ARROW_X
        else:
            X1, Y1, X2, Y2 = c.coords(RIGHT_PAD)
            if Y1-BALL_DIAMETR/3 < BALL_Y1+BALL_DIAMETR/2 and BALL_Y1+BALL_DIAMETR/2 < Y2+BALL_DIAMETR/3:
                ARROW_X = -ARROW_X
                sound_effect.play()
                BALL_DY = random.randint(2, 10)
                ball_speed_up()
            else:
                update_score(1)
                restart(2)

    # выход за верхную границу
    if ARROW_Y < 0:
        if BALL_Y1 - BALL_DY > -1:
            BALL_Y1 = BALL_Y1 + BALL_DY * ARROW_Y
        else:
            ARROW_Y = -ARROW_Y
            sound_effect.play()

    # выход за нижнюю границу
    if ARROW_Y > 0:
        if BALL_Y1 + BALL_DIAMETR + BALL_DY < HEIGHT +1:
            BALL_Y1 = BALL_Y1 + BALL_DY * ARROW_Y
        else:
            ARROW_Y = -ARROW_Y
            sound_effect.play()

    c.moveto(ball, BALL_X1, BALL_Y1)


def run_play():
    move_ball_auto()
    c.after(int(1000/FPS), run_play)


c.bind('<Key>', control)
run_play()
mainloop()