class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def __rmul__(self, other):
        return Point(other*self.x, other*self.y, other*self.z)

    def __eq__(self, other):
        if other.x == self.x and other.y == self.y and other.z == self.z:
            return True
        return False

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
