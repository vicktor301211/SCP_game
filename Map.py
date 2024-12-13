class Wall:
    def __init__(self, canvas, x, y, width, height, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.create()
    def create(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
class Floor:
    def __init__(self, canvas, x, y, width, height, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.create()
    def create(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)