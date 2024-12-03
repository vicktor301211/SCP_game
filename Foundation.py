class Foundation:
    def __init__(self, canvas, x, y, hp, xp, mentality_health, color):
        self.hp = hp
        self.xp = xp
        self.mentality_health = mentality_health
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.create()

    def create(self):
        self.chel = self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill=self.color)