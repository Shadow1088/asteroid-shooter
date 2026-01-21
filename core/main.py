from classes.asteroids.asteroid import Asteroid
from classes.main.ship import Ship
from classes.bullets.bullet import Bullet
from classes.chest.chest import Chest

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
    print(len(entities[1]))

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
        match ((level%10)):
            case 0:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
            case 1:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
            case 2:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
            case 3:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
            case 4:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
            case 5:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.3)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.3)
            case 6:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.3)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.3)
            case 7:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.05)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.15)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.05)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.15)
            case 8:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.3)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.05)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.15)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.05)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.15)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.3)
            case 9:
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.45)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.3)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.05)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0.15)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, 0)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.05)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.1)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.2)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.15)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.3)
                Bullet(spaceship.x+spaceship.w//2, spaceship.y, 5, 10 ,"bullet", bullet_speed, 1+level//10, -0.45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    if entities[0] == []:
        running = False

    screen.fill("black")

    if (time()- last_spawn_time) > asteroid_spawn_interval:
        Asteroid.spawn_random()
        last_spawn_time = time()

    if (time()- last_chest_spawn_time) > chest_spawn_interval:
        Chest.spawn_random()
        last_chest_spawn_time = time()


    for ent in entities[0]:
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        ent.collisions()
        if ent.y > WINDOW_HEIGHT:
            ent.y = WINDOW_HEIGHT
        if ent.x > WINDOW_WIDTH:
            ent.x = WINDOW_WIDTH
        if ent.y < -ent.h:
            ent.y = -ent.h
        if ent.x+ent.w < 0:
            ent.x = 0



    for ent in entities[1]:
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        ent.move()
        if ent.y < 0:
            entities[1].pop(entities[1].index(ent))


    for ent in entities[2]:
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        ent.collisions()
        ent.move()
        if ent.y >= WINDOW_HEIGHT+ent.h:
            entities[2].pop(entities[2].index(ent))

    for ent in entities[3]:
        l=0
        screen.blit(pygame.transform.scale(ent.image, (ent.w, ent.h)), (ent.x, ent.y))
        if not(
            ent.x+ent.w < spaceship.x or
            ent.y+ent.h < spaceship.y or
            ent.x > spaceship.x+spaceship.w or
            ent.y > spaceship.y+spaceship.h
        ): l = ent.hit(ent.durability)
        try:
            if l:
                level+=1
        except:
            pass

        ent.move()
        if ent.y >= WINDOW_HEIGHT+ent.h:
            entities[3].pop(entities[3].index(ent))


    ######### HITBOX

    #pygame.draw.rect(screen, "red", (spaceship.x+spaceship.w/4, spaceship.y+spaceship.h/4, spaceship.w-spaceship.w/4*2, spaceship.h-spaceship.h/4*2))




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
