from pygame import *
import random
import time as t
from math import pi as PI
init()
def relax():
    size = [1366,768]
    screen = display.set_mode(size, FULLSCREEN)
    clock = time.Clock()
    Font = font.SysFont('comicsansms', 72)
    text = Font.render('Propagation of plane Wavefront', True, (0, 128, 255))

    while True:
        color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        color1 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        color2 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        clock.tick(70)
        for E in event.get():
            if E.type == QUIT:
                quit()
            if E.type == KEYDOWN:
                if E.key == K_ESCAPE:
                    quit()
                    return
        screen.fill((0, 0, 0))
        screen.blit(text, (60, 600) )
        for i in range(20, 1200, 30):
            draw.line(screen, (255,255,255), (i, 20), (i, 500), 5)
            display.update()
            t.sleep(0.1)
            for j in range(20, 480, 60):
                draw.arc(screen, (255,0,0), (i-30, j, 60, 60), -PI/2, PI/2, 4)
                display.update()
                t.sleep(0.1)

        display.update()
          
    quit()

relax()
