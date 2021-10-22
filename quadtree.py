class QuadTree:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.top_left = QuadTree()
        self.top_right = QuadTree()
        self.bottom_left = QuadTree()
        self.bottom_right = QuadTree()

    def insert_rectangle(rectangle):
        return

    def subdivide():
        return