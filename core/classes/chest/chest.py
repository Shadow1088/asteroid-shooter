from classes.main.objects import Objects
from settings import *
from random import randint
from variables import *

class Chest(Objects):
    def __init__(self, x: int, y: int, w: int, h: int, image: str, speed:int):
        super().__init__(x, y, w, h, image)
        self.speed = speed if speed != 1 else randint(*asteroid_speed_range)
        self.durability = 1
        entities[3].append(self)

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.durability}, {self.speed}'

    def hit(self, amount):
        global level
        self.durability -= amount
        if not self.durability > 0:
            try:
                entities[3].pop(entities[3].index(self))
                return 1
            except:
                pass

    def move(self):
        self.y += self.speed

    @classmethod
    def spawn_random(cls):
        size = 80
        return cls(randint(100,1180), -500, size, size, "chest", 1)
