class sii:
    def __init__(self, canvas):
        self.canvas = canvas
        self.items = []

    def si(self, x):
        self.items.append(self.canvas.create_rectangle(
            x+5, 50, x-5, 70, fill='Orange'))

    def loop(self, spxy):
        self.xys = []
        self.ud = 0
        for itme in range(len(self.items)):
            if itme < len(self.items):
                self.xy = self.canvas.coords(self.items[itme])
                self.xys.append(self.xy)
                if self.xy[3] > 434:
                    try:
                        if spxy[0] < self.xy[2] and self.xy[0] < spxy[2]:
                            self.ud += 1
                        self.canvas.delete(self.items[itme])
                        del self.items[itme]
                    except:
                        pass
                try:
                    self.canvas.move(self.items[itme], 0, 8)
                except:
                    pass
        return self.ud
