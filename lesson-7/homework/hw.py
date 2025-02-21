
import math

class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions.")
            return sum(a * b for a, b in zip(self.components, other.components))
        raise TypeError("Unsupported operation.")

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)
print(v2 - v1)
print(v1 * v2)
print(3 * v1)
print(v1.magnitude())
print(v1.normalize())
