from lib.si import si


class sprinnn:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.sif = si(canvas)
        self.item = self.canvas.create_rectangle(
            200, 430, 250, 480, fill='Black')
        self.canvas.bind('<Motion>', self.mot)
        self.canvas.bind('<B1-Motion>', self.b1mot_si)
        self.canvas.bind('<Button-1>', self.sit)
        self.moveby(self.x)
        self.dk = 50
        self.time = 0
        self.dkkd = 50
        self.timee = 0
        self.text = self.canvas.create_text(
            50, 10, width=80, text='剩餘子彈數'+str(self.dk))
        self.text2 = self.canvas.create_text(
            50, 10, width=80, text='剩餘血量'+str(self.dkkd))

    def loop(self, siixys, ssixys):
        self.moveby(self.x)

        self.sif.loop_move()
        self.time += 1
        self.timee += 1

        if self.time > 49:
            self.dk += 1
            self.time = 0
        if self.timee > 249:
            self.dkkd += 2
            self.timee = 0

        self.sixy = self.sif.xys
        self.xy = self.canvas.coords(self.item)

        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(
            40, 10, width=100, text='剩餘子彈數'+str(self.dk))
        self.canvas.delete(self.text2)
        self.text2 = self.canvas.create_text(
            40, 20, width=100, text='剩餘血量'+str(self.dkkd))

    def moveby(self, x):
        self.xy = self.canvas.coords(self.item)
        self.xu = self.x-(self.xy[0]+self.xy[2])//2
        self.canvas.move(self.item, self.xu, 0)

    def mot(self, event):
        self.x = event.x

    def b1mot_si(self, event):
        self.x = event.x

        if self.dk > 0 and self.time % 4 == 0:
            self.dk -= 1
            self.xy = self.canvas.coords(self.item)
            self.xt = (self.xy[0]+self.xy[2])//2
            self.sif.sie(self.xt)

    def sit(self, event):
        if self.dk > 0:
            self.dk -= 1
            self.xy = self.canvas.coords(self.item)
            self.xt = (self.xy[0]+self.xy[2])//2
            self.sif.sie(self.xt)
