import rectangle

class QuadTree:
    def __init__(self, width: int, height: int, node_capacity: int = 4):
        self.width = width
        self.height = height
        self.node_capacity = node_capacity

        self.items: rectangle = []

    def insert_rectangle(self, rectangle):
        if len(self.items) < self.node_capacity:
            self.items.append(rectangle)

    def subdivide(self):
        self.top_left = QuadTree()
        self.top_right = QuadTree()
        self.bottom_left = QuadTree()
        self.bottom_right = QuadTree()
