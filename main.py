import random


from Foundation import *
from tkinter import *
from Map import *

w = Tk()
w.title('Меню')
canv = Canvas(w, width=800, height=800, bg = 'alice blue')
canv.pack(expand=True, fill=BOTH)
def generate():
    Floor(canvas=canv, x = 0, y = 0, width = 800, height = 800, color = 'black')
    room = ['I_coridor']
    selected_room = random.choice(room)
    if selected_room == room[0]:
        wall1 = Wall(canvas=canv, x = 0, y=150, width = 800, height = 10, color = '#D3D3D3')
        wall2 = Wall(canvas=canv, x = 0, y=650, width = 800, height = 10, color = '#D3D3D3')
        wall3 = Wall(canvas=canv, x = 0, y=160, width = 10, height = 500, color = '#D3D3D3')
        wall4 = Wall(canvas=canv, x = 790, y=160, width = 10, height = 500, color = '#D3D3D3')
generate()

player = Foundation(canvas=canv, x = 350, y = 350, hp = 100, xp = 0, mentality_health=100, fraction='scientist')
w.mainloop()