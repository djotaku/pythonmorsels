import cmath


class Circle:
    def __init__(self, radius: float = 1):
        self.radius: float = radius

    @property
    def diameter(self) -> float:
        return self.radius * 2

    @property
    def area(self) -> float:
        return cmath.pi * self.radius * self.radius

    def __repr__(self):
        return f"Circle({self.radius})"
