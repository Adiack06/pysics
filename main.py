import math

import pygame
import time

pygame.init()
screen_width = 1080
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


running: bool = True
lasttime = time.time()

Xposition = 100
Yposition = 100
Xvelocity = 0
Yvelocity = 0
bounce_ball_r = 65
mouse_gravity = 980
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

    Yvelocity = Yvelocity + (0 * deltatime)
    xmousepos = pygame.mouse.get_pos()[0]
    ymousepos = pygame.mouse.get_pos()[1]

    Angle = math.atan2(Yposition-ymousepos ,Xposition-xmousepos)
    Yvelocity += (math.sin(Angle))* (-(0.98/math.sqrt((Xposition-xmousepos)**2)+((Yposition-ymousepos)**2))*deltatime)
    Xvelocity += (math.cos(Angle))* (-(0.98/math.sqrt((Xposition-xmousepos)**2)+((Yposition-ymousepos)**2))*deltatime)

    #claclulate
    Xposition =Xposition + (Xvelocity * deltatime)
    Yposition =Yposition + (Yvelocity * deltatime)

    #if Yposition > screen_height-65:
        #Yvelocity = 0.9*(Yvelocity*-1)
        #Yposition = screen_height-65

    #if Yposition < 0+65:
        #Yvelocity = 0.9 * (Yvelocity * -1)
        #Yposition = 0+65

    #if Xposition < 0+65:
        #Xvelocity = 0.9 * (Xvelocity * -1)
        #Xposition = 0+65

    #if Xposition > screen_width-65:
        #Xvelocity = 0.9 * (Xvelocity * -1)
        #Xposition = screen_width-65

    #draw
    # left
    pygame.draw.polygon(screen, (150, 150, 150), ((0, 0), (0, 900), (960, 450)), width=0)
    # top
    pygame.draw.polygon(screen, (255, 255, 255), ((0, 0), (1920, 0), (960, 450)), width=0)
    # rigth
    pygame.draw.polygon(screen, (150, 150, 150), ((1920, 0), (1920, 900), (960, 450)), width=0)
    # bottem
    pygame.draw.polygon(screen, (50, 50, 50), ((0, 900), (1920, 900), (960, 450)), width=0)

    pygame.draw.circle(screen, (100 , 100 ,100) , (Xposition , Yposition),bounce_ball_r)
    pygame.draw.circle(screen, (255, 255, 255), (xmousepos, ymousepos), 65)

    pygame.display.flip()
