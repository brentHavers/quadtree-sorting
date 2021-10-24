import sys
from quadtree import QuadTree
from rectangle import Rectangle

def populate_quadtree():
    boundary = Rectangle(0, 0, 100, 100)
    qt = QuadTree(boundary, 4)
    qt.display_debug_details()

populate_quadtree()