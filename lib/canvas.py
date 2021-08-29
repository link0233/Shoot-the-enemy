import time
from tkinter import *
from lib.sprinnn import sprinnn
from lib.mobs.mob1 import mob1
from lib.mobs.mob2 import mob2
from lib.mobs.mob3 import mob3
from lib.mobs.mob4 import mob4

class canvas(Canvas):
    def __init__(self):
        self.root = Tk()
        self.root.title('射擊遊戲')
        super(canvas, self).__init__(
            self.root, width=640, height=480, bg='#ffffff')
        self.pack()
        rd = [[1, 0, 0, 0], [2, 0, 0, 0], [2, 1, 0, 0], [3, 3, 1, 0],
              [5, 4, 1, 1], [5, 5, 3, 2], [5, 6, 3, 3], [5, 5, 5, 5]]
        self.step()
        for dk in rd:
            self.sp.dkkd += 20
            self.sp.dk += 20
            self.mob1.ru(int(dk[0]))
            self.mob2.ru(int(dk[1]))
            self.mob3.ru(int(dk[2]))
            self.mob4.ru(int(dk[3]))
            while len(self.mob1.items+self.mob2.items+self.mob3.items+self.mob4.items) > 0:
                self.loop()
        self.sp.dkkd += 100
        self.sp.dk += 100
        self.mob1.ru(15)
        self.mob2.ru(15)
        self.mob3.ru(10)
        self.mob4.ru(10)
        while len(self.mob1.items+self.mob2.items+self.mob3.items+self.mob4.items) > 0:
            self.loop()
        self.create_text(320, 240, text='you win')
        self.root.mainloop()

    def step(self):
        self.mob1 = mob1(self)
        self.mob2 = mob2(self)
        self.mob3 = mob3(self)
        self.mob4 = mob4(self)

        self.sp = sprinnn(self)

    def loop(self):
        self.sp.loop(self.mob1.xys, self.mob3.xys)
        self.mob1.loop(self.sp.sixy, self.sp.xy)
        self.mob2.loop(self.sp.sixy, self.sp.xy)
        self.mob3.loop(self.sp.sixy, self.sp.xy)
        self.mob4.loop(self.sp.sixy, self.sp.xy)

        self.sp.dkkd -= self.mob1.ud+self.mob2.ud+self.mob3.ud+self.mob4.ud

        if self.sp.dkkd < 1:
            import sys
            sys.exit()

        self.root.update()
        time.sleep(0.01)
