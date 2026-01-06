from core.classes.asteroids.asteroid import Asteroid
from core.variables import *

Asteroid.spawn_random()
print(*entities[2])
entities[2][0].hit(1)
print(*entities[2] if entities[2] != [] else "test")
ast1 = Asteroid(1,1,1,1,"asteroid",1,2)
print(*entities[2])
