class Foundation:
    def __init__(self, canvas, x, y, hp, xp, mentality_health, fraction):
        self.hp = hp
        self.xp = xp
        self.mentality_health = mentality_health
        self.canvas = canvas
        self.x = x
        self.y = y
        self.fraction = fraction
        self.create()

    def create(self):
        if self.fraction == 'scientist':
            self.scientist = self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='yellow')
        elif self.fraction == 'security':
            self.security = self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='gray')