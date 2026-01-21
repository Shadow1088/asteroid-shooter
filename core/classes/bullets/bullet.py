from classes.main.objects import Objects
from variables import entities


class Bullet(Objects):
    def __init__(self, x: int, y: int, w: int, h: int, image: str, speed:int, damage:int, direction: float=0):
        super().__init__(x, y, w, h, image)
        self.direction = direction
        self.speed = speed
        self.damage = damage
        entities[1].append(self)

    def move(self):
        self.y -= self.speed
        self.x += self.speed * self.direction
