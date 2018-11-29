import math


class Vector:
    """
    A simple n-dimensional vector class. Supports addition, subtraction, L2 Norm,
    dot product and scalar multiplication
    """

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __eq__(self, other):
        return self.components == other.components

    def __abs__(self):
        """ Returns L2 (Euclidean) Norm """
        return math.sqrt(sum([c**2 for c in self.components]))

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        i=0
        sum=[]
        for c in components:
            sum.append(self.components[i]+other.components[i])
        return Vector(sum)

    def __mul__(self, other):
        """ Returns dot product """
        i=0
        for c in components:
           total+= self.components[i] * other.components[i]
            i+=1
        return total
     
    def __rmul__(self, other):
        """ Supports (left) scalar multiplication """
        return Vector(self.x * other, self.y * other)

    def __neg__(self):
        """ Unary minus support """
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        """ Returns component-wise difference as a Vector """
        return self + -other


def angle(a: Vector, b: Vector, degrees=True) -> float:
    """ Returns the angle between two Vectors in degrees unless degrees=False """
    a = math.acos((a*b)/(abs(a)*abs(b)))
    if degrees:
        return math.degrees(a)
    else:
        return a


