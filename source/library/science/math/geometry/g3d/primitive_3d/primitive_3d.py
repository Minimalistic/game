from pygame import math

class Primitive3D:
    position    = None
    radius      = 1
    nodes       = []

    def __init__(self):
        self.position = math.Vector3(0, 0, 0)
        pass

    def get_nodes(self):
        return [None]

    def collide(self, object):
        distance = self.position.distance_to(object.position)
        if distance < self.radius + object.radius:
            return True
        else:
            return False

    def transform(self):
        p = math.Vector3(self.position.x, self.position.y, self.position.z)
        self.translate()
        self.rotate()
        if self.position != p:
            self.get_collisions()
        pass

    def translate(self):
        pass

    def rotate(self):
        pass
