import os
from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        if self == Circle:
            self.display(self)
        elif self == Rectangle:
            self.display(self)


class Rectangle(Shape):
    def display(self):
        print("-" * 4)
        print("|  |")
        print("-" * 4)


class Circle(Shape):
    def display(self):
        print(" -- ")
        print("-  -")
        print(" -- ")


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [Rectangle]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    os.system("cls||clear")
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
