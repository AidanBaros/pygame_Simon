import pygame
from math import pi, sin, cos, sqrt
import numpy

def p_2_c(O,R):
    x = R * cos(O)
    y = R * sin(O)
    return pygame.Vector2(x,y)

def distance_formula(x1, y1, x2, y2):
    return sqrt(((x1-x2)**2)+((y1-y2)**2))

def point_gen(theta1, theta2, radius1, radius2, steps):
    step_dist = (theta2 - theta1) / steps
    inner = numpy.arange(theta1, theta2, step_dist)
    outer = numpy.arange(theta2, theta1, -step_dist)

    points = []
    for i in inner:
        points.append(p_2_c(i, radius1))
    for i in outer:
        points.append(p_2_c(i, radius2))

    return points

def main():
    pygame.init()
    pygame.display.set_caption("Simon")
    screen:pygame.surface.Surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screenSize = screen.get_size()
    clock = pygame.time.Clock()
    gameover = False

    RED = (255,0,0)
    BULE = (0,0,255)
    GREEN = (0,255,0)
    YELLOW = (255,255,0)

    red_points = point_gen(0,pi/2,200,400,5)
    blue_points = point_gen(pi/2,pi,200,400,5)
    green_points = point_gen(pi, 3*pi/2,200,400,5)
    yellow_points = point_gen(3*pi/2, 2*pi,200,400,5)

    while not gameover:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL] or keys[pygame.K_ESCAPE]:
                gameover = True


        screen.fill("black")
        pygame.display.flip()

    pygame.quit()


main()