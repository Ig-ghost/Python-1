#abstract classes and abstract methods

#abstract classes -> makes some rules 

from abc import ABC, abstractmethod

class Shape(ABC): #abstract class
    @abstractmethod
    def printArea(self): #abstract method
        return 0

class Rect(Shape):
    def __init__(self):
        self.length = 5
        self.breadth = 8

    def printArea(self):
        print(self.length * self.breadth)

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 5

    def printArea(self):
        print(3.14 * self.radius ** 2)

newRect = Rect()
newRect.printArea()

newCircle = Circle()
newCircle.printArea()

lst = [81, 2, 3, 45, 5, 6]
print(lst[3])

# for i in lst:
#     # i = 0
#     print(i)

for i in range(len(lst)):
    print(lst[i])

