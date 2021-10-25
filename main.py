import sys
from quadtree import QuadTree
from rectangle import Rectangle

def populate_quadtree():
    boundary = Rectangle(0, 0, 100, 100)
    qt = QuadTree(boundary, 4)
    qt.display_debug_details()

def test_rectangle_intersection():
    rect1 = Rectangle(0, 0, 10, 10)
    rect2 = Rectangle(5, 5, 10, 10)

    intersect = rect1.intersects(rect2)
    print (f'Do these rectangles intersect? {intersect}')

populate_quadtree()