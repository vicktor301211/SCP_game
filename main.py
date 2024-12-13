from Foundation import *
from Insurgency import *
from tkinter import *
from SCPs import SCPs
from Map import Wall

w = Tk()
w.title('Меню')
canv = Canvas(w, width=800, height=800, bg = 'alice blue')
canv.pack()
def create_d_block():
    wall_1 = Wall(canvas = canv, x = 0, y = 0, width = 800, height = 10, color = 'green')
    wall_2 = Wall(canvas = canv, x = 0, y = 790, width = 800, height = 10, color = 'green')
    wall_3 = Wall(canvas = canv, x = 0, y = 10, width = 10, height = 790, color = 'green')
    wall_4 = Wall(canvas = canv, x = 790, y = 10, width = 10, height = 790, color = 'green')
    wall_5 = Wall(canvas = canv, x = 0, y = 150, width = 300, height = 10, color='green')
    wall_6 = Wall(canvas = canv, x = 500, y = 150, width = 300, height = 10, color='green')
    wall_7 = Wall(canvas = canv, x = 0, y = 310, width = 300, height = 10, color='green')
    wall_8 = Wall(canvas = canv, x = 500, y = 310, width = 300, height = 10, color='green')
    wall_9 = Wall(canvas = canv, x = 0, y = 460, width = 300, height = 10, color='green')
    wall_10 = Wall(canvas = canv, x = 500, y = 460, width = 300, height = 10, color='green')
    wall_11 = Wall(canvas = canv, x = 0, y = 620, width = 300, height = 10, color='green')
    wall_12 = Wall(canvas = canv, x = 500, y = 620, width = 300, height = 10, color='green')


anomaly2 = SCPs(canvas=canv, x = 200, y = 10, fraction='106')
anomaly1 = SCPs(canvas=canv, x = 500, y = 10, fraction='173')
enemy2 = Insurgency(canvas=canv, x= 450, y= 450, hp=100, xp= 0, mentality_health=100, fraction='D')
enemy1 = Insurgency(canvas=canv, x= 250, y= 250, hp=100, xp= 0, mentality_health=100, fraction='chaos')
player = Foundation(canvas=canv, x = 350, y = 350, hp = 100, xp = 0, mentality_health=100, fraction='scientist')
friend1 = Foundation(canvas=canv, x= 400, y = 350, hp = 100, xp = 0, mentality_health=100, fraction='security')
create_d_block()
w.mainloop()