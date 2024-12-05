class Insurgency:
    def __init__(self, canvas, x, y, hp, xp, mentality_health, fraction):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.hp = hp
        self.xp = xp
        self.mentality_health = mentality_health
        self.fraction = fraction
        self.create()

    def create(self):
        if self.fraction == 'chaos':
            self.Chaos_insurgency = self.canvas.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill='green')
        elif self.fraction == 'D':
            self.D_class = self.canvas.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill = 'orange')