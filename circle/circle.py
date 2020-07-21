import cmath


class Circle:
    def __init__(self, radius: float = 1):

        self._radius: float = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = new_radius

    @property
    def diameter(self) -> float:
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter) -> None:
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")
        self.radius = diameter/2

    @property
    def area(self) -> float:
        return cmath.pi * self.radius * self.radius

    @area.setter
    def area(self, area) -> None:
        raise AttributeError

    def __repr__(self):
        return f"Circle({self.radius})"
