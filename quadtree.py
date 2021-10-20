class QuadTree:
    def __init__(self):
        self.top_left = QuadTree()
        self.top_right = QuadTree()
        self.bottom_left = QuadTree()
        self.bottom_right = QuadTree()
