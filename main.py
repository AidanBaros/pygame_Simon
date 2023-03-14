import pygame
from math import pi, sin, cos, sqrt
import numpy
import random

def p_2_c(theta,radus):
    x = radus * cos(theta)
    y = radus * sin(theta)
    return pygame.Vector2(x,y)

def distance_formula(x1, y1, x2, y2):
    return sqrt(((x1-x2)**2)+((y1-y2)**2))

def point_gen(theta1, theta2, radius1, radius2, steps, screen_size):
    inner = numpy.linspace(theta1, theta2, steps)
    outer = numpy.linspace(theta2, theta1, steps)

    points = []
    for i in inner:
        points.append(p_2_c(i, radius1) + pygame.Vector2(screen_size[0]//2, screen_size[1]//2))
    for i in outer:
        points.append(p_2_c(i, radius2) + pygame.Vector2(screen_size[0]//2, screen_size[1]//2))

    return points

def main():
    pygame.init()
    pygame.display.set_caption("Simon")
    screen:pygame.surface.Surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen_size = screen.get_size()
    clock = pygame.time.Clock()
    gameover = False

    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    YELLOW = (255,255,0)
    WHITE = (255,255,255)

    steps = 90

    red_points = point_gen(0,pi/2,200,400,steps,screen_size)
    blue_points = point_gen(pi/2,pi,200,400,steps,screen_size)
    green_points = point_gen(pi, 3*pi/2,200,400,steps,screen_size)
    yellow_points = point_gen(3*pi/2, 2*pi,200,400,steps,screen_size)

    sequence = []
    sequence.append(random.randint(0,4))

    while not gameover:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL] or keys[pygame.K_ESCAPE]:
                gameover = True

        for i, choice in enumerate(sequence):
            screen.fill("black")
            pygame.draw.polygon(screen,RED,red_points,0)
            pygame.draw.polygon(screen,BLUE,blue_points,0)
            pygame.draw.polygon(screen,GREEN,green_points,0)
            pygame.draw.polygon(screen,YELLOW,yellow_points,0)
            if choice == 0:
                pygame.draw.polygon(screen,WHITE,red_points,0)
            elif choice == 1:
                pygame.draw.polygon(screen,WHITE,blue_points,0)
            elif choice == 2:
                pygame.draw.polygon(screen,WHITE,green_points,0)
            elif choice == 3:
                pygame.draw.polygon(screen,WHITE,yellow_points,0)

        
        

        pygame.display.flip()

    pygame.quit()


main()