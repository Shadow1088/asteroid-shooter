from classes.asteroids.asteroid import Asteroid
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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    if (time()- last_spawn_time) > asteroid_spawn_interval:
        Asteroid.spawn_random()
        last_spawn_time = time()

    print(last_spawn_time - time())
    # RENDER YOUR GAME HERE
    for ent in entities[2]:
        screen.blit(ent.image, (ent.x, ent.y))
        ent.move()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
