from __future__ import annotations
from rectangle import Rectangle

class QuadTree:
    top_left = None
    top_right = None
    bottom_left = None
    bottom_right = None

    def __init__(self, boundary: Rectangle, node_capacity: int = 4):
        self.boundary = boundary
        self.node_capacity = node_capacity

        self.items: Rectangle = []

    def insert_rectangle(self, rectangle):
        if (len(self.items) < self.node_capacity) and (not(self.is_subdivided())):
            self.items.append(rectangle)
            return True

        if not(self.is_subdivided()):
            self.subdivide()
            # TODO: move self.items to children

        if (self.top_left.insert_rectangle(rectangle)):
            return True
        if (self.top_right.insert_rectangle(rectangle)):
            return True
        if (self.bottom_left.insert_rectangle(rectangle)):
            return True
        if (self.bottom_right.insert_rectangle(rectangle)):
            return True

    def subdivide(self):
        subdivision_width = self.boundary.width / 2
        subdivision_height = self.boundary.height / 2
        lower_half_top = self.boundary.top + subdivision_height
        right_half_left = self.boundary.left + subdivision_width

        top_left_boundary = Rectangle(self.boundary.top, self.boundary.left, subdivision_width, subdivision_height)
        top_right_boundary = Rectangle(self.boundary.top, right_half_left, subdivision_width, subdivision_height)
        bottom_left_boundary = Rectangle(lower_half_top, self.boundary.left, subdivision_width, subdivision_height)
        bottom_right_boundary = Rectangle(lower_half_top, right_half_left, subdivision_width, subdivision_height)

        self.top_left = QuadTree(top_left_boundary)
        self.top_right = QuadTree(top_right_boundary)
        self.bottom_left = QuadTree(bottom_left_boundary)
        self.bottom_right = QuadTree(bottom_right_boundary)

    def is_subdivided(self):
        return not(self.top_left == None)


    def __str__(self):
        return (f'boundary: {self.boundary}' + 
        f'\ncapacity: {self.node_capacity}' + 
        f'\nnumber of items: {len(self.items)}' + 
        f'\nitems: {self.items}' +
        f'\nsubdivided: {self.is_subdivided()}') 
