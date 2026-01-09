from classes.asteroids.asteroid import Asteroid
from classes.main.ship import Ship
from classes.bullets.bullet import Bullet

import pygame
from time import time

from settings import *
from functions import *
from variables import *


pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

loadImages("../media/images/")
print(IMAGES)

start_time = time()

spaceship = Ship(WINDOW_WIDTH//2-DEFAULT_SHIP_SIZE//2, WINDOW_HEIGHT-DEFAULT_SHIP_SIZE, DEFAULT_SHIP_SIZE, DEFAULT_SHIP_SIZE, "spaceship")

while running:

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        spaceship.move(-1,0)
    if pressed[pygame.K_RIGHT]:
        spaceship.move(1,0)
    if pressed[pygame.K_UP]:
        spaceship.move(0,-1)
    if pressed[pygame.K_DOWN]:
        spaceship.move(0,1)
    if pressed[pygame.K_SPACE]:
        Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    if entities[0] == []:
        running = False

    screen.fill("black")

    if (time()- last_spawn_time) > asteroid_spawn_interval:
        Asteroid.spawn_random()
        last_spawn_time = time()

    # RENDER YOUR GAME HERE


    for ent in entities[0]:
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        ent.collisions()
        if ent.y > WINDOW_HEIGHT+ent.h:
            entities[0].pop(entities[0].index(ent))



    for ent in entities[1]:
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        ent.move()
        if ent.y > WINDOW_HEIGHT+ent.h:
            entities[1].pop(entities[1].index(ent))


    for ent in entities[2]:
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        ent.collisions()
        ent.move()
        if ent.y >= WINDOW_HEIGHT+ent.h:
            entities[2].pop(entities[2].index(ent))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
