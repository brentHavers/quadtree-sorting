from __future__ import annotations

class Rectangle:
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def right(self):
        return self.left + self.width
    
    def bottom(self):
        return self.top + self.height

    def intersects(self, other: Rectangle):

        return not((self.right() < other.left) or
        (other.top > self.bottom()) or
        (other.right() < self.left) or
        (self.top > other.bottom()))

    def __str__(self):
        return f'top: {self.top} left: {self.left} bottom: {self.bottom()} right: {self.right()}'
