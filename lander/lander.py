#!/usr/bin/python
import pygame, random, sys
from pygame.locals import *
import pprint

#import pdb
#pdb.set_trace()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(pygame.locals.__dict__)


def die(screen, fuel):
    f=pygame.font.SysFont('Arial', 30)
    t=f.render('your fuel was: '+str(fuel), True, (0, 0, 0))
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit(0)
sx = 300
sy = 10
fuel = 100
dirs = 0


pygame.init()
s=pygame.display.set_mode((600, 600))
pygame.display.set_caption('lander')
img = pygame.Surface((20, 20))
img.fill((0, 255, 255))
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()
vy_safe = 0.3
vy = 0.0
main_engine = False
while True:

    clock.tick(200)

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
        elif e.type == KEYDOWN:
            #if e.key == K_LEFT and dirs != 1:dirs = 3
            #elif e.key == K_RIGHT and dirs != 3:dirs = 1
            if e.key == K_SPACE: main_engine = True
        elif e.type == KEYUP:
            #if e.key == K_LEFT and dirs != 1:dirs = 3
            #elif e.key == K_RIGHT and dirs != 3:dirs = 1
            if e.key == K_SPACE: main_engine = False
            
    s.fill((0, 0, 240))
    
    # kackulate next position
    a_moon = 0.00162
    a_engine = main_engine and -0.01 or 0.0
    ay = a_moon + a_engine
    vy = vy + ay
    sy = sy + vy
    
    print str(vy)
    if sy > 590:
        die(s, fuel)
    s.blit(img, (sx, sy))
    t=f.render(str(fuel), True, (0, 0, 0))
    s.blit(t,(300, 10))
    pygame.display.update()





