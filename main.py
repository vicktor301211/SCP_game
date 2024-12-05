from Foundation import *
from Insurgency import *
from tkinter import *
from SCPs import SCPs

w = Tk()
w.title('Меню')
canv = Canvas(w, width=800, height=800, bg = 'alice blue')
canv.pack()
anomaly2 = SCPs(canvas=canv, x = 200, y = 0, fraction='106')
anomaly1 = SCPs(canvas=canv, x = 500, y = 0, fraction='173')
enemy2 = Insurgency(canvas=canv, x= 450, y= 450, hp=100, xp= 0, mentality_health=100, fraction='D')
enemy1 = Insurgency(canvas=canv, x= 250, y= 250, hp=100, xp= 0, mentality_health=100, fraction='chaos')
player = Foundation(canvas=canv, x = 350, y = 350, hp = 100, xp = 0, mentality_health=100, fraction='scientist')
friend1 = Foundation(canvas=canv, x= 400, y = 350, hp = 100, xp = 0, mentality_health=100, fraction='security')
w.mainloop()