'''
'''
from classes.asteroids.asteroid import Asteroid
from variables import *
from functions import loadImages

loadImages("../media/images/")

Asteroid.spawn_random()
print(*entities[2])
entities[2][0].hit(1)
print(*entities[2] if entities[2] != [] else "test")
ast1 = Asteroid(1,1,1,1,"asteroid",1,2)
print(entities[2][0])
