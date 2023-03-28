from quadtree import QuadTree
from rectangle import Rectangle

def populate_quadtree():
    boundary = Rectangle(0, 0, 100, 100)
    qt = QuadTree(boundary, 4)

    rect1 = Rectangle(1, 1, 1, 1)
    rect2 = Rectangle(1, 5, 1, 1)
    rect3 = Rectangle(5, 1, 1, 1)
    rect4 = Rectangle(25, 25, 1, 1)
    rect5 = Rectangle(60, 25, 1, 1)
    
    qt.insert_rectangle(rect1)
    qt.insert_rectangle(rect2)
    qt.insert_rectangle(rect3)
    qt.insert_rectangle(rect4)
    qt.insert_rectangle(rect5)

    # for debugging
    print(f'\n{qt.top_left}')
    print(f'\n{qt.top_right}')
    print(f'\n{qt.bottom_left}')
    print(f'\n{qt.bottom_right}')

def test_rectangle_intersection():
    rect1 = Rectangle(0, 0, 10, 10)
    rect2 = Rectangle(5, 5, 10, 10)

    intersect = rect1.intersects(rect2)
    print (f'Do these rectangles intersect? {intersect}')

populate_quadtree()