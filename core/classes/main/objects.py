from variables import IMAGES

class Objects():
    def __init__(self, x:int, y:int, w:int, h:int, image:str):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = IMAGES[image]

    def __str__(self) -> str:
        return f'{self.x}, {self.y}, {self.w}, {self.h}'
