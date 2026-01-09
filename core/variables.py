from time import time
IMAGES = {}

running = True
entities = [[],[],[]] # P, L, A, C

asteroid_speed_range = (3, 10)
asteroid_size_range = (50, 150)
asteroid_spawn_interval = 0.01 # s

last_spawn_time = time()

ship_speed = 8
bullet_speed = 8

score = 0
