class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        return Point(other*self.x, other*self.y, other*self.z)

    def __rmul__(self, other):
        return Point(other*self.x, other*self.y, other*self.z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
