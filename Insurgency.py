class Insurgency:
    def __init__(self, canvas, x, y, hp, xp, mentality_health, fraction, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.hp = hp
        self.xp = xp
        self.mentality_health = mentality_health
        self.fraction = fraction
        self.color = color

    def create(self):
        self.Chaos_insurgency = self.canvas.create_rectangle(self.x, self.y, color = 'green')
        self.D_class = self.canvas.create_rectangle(self.x, self.y, color = 'orange')