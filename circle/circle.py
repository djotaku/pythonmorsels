import cmath


class Circle:
    def __init__(self, radius: float = 1):
        self.radius: float = radius
        self.diameter: float = radius * 2
        self.area: float = cmath.pi * self.radius * self.radius

    def __repr__(self):
        return f"Circle({self.radius})"
