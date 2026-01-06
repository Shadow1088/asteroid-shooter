from classes.main.objects import Objects
from variables import ship_speed, entities


class Ship(Objects):
    def __init__(self, x: int, y: int, w: int, h: int, image: str):
        super().__init__(x,y,w,h,image)
        self.durability = 1
        self.speed = ship_speed
        entities[0].append(self)

    def __str__(self):
        return f'{self.x}, {self.y}, {self.w}, {self.h}'

    def move(self, x_m:int, y_m:int):
        self.x += self.speed * x_m
        self.y += self.speed * x_y

    def hit(self, amount):
        self.durability -= amount
        if not self.durability > 0:
            entities[0].pop(entities[0].index(self))


    def collisions(self):
        for ast in entities[2]:
            if not(
                self.x+self.w < ast.x or
                self.y+self.h < ast.y or
                self.x > ast.x+ast.w or
                self.y > ast.y+ast.h
            ): self.hit(ast.durability)
