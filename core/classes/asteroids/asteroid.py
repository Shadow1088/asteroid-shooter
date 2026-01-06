from classes.main.objects import Objects
from random import randint, uniform
from variables import asteroid_speed_range, entities, asteroid_size_range

class Asteroid(Objects):
    def __init__(self, x: int, y: int, w: int, h: int, image: str, durability: int, speed: int=1):
        super().__init__(x, y, w, h, image)
        self.durability = durability
        self.speed = speed if speed != 1 else randint(*asteroid_speed_range)
        self.direction=uniform(-2/3,2/3)
        entities[2].append(self)

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.durability}, {self.speed}'

    def hit(self, amount):
        self.durability -= amount
        if not self.durability > 0:
            entities[2].pop(entities[2].index(self))

    def move(self):
        self.y += self.speed
        self.x += self.speed * self.direction


    def collisions(self):
        for bul in entities[1]:
            if not(
                self.x+self.w < bul.x or
                self.y+self.h < bul.y or
                self.x > bul.x+bul.w or
                self.y > bul.y+bul.h
            ): self.hit(bul.damage)


    @classmethod
    def spawn_random(cls):
        size = randint(*asteroid_size_range)
        return cls(randint(100,1180), -500, size, size, "asteroid", 1)
