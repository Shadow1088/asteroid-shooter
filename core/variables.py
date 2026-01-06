from time import time
IMAGES = {}

running = True
entities = [[],[],[]] # P, L, A, C

asteroid_speed_range = (10, 20)
asteroid_size_range = (100, 200)
asteroid_spawn_interval = 1.5 # s

last_spawn_time = time()
