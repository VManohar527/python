from abc import ABC, abstractmethod
class shape (ABC):
    @abstractmethod
    def area (self):
        pass
class circle (shape):
    def __init__ (self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
class Rectangle (shape):
    def __init__ (self, l, w):
        self.l = l
        self.w = w
    def area (self):
        return self.l * self.w

Shapes = [circle (5), Rectangle(4,6)]
for shapes in Shapes:
    print (Shapes.area())
