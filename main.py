from Foundation import *
from tkinter import *
w = Tk()
w.title('Меню')
canv = Canvas(w, width=800, height=800, bg = 'alice blue')
canv.pack()
player = Foundation(canvas=canv, x = 350, y = 350, hp = 100, xp = 0, mentality_health=100, color = 'yellow')
w.mainloop()