from dataclasses import astuple, dataclass


@dataclass
class Point:

    x: float
    y: float
    z: float

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        return Point(other*self.x, other*self.y, other*self.z)

    def __rmul__(self, other):
        return Point(other*self.x, other*self.y, other*self.z)

    def __iter__(self):
        yield from astuple(self)