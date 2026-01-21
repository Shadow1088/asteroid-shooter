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
        self.y += self.speed * y_m

    def hit(self, amount):
        self.durability -= amount
        if not self.durability > 0:
            entities[0].pop(entities[0].index(self))


    def collisions(self):
        sx1 = self.x + self.w / 4
        sy1 = self.y + self.h / 4
        sx2 = self.x + self.w - self.w / 4
        sy2 = self.y + self.h - self.h / 4

        for ast in entities[2]:
            ax1 = ast.x
            ay1 = ast.y
            ax2 = ast.x + ast.w
            ay2 = ast.y + ast.h

            if not (
                sx2 < ax1 or
                sx1 > ax2 or
                sy2 < ay1 or
                sy1 > ay2
            ):
                self.hit(ast.durability)
