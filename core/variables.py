from time import time
IMAGES = {}

running = True
entities = [[],[],[],[]] # P, L, A, C

asteroid_speed_range = (3, 10)
asteroid_size_range = (50, 150)
asteroid_spawn_interval = 1 # s

chest_spawn_interval = 1

last_spawn_time = time()
last_chest_spawn_time = time()

ship_speed = 8
bullet_speed = 8

level=0
score = 0
