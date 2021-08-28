class si:
    def __init__(self, canvas):
        self.canvas = canvas
        self.items = []
        self.xy = [0, 0, 0, 0]

    def sie(self, x):
        self.items.append(self.canvas.create_rectangle(x-5, 430, x+5, 400))

    def loop_move(self):
        self.xys = []
        for item in range(len(self.items)):
            if item < len(self.items):
                self.canvas.move(self.items[item], 0, -10)

                self.xy = self.canvas.coords(self.items[item])

                if self.xy[1] < 39:

                    try:
                        self.canvas.delete(self.items[item])
                        del self.items[item]
                    except:
                        pass
                else:
                    self.xys.append(self.xy)
