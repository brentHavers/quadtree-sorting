from rectangle import Rectangle

class QuadTree:
    def __init__(self, boundary: Rectangle, node_capacity: int = 4):
        self.boundary = boundary
        self.node_capacity = node_capacity

        self.items: Rectangle = []

    def insert_rectangle(self, rectangle):
        if len(self.items) < self.node_capacity:
            self.items.append(rectangle)

    def subdivide(self):
        self.top_left = QuadTree()
        self.top_right = QuadTree()
        self.bottom_left = QuadTree()
        self.bottom_right = QuadTree()

    def __str__(self):
        return (f'boundary: {self.boundary}' + 
        f'\ncapacity: {self.node_capacity}' + 
        f'\nnumber of items: {len(self.items)}' + 
        f'\nitems: {self.items}')
