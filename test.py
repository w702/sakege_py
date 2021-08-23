from random import random
from pygame.locals import *
import pygame as pg
import sys, time
import random

from pygame.constants import K_SPACE

y=200
dy=4
x=200
dx=4
x1=300 * random.random()
x2=300 * random.random()
dx1=-4
dx2=4
a=200
b=560
rocketx=20
rockety=40
pg.init()
screen = pg.display.set_mode((400, 600))
pg.display.set_caption('Hello World!')
while True:
    pressed_key = pg.key.get_pressed()
    if pressed_key[K_LEFT] and a > 0:
        a-=7
    if pressed_key[K_RIGHT] and a < 380:
        a+=7
    if pressed_key[K_UP] and b > 0:
        b-=7
    if pressed_key[K_DOWN] and b < 560:
        b+=7
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (0, 255, 0), (x, y), 15, 500)
    pg.draw.circle(screen, (0, 255, 0), (x1, y), 15, 500)
    pg.draw.circle(screen, (0, 255, 0), (x2, y), 15, 500)

    pg.draw.rect(screen, (0, 255, 0), (a, b, rocketx, rockety))
    pg.display.update()

    y += dy
    if y + 15> 600 or y < 15:
        dy = -dy
    time.sleep(0.005)
    x += dx
    if x + 15> 400 or x < 15:
        dx = -dx
    time.sleep(0.005)

    y += dy
    if y + 15> 600 or y < 15:
        dy = -dy
    time.sleep(0.005)
    x1 += dx1
    if x1 + 15> 400 or x1 < 15:
        dx1 = -dx1
    time.sleep(0.005)

    y += dy
    if y + 15> 600 or y < 15:
        dy = -dy
    time.sleep(0.005)
    x2 += dx2
    if x2 + 15> 400 or x2 < 15:
        dx2 = -dx2
    time.sleep(0.005)

    if(y + dy > b and y + dy < b + rockety):
        if x > a and x < a + rocketx :
            pg.quit()
            sys.exit()
        if x1 > a and x1 < a + rocketx :
            pg.quit()
            sys.exit()
        if x2 > a and x2 < a + rocketx :
            pg.quit()
            sys.exit()
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
