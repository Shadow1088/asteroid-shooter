from core.classes.main.objects import Objects


class Bullet(Objects):
    def __init__(self, x: int, y: int, w: int, h: int, image: str):
        super().__init__(x, y, w, h, image)
