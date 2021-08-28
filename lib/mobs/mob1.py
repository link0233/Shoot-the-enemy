import random
from lib.sii import sii

class mob1:
    def __init__(self, canvas):
        self.canvas = canvas
        self.items = []
        self.sii = sii(canvas)
        self.xys = []

    def ru(self, gj):
        for f in range(gj):
            self.x = random.randint(0, 590)
            self.items.append([self.canvas.create_rectangle(
                self.x, 0, self.x+50, 50, fill='blue'), 5, self.canvas.create_text(self.x+25, 25, text='5')])

    def loop(self, sixy, spxy):
        self.ud = self.sii.loop(spxy)
        for itme in range(len(self.items)):
            if itme < len(self.items):

                self.random = random.randint(1, 50)  # 移動
                if self.random == 1:
                    self.random = random.randint(1, 2)
                    self.xy = self.canvas.coords(self.items[itme][0])
                    if self.random == 1:
                        if self.xy[2] < 640:
                            self.random = random.randint(1, 15)
                            self.canvas.move(
                                self.items[itme][0], self.random, 0)
                    else:
                        if self.xy[0] > 0:
                            self.random = random.randint(1, 15)*-1
                            self.canvas.move(
                                self.items[itme][0], self.random, 0)

                self.random = random.randint(1, 100)  # 射擊
                if self.random == 1:
                    self.xy = self.canvas.coords(self.items[itme][0])
                    self.x = (self.xy[2]+self.xy[0])//2
                    self.sii.si(self.x)

            if itme < len(self.items):
                self.xy = self.canvas.coords(self.items[itme][0])  # 碰撞
                for six in sixy:
                    if self.xy[3] > six[1] and self.xy[0] < six[2] and self.xy[2] > six[0]:
                        self.items[itme][1] -= 1
                        try:
                            if self.items[itme][1] < 1:
                                self.canvas.delete(self.items[itme][0])
                                self.canvas.delete(self.items[itme][2])
                                del self.items[itme]
                        except:
                            self.canvas.delete(self.items[itme][0])
                            self.canvas.delete(self.items[itme][2])
                            del self.items[itme]

            if itme < len(self.items):
                self.canvas.delete(self.items[itme][2])
                self.xy = self.canvas.coords(self.items[itme][0])
                self.x = (self.xy[0]+self.xy[2])//2
                self.items[itme][2] = self.canvas.create_text(
                    self.x, 25, text=str(self.items[itme][1]))
        self.xys = self.sii.xys
