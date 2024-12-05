class SCPs:
    def __init__(self, x, y, canvas, fraction):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.fraction = fraction
        self.create()
    def create(self):
        if self.fraction == '173':
            self.scp173 = self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='red')
        if self.fraction == '106':
            self.scp106 = self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='black')