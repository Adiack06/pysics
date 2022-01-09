import math

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1920, 900))


running: bool = True
lasttime = time.time()

Xposition = 100
Yposition = 100
Xvelocity = 0
Yvelocity = 0
def handle_event(event):
    global  running
    if event.type == pygame.QUIT:
        running = False

while running:
    keys = pygame.key.get_pressed()
    deltatime = time.time() - lasttime
    lasttime = time.time()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        handle_event(event)

    if keys[pygame.K_SPACE]:
        Yvelocity = Yvelocity - (980 * deltatime)

    Yvelocity = Yvelocity + (980 * deltatime)
    xmousepos = pygame.mouse.get_pos()[0]
    ymousepos = pygame.mouse.get_pos()[1]

    Angle = math.atan2(Yposition-ymousepos ,Xposition-xmousepos)
    Yvelocity += (math.sin(Angle))*(-980*deltatime)
    Xvelocity += (math.cos(Angle))*(-980*deltatime)

    #claclulate
    Xposition =Xposition + (Xvelocity * deltatime)
    Yposition =Yposition + (Yvelocity * deltatime)

    if Yposition > 835:
        Yvelocity = 0.9*(Yvelocity*-1)
        Yposition = 835

    #draw
    # left
    pygame.draw.polygon(screen, (150, 150, 150), ((0, 0), (0, 900), (960, 450)), width=0)
    # top
    pygame.draw.polygon(screen, (255, 255, 255), ((0, 0), (1920, 0), (960, 450)), width=0)
    # rigth
    pygame.draw.polygon(screen, (150, 150, 150), ((1920, 0), (1920, 900), (960, 450)), width=0)
    # bottem
    pygame.draw.polygon(screen, (50, 50, 50), ((0, 900), (1920, 900), (960, 450)), width=0)

    pygame.draw.circle(screen, (100 , 100 ,100) , (Xposition , Yposition),65)
    pygame.draw.circle(screen, (255, 255, 255), (xmousepos, ymousepos), 65)

    pygame.display.flip()
