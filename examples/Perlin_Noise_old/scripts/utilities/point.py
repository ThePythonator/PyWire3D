from math import sqrt as math_sqrt

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return math_sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point2D(self.x + other[0], self.y + other[1])
        else:
            return Point2D(self.x + other, self.y + other)
    
    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point2D(self.x - other[0], self.y - other[1])
        else:
            return Point2D(self.x - other, self.y - other)
    
    def __mul__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x * other.x, self.y * other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point2D(self.x * other[0], self.y * other[1])
        else:
            return Point2D(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x / other.x, self.y / other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point2D(self.x / other[0], self.y / other[1])
        else:
            return Point2D(self.x / other, self.y / other)
            
    def __floordiv__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x // other.x, self.y // other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point2D(self.x // other[0], self.y // other[1])
        else:
            return Point2D(self.x // other, self.y // other)
            
    def __mod__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x % other.x, self.y % other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point2D(self.x % other[0], self.y % other[1])
        else:
            return Point2D(self.x % other, self.y % other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __neg__(self):
        return Point2D(-self.x, -self.y)

    def __pos__(self):
        return Point2D(self.x, self.y)

    def __iadd__(self, other):
        return self.__add__(other)
        
    def __isub__(self, other):
        return self.__sub__(other)
        
    def __imul__(self, other):
        return self.__mul__(other)
        
    def __idiv__(self, other):
        return self.__truediv__(other)
        
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
        
    def __imod__(self, other):
        return self.__mod__(other)

    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def __repr__(self):
        return f"({self.x}, {self.y})"