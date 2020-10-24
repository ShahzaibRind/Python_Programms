
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 4

    def printArea(self):
        return self.breadth * self.length


rect1 = Rectangle()
print(rect1.printArea())

# tryObj = Shape() We Can't Make Object in Abstract Class